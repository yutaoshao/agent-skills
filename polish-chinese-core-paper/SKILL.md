---
name: polish-chinese-core-paper
description: >-
  Polish, substantively edit, review, and prepare Chinese academic manuscripts
  for submission to Chinese core journals, with default discipline guidance for
  computer science and engineering. Audit whether each sentence is supported,
  necessary, correctly placed, and proportionately emphasized. Use for requests
  involving 中文核心、北大核心或 CSCD 论文润色, 中文学术表达优化, 逐句必要性审查,
  内容取舍与篇章位置调整, 摘要或段落改写, 去除机械或 AI 腔, 期刊规范核对,
  保留修改说明, or submission-oriented review of .docx, .tex, .md, PDF, and
  plain-text manuscripts.
---

# Polish Chinese Core Journal Papers

Polish existing Chinese academic manuscripts without changing their evidentiary meaning. Combine general academic Chinese guidance with a discipline profile and a verified target-journal profile; never treat “中文核心” as a shared formatting standard.

## Establish Scope

- Default to computer science and engineering conventions only when the manuscript belongs to those fields.
- For another discipline, apply only the general language and integrity rules unless a relevant discipline profile or authoritative guidance is available. State this limitation in the delivery.
- Distinguish polishing from research contribution development. Diagnose missing evidence or reasoning, but do not invent it.
- Treat target-journal compliance and language polishing as separate claims. A manuscript can be linguistically polished without being journal-compliant.
- Treat grammatical correctness as necessary but insufficient. Judge each sentence or proposition-bearing unit by its function in the paragraph, section, and manuscript.
- Preserve necessary information and evidentiary boundaries, not necessarily the original sentence, wording, location, or repetition. Do not hide an unfavorable result or limitation merely to make the paper appear stronger.

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
| `light` | Correct grammar, punctuation, awkward wording, local redundancy, and local cohesion; flag an obviously unsupported, unnecessary, or misplaced sentence | Delete content-bearing sentences, move information across sections, or change claim structure |
| `standard` | Apply `light`; audit every prose sentence for function, necessity, redundancy, placement, and emphasis; improve paragraph and section coherence | Add evidence, alter conclusions, or silently delete or relocate protected content |
| `deep` | Apply `standard`; reallocate information across sections and propose structural or argumentative repair | Present substantive rewrites, deletions, or changes of emphasis as author-approved facts |

Default to `standard` for an unspecified whole-manuscript request and `light` for a short sentence or paragraph. In `standard`, apply low-risk rewrites, merges, moves, and deletions only when the informational content, evidence attachment, and argumentative emphasis remain intact; log every nonlocal change. Mark every unresolved substantive proposal in `deep` mode for author confirmation.

## Build the Rule Set

1. Read `references/integrity-boundaries.md` before editing any manuscript.
2. Read `references/chinese-academic-style.md` for every language-polishing task.
3. Read `references/sentence-function-audit.md` for `standard`, `deep`, and every request that asks whether content should remain, move, merge, or be deleted.
4. Read `references/cs-engineering-profile.md` only for computer science and engineering manuscripts.
5. For journal-specific work, obtain current official instructions and fill `references/journal-profile-schema.md` in task-local notes.
6. Read `references/review-checklist.md` for `standard`, `deep`, and submission-readiness tasks.

Prefer official author instructions, the official submission system, and official templates. Record the source and access date. Treat recent published articles as examples of editorial practice, not as formal rules. If a requirement cannot be verified, mark it `unknown`; do not infer it from the journal's index category or from another journal.

## Lock Integrity Anchors

Before editing, inventory the protected anchors relevant to the input:

- numbers, units, ranges, uncertainty values, dates, sample sizes, and statistical results;
- equations, symbols, algorithms, code identifiers, method names, datasets, and metrics;
- citation keys, author-year references, quotations, figure/table references, and bibliography metadata;
- research questions, assumptions, limitations, comparison scope, causal strength, and conclusion strength;
- funding, ethics, conflict-of-interest, data-availability, authorship, and affiliation statements.

Preserve atomic anchors such as numbers, symbols, names, citation attachment, and claim strength exactly unless the source material proves a correction. Preserve proposition-level anchors such as assumptions, limitations, and negative results in meaning and appropriate visibility; this does not freeze their original sentence or section. When an apparent error cannot be resolved, keep the original information and report it as an author query.

## Polish in Passes

Process a full manuscript section by section. Read enough surrounding context to preserve the argument, and polish the abstract after the body.

### Pass 1: Diagnose the Manuscript

- Map each section to its rhetorical job and the evidence supporting it.
- Separate language problems from missing reasoning, missing evidence, and journal-format issues.
- Inventory protected propositions as well as atomic anchors so that necessary information can be relocated without being lost.
- For long manuscripts, report the dominant patterns and editing plan before making broad structural changes.

### Pass 2: Audit Every Sentence

- In `standard` and `deep`, evaluate every prose sentence and every proposition-bearing heading, list item, caption, and note using `references/sentence-function-audit.md`.
- Assign one disposition: `keep`, `rewrite`, `merge`, `move`, `delete`, or `query`.
- Apply the deletion test: state what necessary fact, reasoning step, evidence, qualification, or navigation would be lost. If nothing unique would be lost, merge or delete the sentence.
- Check whether the information has a better home elsewhere and whether its current position gives it too much or too little emphasis.
- Keep the full ledger in working notes. Deliver changed, risky, or queried items unless the user requests a complete sentence-by-sentence report.

### Pass 3: Recompose the Information

- Align title, abstract, research question, method, results, discussion, and conclusion.
- Give each necessary proposition one primary home. Repeat it elsewhere only when the new location serves a distinct reader need.
- Give each paragraph one identifiable job while preserving necessary nuance.
- Repair missing logical links by stating the real relation: cause, contrast, condition, progression, example, or limitation.
- Treat abstract position as an editorial decision: include information needed to interpret the main claim, but do not copy every limitation or compliance statement into the abstract. State evaluation scope directly and place fuller limitations where readers can assess them.
- In `deep` mode, present high-risk moves, merges, deletions, and changes of emphasis as explicit proposals.

### Pass 4: Refine Academic Chinese

- Prefer precise subjects, active information flow, concrete verbs, and stable terminology.
- Remove empty emphasis, redundant framing, translationese, and mechanical transitions only when they add no meaning.
- Vary sentence structure without turning style variation into an objective of its own.
- Retain necessary hedging and disciplinary phrasing. Do not use a banned-word list as an automatic rewriting rule.
- Preserve the author's defensible voice rather than homogenizing every paragraph.

### Pass 5: Check Claims and Evidence

- Keep observed association, explanation, prediction, and causation distinct.
- Tie comparisons to the named baseline, dataset, metric, condition, and numerical result.
- Use “显著” as a statistical claim only when the manuscript provides an appropriate test; otherwise query or weaken it with author approval.
- Never generate references or bibliographic metadata from memory. Preserve unverified items and mark them `[待核引]` in the report rather than silently completing them.

### Pass 6: Check Journal Requirements

- Evaluate only requirements recorded in the journal profile.
- Report each requirement as `pass`, `fail`, `unknown`, or `not-applicable`, with evidence.
- Keep formal requirements separate from optional style suggestions.
- Do not claim that compliance predicts acceptance.

### Pass 7: Verify the Revision

- Compare the revised manuscript against the integrity-anchor inventory.
- Run a coverage check: every necessary protected proposition from the source remains present, correctly scoped, and sufficiently visible.
- Run an entitlement check: every sentence in the revised manuscript performs a necessary function in its current location.
- Recheck every changed or relocated sentence containing a number, citation, equation reference, comparison, limitation, negative result, or conclusion.
- Read the clean revision independently of the change log, then re-read each modified paragraph in context; pattern replacement alone is not a quality check.
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
3. sentence-level moves, merges, deletions, and changes of emphasis, each with its editorial reason;
4. unresolved author queries, each tied to a location and reason;
5. a journal-compliance table when a verified target profile exists;
6. an integrity summary confirming what was compared and listing any anchors or protected propositions that could not be verified.

Describe the result as ready for author review, not guaranteed submission acceptance.

## Reference Map

- `references/chinese-academic-style.md`: paragraph, sentence, terminology, and de-mechanization guidance.
- `references/integrity-boundaries.md`: protected anchors, claim-strength rules, and author-confirmation boundaries.
- `references/sentence-function-audit.md`: sentence-level function, necessity, placement, emphasis, and disposition rules.
- `references/journal-profile-schema.md`: source hierarchy and task-local journal requirement template.
- `references/cs-engineering-profile.md`: default rhetorical and evidentiary guidance for computer science and engineering.
- `references/review-checklist.md`: final quality gate, severity model, and delivery report structure.
