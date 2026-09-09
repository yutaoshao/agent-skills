---
name: paper-writer
description: Draft, revise, verify, and submit English CS, ML, and AI research papers in LaTeX. Use for paper writing from research artifacts, evidence-backed figures and tables, citation verification, LaTeX review, submission preparation, and reviewer responses. Use chinese-engineering-paper-writing for Chinese engineering manuscripts.
---

# Paper Writer

Write and revise English CS/ML/AI papers around a defensible research claim: the problem, technical idea, and evidence must agree. Work directly on the requested task; a paper can begin at any module and does not require a project plan, a fixed stage order, or a venue before drafting.

## Scope

Use this skill for English research papers and LaTeX submission or revision work. Route Chinese engineering-paper drafting and rewriting to `chinese-engineering-paper-writing`. Preserve user-provided templates, claims, notation, and evidence unless the task calls for changing them.

## Choose the work

Load only the module that matches the request. Combine modules when the requested deliverable requires it.

| Request | Module |
|---|---|
| Derive a paper story from code, experiments, or notes | `modules/m01-project-analysis.md` |
| Find, assess, or integrate related work | `modules/m02-literature-review.md` |
| Build or repair an outline and claim structure | `modules/m03-paper-structure.md` |
| Draft or rewrite a paper section | `modules/m04-writing-core.md` |
| Create or check figures and result tables | `modules/m05-figures-tables.md` |
| Verify or repair citations and BibTeX | `modules/m06-citation-management.md` |
| Edit English prose for clarity and argument flow | `modules/m07-polish.md` |
| Compile or diagnose a LaTeX project | `modules/m08-latex-compilation.md` |
| Review a paper or assemble a submission | `modules/m09-review-submission.md` |
| Respond to reviews or prepare a revision | `modules/m10-revision-resubmission.md` |

## Evidence Rules

- Separate verified results, source-supported statements, assumptions, and missing evidence. Do not turn an unverified interpretation into a contribution claim.
- Trace every reported number in a figure, table, abstract, or response letter to its source result, calculation, or supplied manuscript. Report discrepancies with their locations.
- Do not invent papers, authors, venues, identifiers, results, or BibTeX. Verify a cited work from a primary record or supplied source before adding it; retain a visible placeholder when verification is unavailable.
- Treat venue requirements, page limits, templates, disclosure rules, and submission checklists as time-sensitive. Verify them from the target venue's current official materials when the user asks for submission readiness.

## Drafting and Editing

Make the prose serve the argument. State what the work addresses, why the setting is difficult or consequential, what changes technically, and which evidence supports each material claim. Choose section and paragraph shapes from the paper's content and target template; do not impose fixed sentence counts, paragraph counts, reference counts, or vocabulary bans.

When revising, preserve equations, notation, citations, numerical meaning, and valid LaTeX structure unless a change is intentional. Explain substantive framing changes and flag information that is needed to support a stronger claim.

## LaTeX and Delivery

Use the supplied template whenever one exists. Compile before claiming a LaTeX deliverable is ready, inspect the log for actionable errors and unresolved references, and inspect the rendered PDF when layout, floats, figures, tables, or anonymization matter. The requested output may be a focused draft, an edited source file, a findings report, or a submission package.

Read [references/writing-philosophy.md](references/writing-philosophy.md) for English section drafting and revision, [references/citation-guide.md](references/citation-guide.md) for citation work, [references/evidence-review.md](references/evidence-review.md) for figures, tables, and full-paper review, and [references/latex-checklist.md](references/latex-checklist.md) for LaTeX compilation or submission checks.
