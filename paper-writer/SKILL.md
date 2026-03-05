---
name: paper-writer
description: |
  Academic paper writing skill for CS/ML/AI researchers. Use this skill when the user wants to
  write a research paper from project source code, draft paper sections, structure a paper,
  generate figures/tables, manage citations, polish text (de-AI), compile LaTeX, prepare for
  conference/journal submission, or handle reviewer responses. Supports NeurIPS, ICML, ICLR,
  ACL, AAAI, COLM conference formats and custom templates. Triggers on: "write paper",
  "draft paper", "paper from code", "prepare submission", "write introduction/methods/experiments",
  "polish paper", "de-AI", "expand citations", "rebuttal", "camera-ready".
---

# Paper Writer - CS/ML/AI Academic Paper Writing

From project source code to submission-ready LaTeX paper. A 10-stage lifecycle covering code analysis, literature review, paper structure, section drafting, figure/table generation, citation management, de-AI polishing, LaTeX compilation, submission preparation, and revision handling.

## 0. Execution Gate

Before any substantive task, execute in order:

### 0.1 Discuss Before Execute

- Restate user's goal in 2-5 sentences: topic, current stage, target output, target venue, deadline.
- If information is incomplete, ask before proceeding.
- If user explicitly says "skip discussion", proceed but still write to plan.

### 0.2 Check or Create plan/

- If `plan/` does not exist, initialize from `plan-template/` (run `scripts/init_plan.sh` or copy manually).
- If `plan/` exists, read `project-overview.md`, `progress.md`, `notes.md`, `stage-gates.md` before continuing.

### 0.3 Task Logging

- Before execution: write a "task card" to `plan/progress.md` (task name, type, input, expected output).
- After execution: update completion status, output path, next action.

### 0.4 No Plan, No Long Task

- One-off Q&A is exempt. Any task involving writing >1 section or multi-file edits requires plan/ management.

## 1. Default Output Norms

### 1.1 De-AI Language (Enforced Always)

- **English**: No mechanical transitions (Furthermore/Moreover/Additionally/Notably). No bold-label paragraph openers. No filler phrases. No AI vocabulary (leverage/utilize/harness/delve/paradigm/landscape/plethora). Max 2 identical transition words per section.
- **Chinese**: No mechanical transitions (首先/其次/最后/此外/另外). No emphasis fillers (值得注意的是/需要指出的是). No subjective phrases in formal text (我认为/我觉得).

### 1.2 Formatting

- Continuous prose paragraphs in body text. Lists only in plan files, checklists, parameter tables, and step instructions.
- One blank line between paragraphs. No consecutive blank lines.
- No unnecessary bold or italic in body text.

### 1.3 Delivery Format

- Default output: LaTeX (`.tex` + `.bib`).
- Markdown for plan files, outlines, and reports.
- Figures: PDF (vector) for plots, PNG (450 DPI) for raster. Dual format when possible.

## 2. Workflow Decision Tree

Route user requests to the appropriate module(s):

| Trigger Keywords | Module(s) |
|-----------------|-----------|
| "analyze code", "extract contributions", "understand repo" | M01: Project Analysis |
| "literature review", "find papers", "related work", "survey" | M02: Literature Review |
| "outline", "structure", "plan paper", "organize" | M03: Paper Structure |
| "write", "draft", "introduction", "methods", "experiments", "abstract" | M04: Writing Core |
| "figures", "plots", "tables", "TikZ", "diagram", "chart" | M05: Figures & Tables |
| "citations", "references", "bibliography", "verify citations" | M06: Citation Management |
| "polish", "de-AI", "improve writing", "natural writing", "rewrite" | M07: Polish |
| "compile", "LaTeX", "template", "format", "build" | M08: LaTeX Compilation |
| "review", "submission", "checklist", "quality check", "submission ready" | M09: Review & Submission |
| "revision", "resubmit", "rebuttal", "reviewer comments", "camera-ready" | M10: Revision & Resubmission |
| "write paper from scratch", "full paper" | Run M01 through M09 sequentially |
| Ambiguous or unclear | Ask user to clarify, default to M09 for existing papers |

When a full paper writing project is initiated, stages execute in order S1-S10. Each stage can also be invoked independently.

## 3. Template Selection

```
User initiates paper writing:
|-- User provides a .tex template?
|   |-- YES: Use user-provided template. Verify it compiles first.
|   '-- NO: Ask about target venue.
|       |-- Specifies conference (NeurIPS/ICML/ICLR/ACL/AAAI/COLM)?
|       |   '-- YES: Follow references/templates-guide.md to download official template.
|       |-- Specifies journal?
|       |   '-- YES: Provide official template download link if known. Ask user to supply if not.
|       '-- No preference?
|           '-- Recommend NeurIPS format. Provide download link.
```

Template setup workflow:
1. Download or copy the full template directory (not just main.tex).
2. Verify the template compiles as-is before any changes.
3. Replace content section by section, keeping template comments as reference.
4. Clean up template artifacts only at the end.

See `references/templates-guide.md` for download links and compilation guides.

## 4. Stage Overview

| Stage | Module | Deliverable |
|-------|--------|-------------|
| S1 | M01: Project Analysis | Contribution summary, artifact-to-section mapping |
| S2 | M02: Literature Review | Organized reference list, related work draft |
| S3 | M03: Paper Structure | Complete paper outline in `plan/outline.md` |
| S4 | M04: Writing Core | Full paper draft (all sections) |
| S5 | M05: Figures & Tables | Publication-quality figures and verified tables |
| S6 | M06: Citation Management | Verified bibliography, no placeholders |
| S7 | M07: Polish | De-AI'd, natural academic prose |
| S8 | M08: LaTeX Compilation | Clean compilation, passes checklist |
| S9 | M09: Review & Submission | Passes all checklists, submission package ready |
| S10 | M10: Revision & Resubmission | Reviewer response, revised paper |

## 5. Module Briefs

Each module is defined in `modules/`. Load only the required module file for the current task.

### M01: Project Analysis (`modules/m01-project-analysis.md`)

Explore a research repository to extract contributions, methods, and results. Map code artifacts to paper sections. Generate a "contribution hypothesis" for user confirmation.

### M02: Literature Review (`modules/m02-literature-review.md`)

Search for relevant papers, organize by theme, identify research gaps, and write a synthesized literature review. English literature via WebSearch + Semantic Scholar. Chinese literature: provide search strategy for CNKI/Wanfang.

### M03: Paper Structure (`modules/m03-paper-structure.md`)

Define the one-sentence contribution. Apply the Narrative Principle (What/Why/So What). Generate a paper outline with section-to-contribution mapping. Conference-specific structure guidance.

### M04: Writing Core (`modules/m04-writing-core.md`)

Section-by-section drafting: Abstract (5-sentence formula), Introduction (contribution bullets), Methods (enable reimplementation), Experiments (explicit claims), Related Work (methodological organization), Limitations, Conclusion. Applies Gopen & Swan 7 Principles and writing philosophy.

### M05: Figures & Tables (`modules/m05-figures-tables.md`)

Python figure generation (450 DPI, Nature/Science/Cell palettes, colorblind-safe). TikZ diagram verification. Table data cross-checking against source data files. Accessibility compliance.

### M06: Citation Management (`modules/m06-citation-management.md`)

Anti-hallucination protocol: NEVER generate BibTeX from memory. 5-step verification (Search -> Verify -> Fetch BibTeX via DOI -> Validate claim -> Add). Citation gap analysis and expansion. Natural citation integration.

### M07: Polish (`modules/m07-polish.md`)

Merged de-AI pattern detection: 8 English categories + 4 Chinese categories. Paragraph-level flow assessment. Three-round quality check (structure -> language -> formatting). Load `references/de-ai-patterns.md`.

### M08: LaTeX Compilation (`modules/m08-latex-compilation.md`)

Template selection and setup. Compilation pipeline verification. 80+ item checklist from `references/latex-checklist.md`. Typography, cross-reference, and formatting checks.

### M09: Review & Submission (`modules/m09-review-submission.md`)

Comprehensive pre-submission review (runs M06+M07+M08 checks). Conference-specific checklists (NeurIPS 16-item, ICML, ICLR, ACL, AAAI). Self-review from reviewer perspective. Submission package preparation (cover letter, author contributions, ethics statements).

### M10: Revision & Resubmission (`modules/m10-revision-resubmission.md`)

Reviewer response matrix (comment-by-comment classification). Change log generation. Conference format conversion workflow. Camera-ready preparation.

## 6. Citation Rules (CRITICAL)

**AI-generated citations have ~40% error rate. This is the single most important rule.**

| Situation | Action |
|-----------|--------|
| Need to cite a paper | Search API -> Verify existence -> Fetch BibTeX via DOI |
| Cannot verify a paper | Mark as `[CITATION NEEDED]` or `\cite{PLACEHOLDER_verify}` |
| "I think there's a paper about X" | NEVER cite from memory. Search first or mark placeholder. |
| Found paper, got DOI, fetched BibTeX | Safe to use |
| Found paper, no DOI | Use arXiv BibTeX or manual entry from the actual paper |

Always inform the user about any placeholder citations.

See `references/citation-guide.md` and `modules/m06-citation-management.md` for the complete workflow.

## 7. Literature & Fact Rules

1. Never fabricate references.
2. English literature: searchable via WebSearch, Semantic Scholar, arXiv.
3. Chinese literature: provide search strategy for user to query CNKI/Wanfang/CSCD. Do not generate Chinese citations from memory.
4. Every citation must be traceable (at minimum: author, year, source).
5. Factual claims require evidence. Do not assert unsupported claims.

## 8. Output Priority

When rules conflict, priority order:

1. User's explicit request (highest)
2. This skill's execution gates (Section 0)
3. Citation rules (Section 6) -- never compromise on anti-hallucination
4. Module-specific procedures
5. Default output norms (Section 1) (lowest)

## 9. Proactivity Guidelines

Default: be proactive. Deliver drafts, then iterate.

| Confidence Level | Action |
|-----------------|--------|
| **High** (clear repo, obvious contribution) | Write full draft, deliver, iterate on feedback |
| **Medium** (some ambiguity) | Write draft with flagged uncertainties, continue |
| **Low** (major unknowns) | Ask 1-2 targeted questions, then draft |

When delivering a draft, include notes like:
- "I framed the contribution as X -- adjust if needed"
- "I highlighted results A, B, C -- let me know if others are more important"
- "I cited papers X, Y, Z -- add any I missed"

Only block for input when:
- Target venue is unclear (affects page limits and framing)
- Multiple contradictory framings seem equally valid
- Results seem incomplete or inconsistent

## 10. Quick Response Templates

### Template A: Project Start

```
Based on my analysis of the repository, I understand:
- Main contribution: [contribution]
- Key results: [results]
- Target venue: [venue]

I'll initialize plan/ and begin with [stage].
```

### Template B: Stage Complete

```
Completed: [stage result].
Updated plan/progress.md and plan/notes.md.
Next step: [next action].
```

### Template C: Citation Placeholder

```
I've marked [N] citations as placeholders that need verification:
- [paper description] -- could not find in Semantic Scholar
- [paper description] -- found similar paper but different authors
Please verify these before submission.
```

## 11. Reference Files

Load on demand. Do not load all files at once.

| File | When to Load |
|------|-------------|
| `references/de-ai-patterns.md` | M07 (Polish) |
| `references/citation-guide.md` | M02 (Literature Review), M06 (Citation Management) |
| `references/latex-checklist.md` | M08 (LaTeX Compilation), M09 (Review) |
| `references/writing-philosophy.md` | M04 (Writing Core) |
| `references/conference-checklists.md` | M09 (Review & Submission) |
| `references/reviewer-guidelines.md` | M09 (Review), M10 (Revision) |
| `references/prompts-collection.md` | M04 (Writing), M07 (Polish) -- translation/rewrite prompts |
| `references/color-palettes.md` | M05 (Figures & Tables) |
| `references/templates-guide.md` | M08 (LaTeX Compilation) -- template download and setup |

## 12. Module Files

| File | Stage |
|------|-------|
| `modules/m01-project-analysis.md` | S1 |
| `modules/m02-literature-review.md` | S2 |
| `modules/m03-paper-structure.md` | S3 |
| `modules/m04-writing-core.md` | S4 |
| `modules/m05-figures-tables.md` | S5 |
| `modules/m06-citation-management.md` | S6 |
| `modules/m07-polish.md` | S7 |
| `modules/m08-latex-compilation.md` | S8 |
| `modules/m09-review-submission.md` | S9 |
| `modules/m10-revision-resubmission.md` | S10 |
