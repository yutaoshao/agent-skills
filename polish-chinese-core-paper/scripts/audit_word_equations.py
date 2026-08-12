#!/usr/bin/env python3
"""Audit Word equation objects and compare them across DOCX revisions."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import posixpath
import re
import sys
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


NS = {
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "o": "urn:schemas-microsoft-com:office:office",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
PACKAGE_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"

W_P = f"{{{NS['w']}}}p"
W_TR = f"{{{NS['w']}}}tr"
W_TC = f"{{{NS['w']}}}tc"
W_T = f"{{{NS['w']}}}t"
W_TAB = f"{{{NS['w']}}}tab"
W_DRAWING = f"{{{NS['w']}}}drawing"
W_PICT = f"{{{NS['w']}}}pict"
W_OBJECT = f"{{{NS['w']}}}object"
W_INSTR_TEXT = f"{{{NS['w']}}}instrText"
W_FLD_SIMPLE = f"{{{NS['w']}}}fldSimple"
W_BOOKMARK_START = f"{{{NS['w']}}}bookmarkStart"
W_NAME = f"{{{NS['w']}}}name"
W_INSTR = f"{{{NS['w']}}}instr"
R_ID = f"{{{NS['r']}}}id"
R_EMBED = f"{{{NS['r']}}}embed"
R_LINK = f"{{{NS['r']}}}link"
M_O_MATH = f"{{{NS['m']}}}oMath"
M_O_MATH_PARA = f"{{{NS['m']}}}oMathPara"
M_T = f"{{{NS['m']}}}t"
O_OLE_OBJECT = f"{{{NS['o']}}}OLEObject"
RELATIONSHIP = f"{{{PACKAGE_REL_NS}}}Relationship"
MC_ALTERNATE_CONTENT = f"{{{MC_NS}}}AlternateContent"
MC_CHOICE = f"{{{MC_NS}}}Choice"
MC_FALLBACK = f"{{{MC_NS}}}Fallback"
SUPPORTED_MCE_NAMESPACE_URIS = {
    NS["m"],
    NS["o"],
    NS["w"],
    "http://schemas.openxmlformats.org/drawingml/2006/main",
    "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas",
    "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing",
    "http://schemas.microsoft.com/office/word/2010/wordprocessingGroup",
    "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
}

WORD_STORY_RE = re.compile(
    r"^word/(?:document|footnotes|endnotes|comments|header\d+|footer\d+)\.xml$"
)
EQUATION_NUMBER_RE = re.compile(
    r"[（(]\s*((?:\d+(?:[.-]\d+)*[A-Za-z]?|[A-Za-z](?:[.-]\d+)+))"
    r"\s*[）)]\s*[，,。.;；:：]?\s*$"
)
VISIBLE_REFERENCE_RE = re.compile(
    r"式\s*[（(]\s*((?:\d+(?:[.-]\d+)*[A-Za-z]?|[A-Za-z](?:[.-]\d+)+))"
    r"\s*[）)]"
)
FIELD_RE = re.compile(
    r"\b(SEQ|REF)\s+(?:\"([^\"]+)\"|([^\s\\]+))", re.IGNORECASE
)
RAW_TEX_RE = re.compile(
    r"\\[A-Za-z]{2,}\b|\\[()[\]{}]|\${2,}|(?<!\\)\$[^$\r\n]+\$"
)

SKIP_SEMANTIC_TAGS = {
    f"{{{NS['w']}}}rPr",
    f"{{{NS['m']}}}ctrlPr",
}


@dataclass(frozen=True)
class Issue:
    severity: str
    code: str
    message: str
    part: str | None = None
    paragraph: int | None = None


@dataclass(frozen=True)
class EquationRecord:
    part: str
    paragraph: int
    equation: int
    role: str
    number: str | None
    math_text: str
    semantic_hash: str
    xml_hash: str
    bookmarks: tuple[str, ...]


@dataclass(frozen=True)
class NumberRecord:
    part: str
    paragraph: int
    number: str


@dataclass(frozen=True)
class FieldRecord:
    part: str
    paragraph: int
    field_type: str
    target: str
    instruction: str


@dataclass(frozen=True)
class ReferenceRecord:
    part: str
    paragraph: int
    number: str


@dataclass(frozen=True)
class EmbeddedRelationshipRecord:
    part: str
    paragraph: int
    relationship_id: str
    relationship_type: str
    target: str
    resolved_part: str | None
    target_hash: str | None


@dataclass(frozen=True)
class DrawingEquationCandidate:
    part: str
    paragraph: int
    number: str
    xml_hash: str
    target_signatures: tuple[str, ...]


@dataclass
class AuditResult:
    path: str
    native_math_count: int
    displayed_math_count: int
    inline_math_count: int
    embedded_object_count: int
    embedding_part_count: int
    drawing_count: int
    equations: list[EquationRecord]
    numbers: list[NumberRecord]
    fields: list[FieldRecord]
    bookmarks: list[str]
    visible_references: list[ReferenceRecord]
    embedding_hashes: list[str]
    embedded_relationships: list[EmbeddedRelationshipRecord]
    drawing_equation_candidates: list[DrawingEquationCandidate]
    issues: list[Issue]

    def public_dict(self) -> dict[str, object]:
        return asdict(self)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def normalized_text(values: Iterable[str | None]) -> str:
    return "".join(value or "" for value in values)


def exact_hash(element: ET.Element) -> str:
    return hashlib.sha256(ET.tostring(element, encoding="utf-8")).hexdigest()


def semantic_tokens(element: ET.Element) -> Iterable[str]:
    name = local_name(element.tag)
    if element.tag in SKIP_SEMANTIC_TAGS:
        return

    attrs = ",".join(
        f"{local_name(key)}={value}" for key, value in sorted(element.attrib.items())
    )
    yield f"<{name}:{attrs}>"
    if element.text and element.text.strip():
        yield element.text.strip()
    for child in element:
        yield from semantic_tokens(child)
    yield f"</{name}>"


def semantic_hash(element: ET.Element) -> str:
    payload = "".join(semantic_tokens(element)).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def select_alternate_branch(
    alternate: ET.Element, namespace_by_prefix: dict[str, str]
) -> ET.Element | None:
    fallback = None
    for branch in alternate:
        if branch.tag == MC_FALLBACK:
            fallback = branch
            continue
        if branch.tag != MC_CHOICE:
            continue
        required_prefixes = branch.get("Requires", "").split()
        if required_prefixes and all(
            namespace_by_prefix.get(prefix) in SUPPORTED_MCE_NAMESPACE_URIS
            for prefix in required_prefixes
        ):
            return branch
    return fallback


def owned_elements(
    paragraph: ET.Element, namespace_by_prefix: dict[str, str] | None = None
) -> Iterable[ET.Element]:
    """Yield paragraph descendants without descending into nested text-box paragraphs."""

    namespace_by_prefix = namespace_by_prefix or {}
    stack = list(reversed(list(paragraph)))
    while stack:
        node = stack.pop()
        if node.tag == W_P:
            continue
        yield node
        if node.tag == MC_ALTERNATE_CONTENT:
            selected = select_alternate_branch(node, namespace_by_prefix)
            if selected is not None:
                stack.extend(reversed(list(selected)))
            continue
        stack.extend(reversed(list(node)))


def paragraph_field_instructions(elements: Iterable[ET.Element]) -> list[str]:
    nodes = list(elements)
    complex_fragments = [
        text.strip()
        for text in (node.text for node in nodes if node.tag == W_INSTR_TEXT)
        if text and text.strip()
    ]
    instructions = [" ".join(complex_fragments)] if complex_fragments else []
    for node in nodes:
        if node.tag != W_FLD_SIMPLE:
            continue
        value = node.get(W_INSTR)
        if value and value.strip():
            instructions.append(value.strip())
    return instructions


def iter_field_records(
    instructions: Iterable[str], part: str, paragraph: int
) -> Iterable[FieldRecord]:
    for instruction in instructions:
        for match in FIELD_RE.finditer(instruction):
            yield FieldRecord(
                part=part,
                paragraph=paragraph,
                field_type=match.group(1).upper(),
                target=match.group(2) or match.group(3),
                instruction=" ".join(instruction.split()),
            )


def story_parts(names: Iterable[str]) -> list[str]:
    parts = [name for name in names if WORD_STORY_RE.fullmatch(name)]
    return sorted(parts, key=lambda name: (name != "word/document.xml", name))


def read_member(archive: zipfile.ZipFile, name: str) -> bytes:
    try:
        return archive.read(name)
    except (KeyError, OSError, RuntimeError, zipfile.BadZipFile) as exc:
        raise ValueError(f"cannot read DOCX member {name}: {exc}") from exc


def relationships_for_part(
    archive: zipfile.ZipFile, source_part: str, package_names: set[str]
) -> dict[str, tuple[str, str, str | None]]:
    directory = posixpath.dirname(source_part)
    rels_part = posixpath.join(
        directory, "_rels", f"{posixpath.basename(source_part)}.rels"
    )
    if rels_part not in package_names:
        return {}

    try:
        root = ET.fromstring(read_member(archive, rels_part))
    except ET.ParseError as exc:
        raise ValueError(f"invalid XML in {rels_part}: {exc}") from exc

    relationships: dict[str, tuple[str, str, str | None]] = {}
    for node in root.iter(RELATIONSHIP):
        relationship_id = node.get("Id")
        relationship_type = node.get("Type")
        target = node.get("Target")
        if not relationship_id or not relationship_type or not target:
            continue
        resolved = None
        if node.get("TargetMode") != "External":
            resolved = posixpath.normpath(posixpath.join(directory, target))
        relationships[relationship_id] = (relationship_type, target, resolved)
    return relationships


def related_target_signatures(
    element: ET.Element,
    relationships: dict[str, tuple[str, str, str | None]],
    package_names: set[str],
    archive: zipfile.ZipFile,
) -> tuple[tuple[str, ...], list[str]]:
    relationship_ids = sorted(
        {
            value
            for node in element.iter()
            for key, value in node.attrib.items()
            if key in {R_ID, R_EMBED, R_LINK}
        }
    )
    signatures: list[str] = []
    problems: list[str] = []
    for relationship_id in relationship_ids:
        relationship = relationships.get(relationship_id)
        if relationship is None:
            signatures.append(f"{relationship_id}:missing-relationship")
            problems.append(f"relationship {relationship_id!r} is missing")
            continue
        relationship_type, target, resolved_part = relationship
        if resolved_part is None:
            signatures.append(
                f"{relationship_id}:{relationship_type}:{target}:external"
            )
            problems.append(f"relationship {relationship_id!r} is external")
            continue
        if resolved_part not in package_names:
            signatures.append(
                f"{relationship_id}:{relationship_type}:{target}:missing-target"
            )
            problems.append(
                f"relationship {relationship_id!r} targets missing part {resolved_part!r}"
            )
            continue
        target_hash = hashlib.sha256(read_member(archive, resolved_part)).hexdigest()
        signatures.append(
            f"{relationship_id}:{relationship_type}:{target}:{target_hash}"
        )
    return tuple(signatures), problems


def classify_role(
    equation: ET.Element,
    math_para_ids: set[int],
    has_number: bool,
    tab_count: int,
    word_text: str,
) -> str:
    if id(equation) in math_para_ids:
        return "display"
    if has_number or (tab_count > 0 and len(word_text.strip()) <= 20):
        return "display-candidate"
    return "inline"


def table_row_number_links(
    root: ET.Element, namespace_by_prefix: dict[str, str]
) -> tuple[dict[int, str], set[int], dict[int, tuple[str, ...]]]:
    links: dict[int, str] = {}
    number_owners: set[int] = set()
    bookmark_links: dict[int, tuple[str, ...]] = {}
    allowed_formula_text = {"", ",", "，", ".", "。", ";", "；", ":", "："}

    for row in root.iter(W_TR):
        cells = [child for child in row if child.tag == W_TC]
        formula_cells: list[tuple[int, list[ET.Element]]] = []
        number_cells: list[tuple[int, str, tuple[str, ...]]] = []
        for cell_index, cell in enumerate(cells):
            formula_paragraphs: list[ET.Element] = []
            cell_text_parts: list[str] = []
            for paragraph in cell.iter(W_P):
                elements = list(owned_elements(paragraph, namespace_by_prefix))
                if any(
                    node.tag in {M_O_MATH, W_OBJECT, O_OLE_OBJECT}
                    for node in elements
                ):
                    formula_paragraphs.append(paragraph)
                cell_text_parts.append(
                    normalized_text(node.text for node in elements if node.tag == W_T)
                )
            cell_text = "".join(cell_text_parts).strip()
            if formula_paragraphs and cell_text in allowed_formula_text:
                formula_cells.append((cell_index, formula_paragraphs))
            elif not formula_paragraphs:
                number_match = EQUATION_NUMBER_RE.fullmatch(cell_text)
                if number_match:
                    cell_bookmarks = tuple(
                        name
                        for paragraph in cell.iter(W_P)
                        for node in owned_elements(paragraph, namespace_by_prefix)
                        if node.tag == W_BOOKMARK_START
                        for name in [node.get(W_NAME)]
                        if name
                    )
                    number_cells.append(
                        (cell_index, number_match.group(1), cell_bookmarks)
                    )

        if len(formula_cells) == 1 and len(number_cells) == 1:
            formula_cell_index, formula_paragraphs = formula_cells[0]
            number_cell_index, number, number_bookmarks = number_cells[0]
            if abs(formula_cell_index - number_cell_index) != 1:
                continue
            for paragraph in formula_paragraphs:
                links[id(paragraph)] = number
                bookmark_links[id(paragraph)] = number_bookmarks
            number_owners.add(id(formula_paragraphs[0]))

    return links, number_owners, bookmark_links


def load_audit(path: Path) -> AuditResult:
    if path.suffix.lower() != ".docx":
        raise ValueError(f"expected a .docx file: {path}")
    if not path.is_file():
        raise ValueError(f"file not found: {path}")

    equations: list[EquationRecord] = []
    numbers: list[NumberRecord] = []
    fields: list[FieldRecord] = []
    bookmarks: list[str] = []
    visible_references: list[ReferenceRecord] = []
    embedding_hashes: list[str] = []
    embedded_relationships: list[EmbeddedRelationshipRecord] = []
    drawing_equation_candidates: list[DrawingEquationCandidate] = []
    issues: list[Issue] = []
    embedded_object_count = 0
    drawing_count = 0

    try:
        archive = zipfile.ZipFile(path)
    except (FileNotFoundError, OSError, zipfile.BadZipFile) as exc:
        raise ValueError(f"invalid DOCX package: {path}: {exc}") from exc

    with archive:
        names = archive.namelist()
        package_names = set(names)
        if "word/document.xml" not in names:
            raise ValueError(f"DOCX has no word/document.xml: {path}")

        embedding_names = sorted(
            name for name in names if name.startswith("word/embeddings/")
        )
        for name in embedding_names:
            digest = hashlib.sha256(read_member(archive, name)).hexdigest()
            embedding_hashes.append(f"{name}:{digest}")

        for part in story_parts(names):
            relationships = relationships_for_part(archive, part, package_names)
            xml_payload = read_member(archive, part)
            try:
                namespace_by_prefix = dict(
                    item
                    for _, item in ET.iterparse(
                        io.BytesIO(xml_payload), events=("start-ns",)
                    )
                )
                root = ET.fromstring(xml_payload)
            except ET.ParseError as exc:
                raise ValueError(f"invalid XML in {part}: {exc}") from exc

            (
                table_numbers,
                table_number_owners,
                table_number_bookmarks,
            ) = table_row_number_links(root, namespace_by_prefix)
            for paragraph_index, paragraph in enumerate(root.iter(W_P), start=1):
                owned = list(owned_elements(paragraph, namespace_by_prefix))
                word_text = normalized_text(
                    node.text for node in owned if node.tag == W_T
                )
                math_nodes = [node for node in owned if node.tag == M_O_MATH]
                math_paras = [node for node in owned if node.tag == M_O_MATH_PARA]
                math_para_ids = {
                    id(node)
                    for math_para in math_paras
                    for node in math_para.iter(M_O_MATH)
                }
                tab_count = sum(node.tag == W_TAB for node in owned)
                paragraph_bookmarks = tuple(
                    name
                    for name in (
                        node.get(W_NAME)
                        for node in owned
                        if node.tag == W_BOOKMARK_START
                    )
                    if name
                )
                equation_bookmarks = tuple(
                    dict.fromkeys(
                        [
                            *paragraph_bookmarks,
                            *table_number_bookmarks.get(id(paragraph), ()),
                        ]
                    )
                )
                bookmarks.extend(paragraph_bookmarks)

                instructions = paragraph_field_instructions(owned)
                fields.extend(iter_field_records(instructions, part, paragraph_index))

                for match in VISIBLE_REFERENCE_RE.finditer(word_text):
                    visible_references.append(
                        ReferenceRecord(part, paragraph_index, match.group(1))
                    )

                paragraph_objects = sum(node.tag == W_OBJECT for node in owned)
                ole_objects = sum(node.tag == O_OLE_OBJECT for node in owned)
                paragraph_embedded = max(paragraph_objects, ole_objects)
                paragraph_drawings = sum(
                    node.tag in {W_DRAWING, W_PICT} for node in owned
                )
                embedded_object_count += paragraph_embedded
                drawing_count += paragraph_drawings

                number_match = EQUATION_NUMBER_RE.search(word_text)
                number_prefix = (
                    word_text[: number_match.start()].strip() if number_match else ""
                )
                has_display_number_context = bool(
                    number_match
                    and (math_nodes or paragraph_embedded)
                    and (
                        math_para_ids
                        or tab_count
                        or number_prefix in {"", ",", "，", ".", "。", ";", "；"}
                    )
                )
                number = (
                    number_match.group(1)
                    if has_display_number_context
                    else table_numbers.get(id(paragraph))
                )
                if number and (
                    has_display_number_context or id(paragraph) in table_number_owners
                ):
                    numbers.append(NumberRecord(part, paragraph_index, number))

                drawing_number_context = bool(
                    paragraph_drawings
                    and number_match
                    and not math_nodes
                    and not paragraph_embedded
                    and (
                        tab_count
                        or number_prefix in {"", ",", "，", ".", "。", ";", "；"}
                    )
                )
                if drawing_number_context:
                    drawing_number = number_match.group(1)
                    numbers.append(
                        NumberRecord(part, paragraph_index, drawing_number)
                    )
                    for node in (
                        node for node in owned if node.tag in {W_DRAWING, W_PICT}
                    ):
                        target_signatures, target_problems = related_target_signatures(
                            node, relationships, package_names, archive
                        )
                        drawing_equation_candidates.append(
                            DrawingEquationCandidate(
                                part=part,
                                paragraph=paragraph_index,
                                number=drawing_number,
                                xml_hash=exact_hash(node),
                                target_signatures=target_signatures,
                            )
                        )
                        for problem in target_problems:
                            issues.append(
                                Issue(
                                    "error",
                                    "drawing-target-problem",
                                    f"Drawing equation candidate {problem}.",
                                    part,
                                    paragraph_index,
                                )
                            )

                if paragraph_embedded:
                    issues.append(
                        Issue(
                            "warning",
                            "embedded-object",
                            "Embedded OLE/MathType candidate requires compatible editing tooling.",
                            part,
                            paragraph_index,
                        )
                    )
                for ole_object in (
                    node for node in owned if node.tag == O_OLE_OBJECT
                ):
                    relationship_id = ole_object.get(R_ID)
                    if not relationship_id:
                        issues.append(
                            Issue(
                                "error",
                                "ole-missing-relationship-id",
                                "OLE object has no relationship id.",
                                part,
                                paragraph_index,
                            )
                        )
                        continue
                    relationship = relationships.get(relationship_id)
                    if relationship is None:
                        issues.append(
                            Issue(
                                "error",
                                "ole-missing-relationship",
                                f"OLE relationship {relationship_id!r} is missing.",
                                part,
                                paragraph_index,
                            )
                        )
                        continue
                    relationship_type, target, resolved_part = relationship
                    target_hash = None
                    if resolved_part is None:
                        issues.append(
                            Issue(
                                "warning",
                                "external-ole-link",
                                f"OLE relationship {relationship_id!r} targets an external object.",
                                part,
                                paragraph_index,
                            )
                        )
                    elif resolved_part not in package_names:
                        issues.append(
                            Issue(
                                "error",
                                "ole-missing-target",
                                f"OLE relationship {relationship_id!r} targets missing part {resolved_part!r}.",
                                part,
                                paragraph_index,
                            )
                        )
                    else:
                        target_hash = hashlib.sha256(
                            read_member(archive, resolved_part)
                        ).hexdigest()
                    embedded_relationships.append(
                        EmbeddedRelationshipRecord(
                            part=part,
                            paragraph=paragraph_index,
                            relationship_id=relationship_id,
                            relationship_type=relationship_type,
                            target=target,
                            resolved_part=resolved_part,
                            target_hash=target_hash,
                        )
                    )
                if drawing_number_context:
                    issues.append(
                        Issue(
                            "warning",
                            "drawing-equation-candidate",
                            "A numbered drawing-only paragraph may contain a non-editable equation image.",
                            part,
                            paragraph_index,
                        )
                    )
                if paragraph_drawings and math_nodes:
                    issues.append(
                        Issue(
                            "warning",
                            "mixed-math-and-drawing",
                            "An equation-bearing paragraph also contains a drawing; inspect it before editing.",
                            part,
                            paragraph_index,
                        )
                    )

                for equation_index, equation in enumerate(math_nodes, start=1):
                    math_text = normalized_text(node.text for node in equation.iter(M_T))
                    role = classify_role(
                        equation,
                        math_para_ids,
                        bool(number),
                        tab_count,
                        word_text,
                    )
                    equations.append(
                        EquationRecord(
                            part=part,
                            paragraph=paragraph_index,
                            equation=equation_index,
                            role=role,
                            number=number,
                            math_text=math_text,
                            semantic_hash=semantic_hash(equation),
                            xml_hash=exact_hash(equation),
                            bookmarks=equation_bookmarks,
                        )
                    )
                    if RAW_TEX_RE.search(math_text):
                        issues.append(
                            Issue(
                                "error",
                                "raw-tex-in-omml",
                                "Native math contains a visible TeX command or delimiter.",
                                part,
                                paragraph_index,
                            )
                        )

    number_counts = Counter(record.number for record in numbers)
    for number, count in sorted(number_counts.items()):
        if count > 1:
            issues.append(
                Issue(
                    "warning",
                    "duplicate-equation-number",
                    f"Visible equation number {number!r} appears {count} times.",
                )
            )

    bookmark_set = set(bookmarks)
    for field in fields:
        if field.field_type == "REF" and field.target not in bookmark_set:
            issues.append(
                Issue(
                    "warning",
                    "dangling-ref-field",
                    f"REF target {field.target!r} has no matching bookmark in scanned story parts.",
                    field.part,
                    field.paragraph,
                )
            )

    detected_numbers = set(number_counts)
    for reference in visible_references:
        if reference.number not in detected_numbers:
            issues.append(
                Issue(
                    "warning",
                    "unresolved-visible-equation-reference",
                    f"Visible reference to equation {reference.number!r} has no detected numbered equation.",
                    reference.part,
                    reference.paragraph,
                )
            )

    displayed_count = sum(
        1 for record in equations if record.role in {"display", "display-candidate"}
    )
    return AuditResult(
        path=str(path),
        native_math_count=len(equations),
        displayed_math_count=displayed_count,
        inline_math_count=len(equations) - displayed_count,
        embedded_object_count=embedded_object_count,
        embedding_part_count=len(embedding_hashes),
        drawing_count=drawing_count,
        equations=equations,
        numbers=numbers,
        fields=fields,
        bookmarks=sorted(set(bookmarks)),
        visible_references=visible_references,
        embedding_hashes=embedding_hashes,
        embedded_relationships=embedded_relationships,
        drawing_equation_candidates=drawing_equation_candidates,
        issues=issues,
    )


def add_requested_checks(
    audit: AuditResult,
    expect_native: int | None,
    expect_displayed: int | None,
    require_consecutive: bool,
) -> None:
    if expect_native is not None and audit.native_math_count != expect_native:
        audit.issues.append(
            Issue(
                "error",
                "native-math-count",
                f"Expected {expect_native} native equations, found {audit.native_math_count}.",
            )
        )

    if expect_displayed is not None and audit.displayed_math_count != expect_displayed:
        audit.issues.append(
            Issue(
                "error",
                "displayed-math-count",
                f"Expected {expect_displayed} displayed equations, found {audit.displayed_math_count}.",
            )
        )

    if not require_consecutive:
        return

    values = [record.number for record in audit.numbers]
    if not values:
        audit.issues.append(
            Issue(
                "error",
                "missing-equation-numbers",
                "Consecutive numbering was requested, but no visible equation numbers were detected.",
            )
        )
        return
    if any(not value.isdigit() for value in values):
        audit.issues.append(
            Issue(
                "error",
                "non-integer-numbering",
                "Consecutive integer numbering was requested, but a visible number is section-based or non-integer.",
            )
        )
        return

    integer_values = [int(value) for value in values]
    expected = list(range(1, len(integer_values) + 1))
    if integer_values != expected:
        audit.issues.append(
            Issue(
                "error",
                "non-consecutive-numbering",
                f"Expected visible equation numbers {expected}, found {integer_values}.",
            )
        )


def compare_audits(before: AuditResult, after: AuditResult) -> list[Issue]:
    issues: list[Issue] = []
    if before.native_math_count != after.native_math_count:
        issues.append(
            Issue(
                "error",
                "comparison-native-count",
                f"Native equation count changed from {before.native_math_count} to {after.native_math_count}.",
            )
        )

    before_semantic = [record.semantic_hash for record in before.equations]
    after_semantic = [record.semantic_hash for record in after.equations]
    if before_semantic != after_semantic:
        issues.append(
            Issue(
                "error",
                "comparison-semantic-math",
                "Ordered native-math semantic signatures changed.",
            )
        )

    before_xml = [record.xml_hash for record in before.equations]
    after_xml = [record.xml_hash for record in after.equations]
    if before_xml != after_xml and before_semantic == after_semantic:
        issues.append(
            Issue(
                "warning",
                "comparison-omml-formatting",
                "OMML XML changed although semantic signatures remained stable; review intentional formatting changes.",
            )
        )

    before_roles = [record.role for record in before.equations]
    after_roles = [record.role for record in after.equations]
    if before_roles != after_roles:
        issues.append(
            Issue(
                "warning",
                "comparison-equation-roles",
                f"Inline/display roles changed from {before_roles} to {after_roles}.",
            )
        )

    before_locations = [
        (record.part, record.paragraph) for record in before.equations
    ]
    after_locations = [(record.part, record.paragraph) for record in after.equations]
    if before_locations != after_locations:
        issues.append(
            Issue(
                "warning",
                "comparison-equation-locations",
                "Equation paragraph locations changed; verify every intentional move in context.",
            )
        )

    if before.embedded_object_count != after.embedded_object_count:
        issues.append(
            Issue(
                "error",
                "comparison-embedded-count",
                f"Embedded object count changed from {before.embedded_object_count} to {after.embedded_object_count}.",
            )
        )

    if before.embedding_hashes != after.embedding_hashes:
        issues.append(
            Issue(
                "error",
                "comparison-embedded-objects",
                "Embedded object count, order, or binary content changed.",
            )
        )

    before_links = [
        (
            record.part,
            record.relationship_type,
            record.target,
            record.resolved_part,
            record.target_hash,
        )
        for record in before.embedded_relationships
    ]
    after_links = [
        (
            record.part,
            record.relationship_type,
            record.target,
            record.resolved_part,
            record.target_hash,
        )
        for record in after.embedded_relationships
    ]
    if before_links != after_links:
        issues.append(
            Issue(
                "error",
                "comparison-embedded-relationships",
                "Embedded-object relationships or referenced targets changed.",
            )
        )

    before_drawing_candidates = [
        (record.number, record.xml_hash, record.target_signatures)
        for record in before.drawing_equation_candidates
    ]
    after_drawing_candidates = [
        (record.number, record.xml_hash, record.target_signatures)
        for record in after.drawing_equation_candidates
    ]
    if before_drawing_candidates != after_drawing_candidates:
        issues.append(
            Issue(
                "error",
                "comparison-drawing-equation-candidates",
                "Numbered drawing-only equation candidates changed.",
            )
        )

    before_numbers = [record.number for record in before.numbers]
    after_numbers = [record.number for record in after.numbers]
    if before_numbers != after_numbers:
        issues.append(
            Issue(
                "warning",
                "comparison-equation-numbers",
                f"Visible equation numbers changed from {before_numbers} to {after_numbers}.",
            )
        )

    before_fields = [
        (record.field_type, record.target, record.instruction) for record in before.fields
    ]
    after_fields = [
        (record.field_type, record.target, record.instruction) for record in after.fields
    ]
    if before_fields != after_fields:
        issues.append(
            Issue(
                "warning",
                "comparison-fields",
                "SEQ/REF field instructions changed.",
            )
        )

    ref_targets = {
        record.target
        for record in [*before.fields, *after.fields]
        if record.field_type == "REF"
    }

    def ref_bookmark_bindings(
        audit: AuditResult,
    ) -> list[tuple[str, tuple[tuple[int, str | None, str], ...]]]:
        bindings = []
        for target in sorted(ref_targets):
            owners = tuple(
                (index, equation.number, equation.semantic_hash)
                for index, equation in enumerate(audit.equations, start=1)
                if target in equation.bookmarks
            )
            if owners:
                bindings.append((target, owners))
        return bindings

    if ref_bookmark_bindings(before) != ref_bookmark_bindings(after):
        issues.append(
            Issue(
                "error",
                "comparison-equation-bookmark-bindings",
                "A REF-target bookmark changed its owning equation.",
            )
        )

    before_visible_refs = [record.number for record in before.visible_references]
    after_visible_refs = [record.number for record in after.visible_references]
    if before_visible_refs != after_visible_refs:
        issues.append(
            Issue(
                "warning",
                "comparison-visible-equation-references",
                f"Visible equation references changed from {before_visible_refs} to {after_visible_refs}.",
            )
        )

    if before.bookmarks != after.bookmarks:
        issues.append(
            Issue(
                "warning",
                "comparison-bookmarks",
                "Bookmark names changed.",
            )
        )
    return issues


def render_human(audit: AuditResult, label: str) -> list[str]:
    lines = [
        f"{label}: {audit.path}",
        (
            "Summary: "
            f"native={audit.native_math_count} "
            f"displayed={audit.displayed_math_count} "
            f"inline={audit.inline_math_count} "
            f"embedded={audit.embedded_object_count} "
            f"embedded-links={len(audit.embedded_relationships)} "
            f"embedding-parts={audit.embedding_part_count} "
            f"drawings={audit.drawing_count} "
            f"drawing-equation-candidates={len(audit.drawing_equation_candidates)}"
        ),
        f"Visible equation numbers: {[record.number for record in audit.numbers]}",
        (
            "Fields: "
            f"SEQ={sum(record.field_type == 'SEQ' for record in audit.fields)} "
            f"REF={sum(record.field_type == 'REF' for record in audit.fields)} "
            f"bookmarks={len(audit.bookmarks)}"
        ),
    ]
    for record in audit.equations:
        number = f" number={record.number}" if record.number else ""
        lines.append(
            f"  {record.part}:p{record.paragraph}:e{record.equation} "
            f"{record.role}{number} semantic={record.semantic_hash[:12]}"
        )
    if audit.issues:
        lines.append("Issues:")
        for issue in audit.issues:
            location = ""
            if issue.part:
                location = f" {issue.part}"
                if issue.paragraph is not None:
                    location += f":p{issue.paragraph}"
            lines.append(
                f"  [{issue.severity}] {issue.code}:{location} {issue.message}"
            )
    else:
        lines.append("Issues: none detected by configured checks")
    return lines


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit native and embedded equations in a Word DOCX without editing it."
    )
    parser.add_argument("docx", help="DOCX to audit, or the before version when comparing")
    parser.add_argument(
        "--compare", metavar="AFTER.docx", help="compare equation structures with a revision"
    )
    parser.add_argument(
        "--expect-native", type=int, metavar="N", help="require exactly N native OMML equations"
    )
    parser.add_argument(
        "--expect-displayed",
        type=int,
        metavar="N",
        help="require exactly N displayed or display-candidate native equations",
    )
    parser.add_argument(
        "--require-consecutive",
        action="store_true",
        help="require visible integer equation numbers 1..N in document order",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit nonzero for warnings as well as errors",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.expect_native is not None and args.expect_native < 0:
        print("error: --expect-native must be non-negative", file=sys.stderr)
        return 2
    if args.expect_displayed is not None and args.expect_displayed < 0:
        print("error: --expect-displayed must be non-negative", file=sys.stderr)
        return 2

    try:
        before = load_audit(Path(args.docx))
        add_requested_checks(
            before,
            args.expect_native,
            args.expect_displayed,
            args.require_consecutive,
        )
        after = load_audit(Path(args.compare)) if args.compare else None
        comparison_issues: list[Issue] = []
        if after:
            add_requested_checks(
                after,
                args.expect_native,
                args.expect_displayed,
                args.require_consecutive,
            )
            comparison_issues = compare_audits(before, after)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        payload: dict[str, object] = {"before": before.public_dict()}
        if after:
            payload["after"] = after.public_dict()
            payload["comparison_issues"] = [
                asdict(issue) for issue in comparison_issues
            ]
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print("\n".join(render_human(before, "Audit")))
        if after:
            print()
            print("\n".join(render_human(after, "Compared revision")))
            print()
            if comparison_issues:
                print("Comparison issues:")
                for issue in comparison_issues:
                    print(f"  [{issue.severity}] {issue.code}: {issue.message}")
            else:
                print("Comparison issues: none detected by configured checks")

    all_issues = [*before.issues, *(after.issues if after else []), *comparison_issues]
    has_error = any(issue.severity == "error" for issue in all_issues)
    has_warning = any(issue.severity == "warning" for issue in all_issues)
    return 1 if has_error or (args.strict and has_warning) else 0


if __name__ == "__main__":
    raise SystemExit(main())
