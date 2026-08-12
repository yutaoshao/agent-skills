#!/usr/bin/env python3
"""Dependency-free Architecture Decision Record helper."""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
import tempfile
from pathlib import Path

STATUSES = ("proposed", "accepted", "rejected", "superseded", "deprecated")
TRANSITIONS = {
    "proposed": {"accepted", "rejected", "deprecated"},
    "accepted": {"superseded", "deprecated"},
    "rejected": {"proposed"},
    "superseded": set(),
    "deprecated": set(),
}
FILE_RE = re.compile(r"^(?P<num>[0-9]{4})-(?P<slug>[a-z0-9][a-z0-9-]*)[.]md$")
ID_RE = re.compile(r"^ADR-[0-9]{4}$")
LIST_KEYS = {
    "owners",
    "supersedes",
    "superseded_by",
    "related_tasks",
    "related_design",
    "related_specs",
}
SECTIONS = (
    "Context",
    "Decision Drivers",
    "Options Considered",
    "Decision",
    "Consequences",
    "Non-Functional Constraints",
    "Revisit Triggers",
    "Related Artifacts",
)
REQUIRED_GROUPS = (
    ("Context", ("Context",)),
    ("Decision Drivers", ("Decision Drivers",)),
    ("Options Considered", ("Options Considered",)),
    ("Decision", ("Decision",)),
    ("Consequences", ("Consequences",)),
    ("Non-Functional Constraints", ("Non-Functional Constraints",)),
    ("Implementation", ("Implementation Notes", "Implementation Constraints")),
    ("Revisit Triggers", ("Revisit Triggers",)),
    ("Evidence", ("Evidence",)),
    ("Relationships", ("Related Artifacts", "Relationships")),
)
SECTION_ALIASES = {
    "Context": ("Context",),
    "Decision Drivers": ("Decision Drivers",),
    "Options Considered": ("Options Considered",),
    "Decision": ("Decision",),
    "Consequences": ("Consequences",),
    "Implementation": ("Implementation Notes", "Implementation Constraints"),
    "Revisit Triggers": ("Revisit Triggers",),
    "Relationships": ("Related Artifacts", "Relationships"),
}
OPTIONAL_SECTIONS = ("Review Notes",)


class AdrError(Exception):
    pass


def parse_value(raw):
    value = raw.strip()
    if value in ("", "null", "~"):
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [] if not inner else [x.strip().strip("'\"") for x in inner.split(",")]
    if value.lower() in ("true", "false"):
        return value.lower() == "true"
    return value.strip("'\"")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text, "missing front matter opening marker"
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text, "missing front matter closing marker"
    metadata = {}
    current = None
    errors = []
    for number, line in enumerate(text[4:end].splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if current not in LIST_KEYS or not line.lstrip().startswith("-"):
                errors.append(f"front matter line {number}: unsupported indentation")
            else:
                metadata[current].append(line.lstrip()[1:].strip().strip("'\""))
            continue
        if ":" not in line:
            errors.append(f"front matter line {number}: expected key: value")
            continue
        key, raw = (part.strip() for part in line.split(":", 1))
        if not re.fullmatch(r"[a-z][a-z0-9_]*", key):
            errors.append(f"front matter line {number}: invalid key {key}")
            current = None
            continue
        value = [] if key in LIST_KEYS and not raw.strip() else parse_value(raw)
        metadata[key] = value
        current = key if key in LIST_KEYS and isinstance(value, list) else None
    return metadata, text[end + 4 :].lstrip("\n"), "; ".join(errors) if errors else None


def parse_legacy(text, expected_id):
    """Read the project's common bullet-metadata ADR format without rewriting it."""
    metadata = {"id": expected_id}
    heading = re.search(r"^#\s+" + re.escape(expected_id) + r":\s*(.+?)\s*$", text, re.MULTILINE)
    if heading:
        metadata["title"] = heading.group(1).strip()
    # Legacy metadata is conventionally a bullet list immediately before the first
    # H2. Restricting the scan prevents prose later in the ADR from being parsed.
    prefix = text[: re.search(r"^##\s+", text, re.MULTILINE).start()] if re.search(r"^##\s+", text, re.MULTILINE) else text
    patterns = {
        "status": r"^-\s*Status:\s*`?([^`\n]+?)`?\s*$",
        "date": r"^-\s*Date:\s*`?([^`\n]+?)`?\s*$",
        "owners": r"^-\s*Owners?:\s*`?([^`\n]+?)`?\s*$",
        "related_tasks": r"^-\s*Related task:\s*`?([^`\n]+?)`?\s*$",
        "supersedes": r"^-\s*Supersedes:\s*`?([^`\n]+?)`?\s*$",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, prefix, re.MULTILINE | re.IGNORECASE)
        if not match:
            continue
        value = match.group(1).strip()
        metadata[key] = [] if value.lower() in ("none", "n/a", "-", "") else ([value] if key in LIST_KEYS else value)
    relationships = re.search(r"^##\s+Relationships\s*$([\s\S]*?)(?=^##\s+|\Z)", text, re.MULTILINE)
    if relationships:
        relation_patterns = {
            "superseded_by": r"^-\s*Superseded by:\s*`?([^`\n]+?)`?\s*$",
            "supersedes": r"^-\s*Supersedes:\s*`?([^`\n]+?)`?\s*$",
            "related_specs": r"^-\s*Related Specs and Code:\s*(.+?)\s*$",
        }
        for key, pattern in relation_patterns.items():
            match = re.search(pattern, relationships.group(1), re.MULTILINE | re.IGNORECASE)
            if match:
                value = match.group(1).strip()
                metadata[key] = [] if value.lower() in ("none", "n/a", "-", "") else [value]
    return metadata


def load(path):
    if not path.is_file():
        raise AdrError(f"ADR file does not exist: {path}")
    match = FILE_RE.match(path.name)
    if not match:
        raise AdrError(f"ADR filename must match NNNN-lowercase-slug.md: {path.name}")
    text = path.read_text(encoding="utf-8")
    metadata, body, parse_error = parse_frontmatter(text)
    record_format = "frontmatter"
    if parse_error == "missing front matter opening marker":
        metadata = parse_legacy(text, f"ADR-{match.group('num')}")
        body = text
        parse_error = None
        record_format = "legacy"
    return {
        "path": path,
        "file_id": f"ADR-{match.group('num')}",
        "metadata": metadata,
        "body": body,
        "parse_error": parse_error,
        "format": record_format,
    }


def get_files(directory):
    if not directory.exists():
        raise AdrError(f"ADR directory does not exist: {directory}")
    if not directory.is_dir():
        raise AdrError(f"ADR directory is not a directory: {directory}")
    return sorted(
        (p for p in directory.iterdir() if p.is_file() and FILE_RE.match(p.name)),
        key=lambda p: p.name,
    )


def get_records(directory):
    result, by_id = [], {}
    for path in get_files(directory):
        try:
            record = load(path)
        except AdrError as exc:
            record = {"path": path, "file_id": "", "metadata": {}, "body": "", "parse_error": str(exc)}
        result.append(record)
        if record["file_id"] and record["file_id"] not in by_id:
            by_id[record["file_id"]] = record
        elif record["file_id"]:
            record.setdefault("extra_errors", []).append("duplicate ADR ID")
    for path in sorted(directory.iterdir(), key=lambda candidate: candidate.name):
        if not path.is_file() or path.suffix != ".md" or FILE_RE.match(path.name):
            continue
        if re.match(r"^(?:[0-9]{4}|ADR-[0-9]{4})", path.name, re.IGNORECASE):
            result.append({
                "path": path,
                "file_id": "",
                "metadata": {},
                "body": "",
                "parse_error": f"ADR filename must match NNNN-lowercase-slug.md: {path.name}",
            })
    return result, by_id


def list_value(record, key):
    value = record["metadata"].get(key, [])
    if value in ("", None):
        return []
    return [str(x) for x in value] if isinstance(value, list) else [str(value)]


def repository_root(directory):
    for candidate in (directory, *directory.parents):
        if (candidate / ".git").exists() or (candidate / ".trellis").exists():
            return candidate
    return directory


def has_section(body, heading):
    return bool(re.search(r"^## " + re.escape(heading) + r"\s*$", body, re.MULTILINE))


def has_content(body, heading):
    match = re.search(r"^## " + re.escape(heading) + r"\s*$", body, re.MULTILINE)
    if not match:
        return False
    remainder = body[match.end():]
    next_heading = re.search(r"^## \S.*$", remainder, re.MULTILINE)
    content = remainder[: next_heading.start()] if next_heading else remainder
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    content = re.sub(r"<[^>]+>", "", content)
    content = re.sub(r"[\s_*#<>\-\.]", "", content)
    return bool(content.strip())


def has_any_section(body, headings):
    return any(has_section(body, heading) for heading in headings)


def has_any_content(body, headings):
    return any(has_content(body, heading) for heading in headings)


def section_text(body, heading):
    match = re.search(r"^## " + re.escape(heading) + r"\s*$", body, re.MULTILINE)
    if not match:
        return ""
    remainder = body[match.end():]
    next_heading = re.search(r"^## \S.*$", remainder, re.MULTILINE)
    return remainder[: next_heading.start()] if next_heading else remainder


def body_relation(body, label):
    relationships = section_text(body, "Related Artifacts") or section_text(body, "Relationships")
    match = re.search(r"^-\s*" + re.escape(label) + r":\s*`?([^`\n]+?)`?\s*$",
                      relationships, re.MULTILINE | re.IGNORECASE)
    if not match:
        return None
    value = match.group(1).strip()
    return [] if value.lower() in ("none", "n/a", "-", "") else [value]


def set_body_relation(body, label, values):
    relationships = re.search(
        r"(^## (?:Related Artifacts|Relationships)\s*$)([\s\S]*?)(?=^## \S|\Z)",
        body,
        re.MULTILINE,
    )
    if not relationships:
        raise AdrError(f"cannot update body relationship without a Relationships section: {label}")
    value = values[0] if values else "none"
    section = relationships.group(2)
    pattern = r"(^-\s*" + re.escape(label) + r":\s*).*$"
    if re.search(pattern, section, re.MULTILINE | re.IGNORECASE):
        section = re.sub(pattern, lambda match: match.group(1) + value, section,
                         count=1, flags=re.MULTILINE | re.IGNORECASE)
    else:
        section = section.rstrip() + f"\n- {label}: {value}\n"
    return body[: relationships.start(2)] + section + body[relationships.end(2):]


def validate_record(record, ids=None, root=None, by_id=None):
    metadata, body = record["metadata"], record["body"]
    errors = list(record.get("extra_errors", []))
    warnings = []
    if record.get("parse_error"):
        errors.append(record["parse_error"])
    expected_id = record["file_id"]
    if metadata.get("id") != expected_id:
        errors.append(f"id must be {expected_id}")
    if not metadata.get("title"):
        errors.append("missing required metadata: title")
    if metadata.get("status") not in STATUSES:
        errors.append("status must be one of: " + ", ".join(STATUSES))
    try:
        datetime.date.fromisoformat(str(metadata.get("date", "")))
    except ValueError:
        errors.append("date must be a valid YYYY-MM-DD value")
    if not list_value(record, "owners"):
        errors.append("owners must contain at least one person or team")
    if expected_id and not re.search(r"^# " + re.escape(expected_id) + r":\s+\S+", body, re.MULTILINE):
        errors.append(f"missing heading '# {expected_id}: title'")
    for label, headings in REQUIRED_GROUPS:
        if not has_any_section(body, headings):
            errors.append(f"missing required section: {label}")
        elif metadata.get("status") == "accepted" and not has_any_content(body, headings):
            errors.append(f"accepted ADR has an empty section: {label}")
    if metadata.get("status") == "accepted" and "<!--" in body:
        errors.append("accepted ADR contains unresolved placeholder comments")
    if metadata.get("status") == "accepted" and not has_content(body, "Review Notes"):
        errors.append("accepted ADR must record a review outcome in Review Notes")
    for key, label in (("supersedes", "Supersedes"), ("superseded_by", "Superseded by")):
        body_values = body_relation(body, label)
        if body_values is not None and body_values != list_value(record, key):
            errors.append(f"{label} in the body does not match front matter")
    if ids is not None:
        for key in ("supersedes", "superseded_by"):
            for related in list_value(record, key):
                if not ID_RE.fullmatch(related):
                    errors.append(f"{key} contains invalid ADR ID: {related}")
                elif related not in ids:
                    errors.append(f"{key} references missing ADR: {related}")
                elif by_id is not None:
                    target = by_id.get(related)
                    reciprocal_key = "superseded_by" if key == "supersedes" else "supersedes"
                    if target is not None and record["file_id"] not in list_value(target, reciprocal_key):
                        errors.append(
                            f"{key} relationship to {related} is not reciprocal via {reciprocal_key}"
                        )
    if root is not None:
        for key in ("related_tasks", "related_design", "related_specs"):
            for raw in list_value(record, key):
                path = Path(raw)
                if not path.is_absolute():
                    path = root / path
                if not path.exists():
                    warnings.append(f"{key} path does not exist: {raw}")
    record["errors"], record["warnings"] = errors, warnings
    return record


def fail_if_issues(records, strict=False):
    had = False
    for record in records:
        if record.get("errors"):
            had = True
            print(f"ERROR {record['path']}")
            for error in record["errors"]:
                print(f"  - {error}")
        if record.get("warnings"):
            had = True
            print(f"WARN  {record['path']}")
            for warning in record["warnings"]:
                print(f"  - {warning}")
    if not had:
        print("No ADR issues found.")
    return 1 if any(record.get("errors") or (strict and record.get("warnings")) for record in records) else 0


def slugify(value):
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise AdrError("slug must contain at least one ASCII letter or digit")
    return slug


def quote(value):
    return value if re.fullmatch(r"[A-Za-z0-9._/:-]+", value) else json.dumps(value, ensure_ascii=False)


def write_frontmatter(metadata):
    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                lines.extend(f"  - {quote(str(item))}" for item in value)
        else:
            lines.append(f"{key}: {quote(str(value))}")
    lines.append("---")
    return "\n".join(lines)


def document_body(adr_id, title, metadata):
    def relation(label, key):
        values = metadata.get(key, [])
        value = values[0] if isinstance(values, list) and values else "none"
        return f"- {label}: {value}"

    return f"""# {adr_id}: {title}

## Context

<!-- Describe the problem, scope, constraints, and evidence. -->

## Decision Drivers

- <!-- State the measurable or observable driver. -->

## Options Considered

| Option | Advantages | Costs and risks | Why not / status |
| --- | --- | --- | --- |
| <!-- Option A --> | <!-- ... --> | <!-- ... --> | <!-- ... --> |
| <!-- Option B --> | <!-- ... --> | <!-- ... --> | <!-- ... --> |

## Decision

<!-- State exactly what the project will do and where it applies. -->

## Consequences

### Positive

- <!-- ... -->

### Negative and risks

- <!-- ... -->

### Migration, rollback, and operations

- <!-- ... -->

## Non-Functional Constraints

- <!-- Performance, reliability, security, privacy, compatibility, cost, or operability constraint. -->

## Implementation Notes

- <!-- Boundaries and interfaces for the current task. -->

## Revisit Triggers

- <!-- Observable condition that should cause a new review or superseding ADR. -->

## Evidence

- <!-- Code, test, benchmark, issue, research note, or other source. -->

## Related Artifacts

{relation("Task", "related_tasks")}
{relation("Design", "related_design")}
{relation("Spec", "related_specs")}
{relation("Supersedes", "supersedes")}
{relation("Superseded by", "superseded_by")}

## Review Notes

- <!-- Date, reviewer, outcome, and unresolved questions. -->
"""


def cmd_next(args):
    directory = Path(args.dir).expanduser().resolve()
    numbers = [int(match.group("num")) for path in get_files(directory)
               if (match := FILE_RE.match(path.name))]
    number = max(numbers, default=0) + 1
    if number > 9999:
        raise AdrError("ADR number space exhausted at 9999")
    print(f"ADR-{number:04d}")
    return 0


def cmd_create(args):
    directory = Path(args.dir).expanduser().resolve()
    directory.mkdir(parents=True, exist_ok=True)
    numbers = [int(match.group("num")) for path in get_files(directory)
               if (match := FILE_RE.match(path.name))]
    number = max(numbers, default=0) + 1 if args.number is None else args.number
    if not 1 <= number <= 9999:
        raise AdrError("number must be between 1 and 9999")
    if number in numbers:
        raise AdrError(f"ADR number {number:04d} is already in use")
    slug = slugify(args.slug or args.title)
    path = directory / f"{number:04d}-{slug}.md"
    if path.exists():
        raise AdrError(f"refusing to overwrite existing ADR: {path}")
    if args.status != "proposed" and not args.allow_non_proposed:
        raise AdrError("new ADRs must start as proposed; use --allow-non-proposed only for an intentional import")
    date_value = args.date or datetime.date.today().isoformat()
    try:
        datetime.date.fromisoformat(date_value)
    except ValueError as exc:
        raise AdrError(f"invalid date: {date_value}") from exc
    metadata = {
        "id": f"ADR-{number:04d}",
        "title": args.title,
        "status": args.status,
        "date": date_value,
        "owners": args.owner,
        "supersedes": args.supersedes,
        "superseded_by": [],
        "related_tasks": args.related_task,
        "related_design": args.related_design,
        "related_specs": args.related_spec,
    }
    with path.open("x", encoding="utf-8") as handle:
        handle.write(write_frontmatter(metadata) + "\n\n" + document_body(metadata["id"], args.title, metadata))
    print(f"Created {metadata['id']}: {path}")
    return 0


def summary(record):
    metadata = record["metadata"]
    return {
        "id": metadata.get("id", record["file_id"]),
        "title": metadata.get("title", ""),
        "status": metadata.get("status", ""),
        "date": metadata.get("date", ""),
        "path": str(record["path"]),
        "errors": record.get("errors", []),
        "warnings": record.get("warnings", []),
    }


def cmd_list(args):
    directory = Path(args.dir).expanduser().resolve()
    items, indexed = get_records(directory)
    for item in items:
        validate_record(item, set(indexed), repository_root(directory), indexed)
    selected = [item for item in items if not args.status or item["metadata"].get("status") == args.status]
    if args.json:
        print(json.dumps([summary(item) for item in selected], ensure_ascii=False, indent=2))
    elif not selected:
        print(f"No ADRs found in {directory}")
    else:
        for item in selected:
            metadata = item["metadata"]
            issue = f" [errors: {len(item['errors'])}]" if item["errors"] else ""
            print(f"{metadata.get('id', item['file_id']):<9} {metadata.get('status', '<missing>'):<11} "
                  f"{metadata.get('title', '<missing>')}  {item['path'].name}{issue}")
    return 1 if args.strict and any(item["errors"] or item["warnings"] for item in selected) else 0


def cmd_validate(args):
    if args.path:
        items = [load(Path(raw).expanduser().resolve()) for raw in args.path]
        directory = items[0]["path"].parent if items else None
        siblings, indexed = get_records(directory) if directory is not None else ([], {})
        ids = set(indexed)
        root = repository_root(directory) if directory is not None else None
    else:
        directory = Path(args.dir).expanduser().resolve()
        items, indexed = get_records(directory)
        ids, root = set(indexed), repository_root(directory)
    for item in items:
        validate_record(item, ids, root, indexed)
    return fail_if_issues(items, strict=args.strict)


def cmd_review(args):
    results = []
    for raw in args.path:
        item = load(Path(raw).expanduser().resolve())
        validate_record(item, None, repository_root(item["path"].parent))
        gaps = [f"complete section: {label}" for label, headings in REQUIRED_GROUPS
                if not has_any_content(item["body"], headings)]
        review_notes = section_text(item["body"], "Review Notes")
        if not review_notes or not has_content(item["body"], "Review Notes"):
            gaps.append("record an explicit review outcome in Review Notes")
        body_lower = item["body"].lower()
        project_level = bool(re.search(r"\b(project-level|project wide|项目级|项目范围)\b", body_lower))
        design_declared_none = bool(re.search(r"(?:design|设计)\s*:\s*(?:`?none|无|n/?a|没有对应)", body_lower))
        spec_declared_none = bool(re.search(r"(?:spec|规范)\s*:\s*(?:`?none|无|n/?a|没有对应)", body_lower))
        if not list_value(item, "related_design") and not (project_level or design_declared_none):
            gaps.append("link the task design.md or explain why none applies")
        if not list_value(item, "related_specs") and not (project_level or spec_declared_none):
            gaps.append("link relevant Trellis specs or explain why none applies")
        results.append((item, gaps))
    if args.json:
        print(json.dumps([{"adr": summary(item), "review_gaps": gaps} for item, gaps in results],
                         ensure_ascii=False, indent=2))
    else:
        for item, gaps in results:
            print(f"{item['metadata'].get('id', item['file_id'])}: {item['metadata'].get('title', '<missing title>')}")
            for error in item["errors"]:
                print(f"  ERROR: {error}")
            for gap in gaps:
                print(f"  REVIEW: {gap}")
            if not gaps and not item["errors"]:
                print("  REVIEW: no gaps detected")
    return 1 if any(item["errors"] or gaps for item, gaps in results) else 0


def update_metadata(path, updates):
    text = path.read_text(encoding="utf-8")
    metadata, body, parse_error = parse_frontmatter(text)
    if parse_error == "missing front matter opening marker":
        raise AdrError(
            f"{path} uses legacy Markdown metadata; migrate it to the bundled front matter format before changing status or links"
        )
    if parse_error:
        raise AdrError(f"cannot update malformed front matter: {parse_error}")
    metadata.update(updates)
    if "supersedes" in updates:
        body = set_body_relation(body, "Supersedes", updates["supersedes"])
    if "superseded_by" in updates:
        body = set_body_relation(body, "Superseded by", updates["superseded_by"])
    atomic_write(path, write_frontmatter(metadata) + "\n\n" + body)


def atomic_write(path, content):
    """Replace one file without exposing a partially written document."""
    mode = path.stat().st_mode & 0o777
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def find_id(directory, wanted):
    if not ID_RE.fullmatch(wanted):
        raise AdrError(f"invalid ADR ID: {wanted}; expected ADR-NNNN")
    items, indexed = get_records(directory)
    if wanted not in indexed:
        raise AdrError(f"ADR not found in {directory}: {wanted}")
    return indexed[wanted]


def cmd_status(args):
    path = Path(args.path).expanduser().resolve()
    item = load(path)
    old, new = item["metadata"].get("status"), args.to
    if old == new:
        print(f"{item['file_id']} is already {new}")
        return 0
    if new not in TRANSITIONS.get(old, set()):
        raise AdrError(f"invalid status transition: {old or '<missing>'} -> {new}")
    if new == "accepted":
        item["metadata"]["status"] = "accepted"
        _, indexed = get_records(path.parent)
        validate_record(item, set(indexed), repository_root(path.parent), indexed)
        if item["errors"]:
            raise AdrError("cannot accept an incomplete ADR: " + "; ".join(item["errors"]))
    update_metadata(path, {"status": new})
    print(f"Updated {item['file_id']}: {old} -> {new}")
    return 0


def cmd_supersede(args):
    directory = Path(args.dir).expanduser().resolve()
    old, new = find_id(directory, args.old), find_id(directory, args.new)
    if old["file_id"] == new["file_id"]:
        raise AdrError("an ADR cannot supersede itself")
    if old["metadata"].get("status") != "accepted":
        raise AdrError("old ADR must be accepted")
    if new["metadata"].get("status") != "accepted":
        raise AdrError("new ADR must be accepted")
    old_links = list_value(old, "superseded_by")
    new_links = list_value(new, "supersedes")
    if old_links and args.new not in old_links:
        raise AdrError("old ADR already points to another replacement")
    if new_links and args.old not in new_links:
        raise AdrError("new ADR already supersedes another ADR")
    old_text = old["path"].read_text(encoding="utf-8")
    new_text = new["path"].read_text(encoding="utf-8")
    try:
        update_metadata(new["path"], {"supersedes": [args.old]})
        update_metadata(old["path"], {"status": "superseded", "superseded_by": [args.new]})
    except Exception as write_error:
        # The two replacements are individually atomic, but no filesystem API
        # can commit two independent Markdown files as one transaction. Restore
        # the first file if the second write fails, then surface the error.
        rollback_errors = []
        for path, content in ((new["path"], new_text), (old["path"], old_text)):
            try:
                atomic_write(path, content)
            except Exception as rollback_error:
                rollback_errors.append(f"{path}: {rollback_error}")
        if rollback_errors:
            raise AdrError(
                f"supersession failed: {write_error}; rollback also failed: "
                + "; ".join(rollback_errors)
            ) from write_error
        raise
    print(f"Superseded {args.old} with {args.new}")
    return 0


def parser():
    root = argparse.ArgumentParser(description="Manage Architecture Decision Records")
    sub = root.add_subparsers(dest="command", required=True)

    command = sub.add_parser("next", help="print the next available ADR ID")
    command.add_argument("--dir", default="docs/adr")
    command.set_defaults(run=cmd_next)

    command = sub.add_parser("create", help="create a proposed ADR")
    command.add_argument("--dir", default="docs/adr")
    command.add_argument("--title", required=True)
    command.add_argument("--slug")
    command.add_argument("--number", type=int)
    command.add_argument("--date")
    command.add_argument("--owner", action="append", default=[])
    command.add_argument("--related-task", action="append", default=[])
    command.add_argument("--related-design", action="append", default=[])
    command.add_argument("--related-spec", action="append", default=[])
    command.add_argument("--supersedes", action="append", default=[])
    command.add_argument("--status", choices=STATUSES, default="proposed")
    command.add_argument("--allow-non-proposed", action="store_true")
    command.set_defaults(run=cmd_create)

    command = sub.add_parser("list", help="list ADRs")
    command.add_argument("--dir", default="docs/adr")
    command.add_argument("--status", choices=STATUSES)
    command.add_argument("--json", action="store_true")
    command.add_argument("--strict", action="store_true")
    command.set_defaults(run=cmd_list)

    command = sub.add_parser("validate", help="validate one file or a directory")
    command.add_argument("path", nargs="*")
    command.add_argument("--dir", default="docs/adr")
    command.add_argument("--strict", action="store_true", help="treat missing related paths as errors")
    command.set_defaults(run=cmd_validate)

    command = sub.add_parser("review", help="report review gaps without editing")
    command.add_argument("path", nargs="+")
    command.add_argument("--json", action="store_true")
    command.set_defaults(run=cmd_review)

    command = sub.add_parser("status", help="apply a validated status transition")
    command.add_argument("path")
    command.add_argument("--to", required=True, choices=STATUSES)
    command.set_defaults(run=cmd_status)

    command = sub.add_parser("supersede", help="link two accepted ADRs")
    command.add_argument("--dir", default="docs/adr")
    command.add_argument("--old", required=True)
    command.add_argument("--new", required=True)
    command.set_defaults(run=cmd_supersede)
    return root


def main(argv=None):
    try:
        args = parser().parse_args(argv)
        return int(args.run(args))
    except (AdrError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
