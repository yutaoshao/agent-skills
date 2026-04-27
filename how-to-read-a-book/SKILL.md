---
name: how-to-read-a-book
description: Apply the active-reading methods inspired by Mortimer J. Adler and Charles Van Doren's "How to Read a Book" / "如何阅读一本书". Use when creating reading plans; inspecting or analyzing books, papers, long articles, textbooks, arguments, or study materials; choosing between elementary, inspectional, analytical, and syntopical reading; producing book maps, question lists, chapter notes, critique frameworks, comparative reading syntheses, or deliberate practice plans for better reading.
---

# How to Read a Book

Use active reading as a disciplined investigation: identify what the text is, what it says, whether it is true, and why it matters. Paraphrase the method; do not reproduce copyrighted passages from the source book.

## Quick Start

1. Identify the user's purpose: survey, understand, critique, compare, remember, teach, or apply.
2. Choose the lowest reading level that can satisfy the purpose.
3. Ask for missing source material only when the task depends on unavailable text.
4. Produce visible reading artifacts: structure map, key questions, claims, evidence, terms, objections, and next actions.
5. Separate source-grounded observations from interpretation and speculation.

## Reading Level Decision Tree

- **Elementary reading**: Use when the user needs vocabulary, sentence-level comprehension, translation help, or a plain-language explanation.
- **Inspectional reading**: Use when the user needs a fast orientation, book selection advice, chapter triage, a reading plan, or a preview before deep work.
- **Analytical reading**: Use when the user needs deep understanding of one work: thesis, structure, terms, propositions, arguments, evidence, and critique.
- **Syntopical reading**: Use when the user needs to compare multiple works on the same problem, extract disagreements, or build a research view.

Prefer inspectional reading before analytical reading unless the user has already supplied a clear section, chapter, or argument to analyze.

## Inspectional Reading Workflow

Use this for a rapid first pass.

1. Classify the work by kind, subject, audience, and likely difficulty.
2. Read metadata and surface structure: title, subtitle, table of contents, preface, introduction, conclusion, headings, index, abstract, figures, and summaries when available.
3. Infer the central problem the author is trying to solve.
4. Build a provisional map of parts and their functions.
5. Identify high-value chapters or sections for deeper reading.
6. List questions the analytical pass should answer.

Output a short brief:

```markdown
## Inspectional Brief
- Work type:
- Main subject:
- Likely central question:
- Provisional structure:
- Sections to read deeply:
- Questions for analytical reading:
- Skip/defer:
```

## Analytical Reading Workflow

Use this when the goal is mastery of one work.

1. State the whole-book question: what is the book about as a whole?
2. Map the structure: major parts, chapter roles, and progression of the argument.
3. Define the author's key terms in context; do not assume everyday meanings.
4. Extract major propositions: the claims the author needs the reader to accept.
5. Reconstruct the argument: premises, evidence, reasoning moves, and conclusion.
6. Locate the author's answer to the central problem.
7. Evaluate only after understanding: identify agreement, disagreement, missing evidence, ambiguous terms, weak reasoning, or unresolved implications.
8. Convert insight into action: notes, memory prompts, teaching outline, implementation checklist, or research questions.

Output in this order:

```markdown
## Analytical Reading Notes
### 1. Whole-Book Question
### 2. Structure Map
### 3. Key Terms
### 4. Main Claims
### 5. Argument Reconstruction
### 6. Evaluation
### 7. What To Do With This
```

## Syntopical Reading Workflow

Use this when comparing multiple sources around one problem.

1. Define the neutral question in the user's words before adopting any author's framing.
2. Build a source inventory with each work's scope, stance, and reliability constraints.
3. Translate each author's terms into a shared vocabulary while preserving important differences.
4. Arrange the competing answers by position, not by book order.
5. Compare evidence, assumptions, definitions, and consequences.
6. Identify real disagreements, apparent disagreements, and gaps none of the sources answer.
7. Produce a synthesis that makes the debate clearer without forcing false consensus.

Output a comparison matrix when useful:

```markdown
| Question | Source A | Source B | Source C | Notes |
|---|---|---|---|---|
```

## Genre Adaptation

- **Practical books**: Extract the problem, proposed rules, conditions of use, failure modes, and an action plan.
- **Theoretical books**: Reconstruct definitions, propositions, arguments, evidence, and implications.
- **Textbooks**: Turn chapters into learning objectives, worked examples, review questions, and practice schedule.
- **Research papers**: Identify research question, method, assumptions, results, limitations, and follow-up experiments.
- **Essays and articles**: Separate thesis, rhetorical strategy, evidence, audience, and hidden assumptions.
- **Literature**: Focus on plot structure, characters, themes, symbols, style, historical context, and interpretive alternatives.

## Source Grounding Rules

- If the user supplies text, cite section names, chapter names, page numbers, or short snippets when available.
- If the source text is unavailable, clearly mark the output as a plan, heuristic, or inference.
- Do not invent page numbers, quotations, chapter titles, or claims from a work that has not been provided.
- Keep direct quotations short and only when they are necessary; otherwise paraphrase.
- Distinguish "the author argues" from "a reader might infer".

## Useful Prompts to Generate

- "Create an inspectional reading brief before I decide whether to read this."
- "Turn this chapter into analytical reading notes."
- "Map the author's argument and list the claims I need to verify."
- "Create a reading plan for this technical book over four weeks."
- "Compare these three books syntopically around one question."
- "Quiz me on the key terms and propositions from this chapter."

## Output Style

Be structured, concrete, and question-driven. Favor compact tables, checklists, and maps over long summaries. When the user is actively studying, end with a small set of next reading actions rather than a generic conclusion.
