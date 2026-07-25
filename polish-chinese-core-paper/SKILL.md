---
name: polish-chinese-core-paper
description: >-
  Polish, review, and prepare Chinese academic manuscripts for submission to
  Chinese core journals, with default discipline guidance for computer science
  and engineering. Use for requests involving 中文核心、北大核心或 CSCD 论文润色,
  中文学术表达优化, 摘要或段落改写, 去除机械或 AI 腔, 期刊规范核对, 保留修改说明,
  or submission-oriented review of .docx, .tex, .md, PDF, and plain-text
  manuscripts.
---

# Polish Chinese Core Journal Papers

Polish existing Chinese academic manuscripts without changing their evidentiary meaning. Combine general academic Chinese guidance with a discipline profile and a verified target-journal profile; never treat “中文核心” as a shared formatting standard.

## Establish Scope

- Default to computer science and engineering conventions only when the manuscript belongs to those fields.
- For another discipline, apply only the general language and integrity rules unless a relevant discipline profile or authoritative guidance is available. State this limitation in the delivery.
- Distinguish polishing from research contribution development. Diagnose missing evidence or reasoning, but do not invent it.
- Treat target-journal compliance and language polishing as separate claims. A manuscript can be linguistically polished without being journal-compliant.

## Collect Inputs

Collect only information that materially affects the requested result:

1. Obtain the manuscript or excerpt and identify its file format.
2. Ask for the target journal and article type when the user requests compliance checking. Accept a journal URL, author guide, or template when provided.
3. Identify the discipline, manuscript stage, desired editing level, and any terminology that must remain unchanged.
4. Agree on the output form: clean copy, annotated revision, tracked changes, or review report.

Do not block excerpt-level or general language polishing when the target journal is unknown. Proceed under general academic Chinese conventions and label journal-specific checks as `unknown`.

## Select Editing Level

| Level | Apply | Do not do silently |
|---|---|---|
| `light` | Correct grammar, punctuation, redundancy, awkward wording, and local cohesion | Reorder paragraphs or change claim structure |
| `standard` | Apply `light`; improve paragraph focus, transitions, terminology, and section-level coherence | Add evidence, alter conclusions, or substantially recast the argument |
| `deep` | Apply `standard`; propose structural reorganization and argument repair | Present substantive rewrites as author-approved facts |

Default to `standard` for an unspecified whole-manuscript request and `light` for a short sentence or paragraph. Mark every substantive proposal in `deep` mode for author confirmation.

## Build the Rule Set

1. Read `references/integrity-boundaries.md` before editing any manuscript.
2. Read `references/chinese-academic-style.md` for every language-polishing task.
3. Read `references/cs-engineering-profile.md` only for computer science and engineering manuscripts.
4. For journal-specific work, obtain current official instructions and fill `references/journal-profile-schema.md` in task-local notes.
5. Read `references/review-checklist.md` for `standard`, `deep`, and submission-readiness tasks.

Prefer official author instructions, the official submission system, and official templates. Record the source and access date. Treat recent published articles as examples of editorial practice, not as formal rules. If a requirement cannot be verified, mark it `unknown`; do not infer it from the journal's index category or from another journal.

## Lock Integrity Anchors

Before editing, inventory the protected anchors relevant to the input:

- numbers, units, ranges, uncertainty values, dates, sample sizes, and statistical results;
- equations, symbols, algorithms, code identifiers, method names, datasets, and metrics;
- citation keys, author-year references, quotations, figure/table references, and bibliography metadata;
- research questions, assumptions, limitations, comparison scope, causal strength, and conclusion strength;
- funding, ethics, conflict-of-interest, data-availability, authorship, and affiliation statements.

Preserve these anchors exactly unless the source material proves a correction. When an apparent error cannot be resolved, keep the original in the manuscript and report it as an author query.

## Polish in Passes

Process a full manuscript section by section. Read enough surrounding context to preserve the argument, and polish the abstract after the body.

### Pass 1: Diagnose

- Map each section to its rhetorical job and the evidence supporting it.
- Separate language problems from missing reasoning, missing evidence, and journal-format issues.
- For long manuscripts, report the dominant patterns and editing plan before making broad structural changes.

### Pass 2: Repair Structure

- Align title, abstract, research question, method, results, discussion, and conclusion.
- Give each paragraph one identifiable job while preserving necessary nuance.
- Repair missing logical links by stating the real relation: cause, contrast, condition, progression, example, or limitation.
- In `deep` mode, present moves, merges, and deletions as explicit proposals.

### Pass 3: Refine Academic Chinese

- Prefer precise subjects, active information flow, concrete verbs, and stable terminology.
- Remove empty emphasis, redundant framing, translationese, and mechanical transitions only when they add no meaning.
- Vary sentence structure without turning style variation into an objective of its own.
- Retain necessary hedging and disciplinary phrasing. Do not use a banned-word list as an automatic rewriting rule.
- Preserve the author's defensible voice rather than homogenizing every paragraph.

### Pass 4: Check Claims and Evidence

- Keep observed association, explanation, prediction, and causation distinct.
- Tie comparisons to the named baseline, dataset, metric, condition, and numerical result.
- Use “显著” as a statistical claim only when the manuscript provides an appropriate test; otherwise query or weaken it with author approval.
- Never generate references or bibliographic metadata from memory. Preserve unverified items and mark them `[待核引]` in the report rather than silently completing them.

### Pass 5: Check Journal Requirements

- Evaluate only requirements recorded in the journal profile.
- Report each requirement as `pass`, `fail`, `unknown`, or `not-applicable`, with evidence.
- Keep formal requirements separate from optional style suggestions.
- Do not claim that compliance predicts acceptance.

### Pass 6: Verify the Revision

- Compare the revised manuscript against the integrity-anchor inventory.
- Recheck every changed sentence containing a number, citation, equation reference, comparison, limitation, or conclusion.
- Read each modified paragraph in context; pattern replacement alone is not a quality check.
- Run the final checks in `references/review-checklist.md` and surface every unresolved issue.

## Handle File Formats

- For `.docx`, use structured Word tooling. Preserve styles, fields, equations, comments, footnotes, and revision state; use tracked changes only when the selected tool can generate valid Word revisions.
- For `.tex`, preserve commands, environments, labels, references, citations, and macros. Compile after source-format edits when a compatible toolchain is available, and report unavailable compilation plainly.
- For `.md` and plain text, preserve headings, tables, citation syntax, and code blocks.
- For PDF-only input, perform review and return replacement text or annotations. Request the editable source before promising an in-place polished manuscript.
- Never silently convert a manuscript into a format that loses tracked changes, equations, references, or layout semantics.

## Use the Diagnostic Script

Run the bundled checker on UTF-8 plain text, Markdown, or LaTeX when deterministic diagnostics help:

```bash
python3 scripts/check_chinese_style.py manuscript.txt
python3 scripts/check_chinese_style.py manuscript.tex --json
python3 scripts/check_chinese_style.py manuscript.md --long-sentence 70
```

Use `--long-sentence 0` to disable the configurable sentence-length heuristic. The script reports review prompts and never rewrites text. Do not run it directly on `.docx` or PDF files; extract text with format-aware tooling first. Treat zero findings only as “no configured patterns detected,” not as proof of quality or compliance.

## Deliver the Result

Match delivery detail to task size. For a short excerpt, provide the polished text and concise notes. For a section or full manuscript, provide:

1. the clean revised manuscript in the requested format;
2. an annotated revision or change log identifying structural and semantic-risk changes;
3. unresolved author queries, each tied to a location and reason;
4. a journal-compliance table when a verified target profile exists;
5. an integrity summary confirming what was compared and listing any anchors that could not be verified.

Describe the result as ready for author review, not guaranteed submission acceptance.

## Reference Map

- `references/chinese-academic-style.md`: paragraph, sentence, terminology, and de-mechanization guidance.
- `references/integrity-boundaries.md`: protected anchors, claim-strength rules, and author-confirmation boundaries.
- `references/journal-profile-schema.md`: source hierarchy and task-local journal requirement template.
- `references/cs-engineering-profile.md`: default rhetorical and evidentiary guidance for computer science and engineering.
- `references/review-checklist.md`: final quality gate, severity model, and delivery report structure.
