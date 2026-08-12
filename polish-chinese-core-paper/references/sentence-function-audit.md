# Sentence Function and Necessity Audit

Use this audit to decide not only how a sentence should be written, but whether its information should appear in its current form and location. Treat fluency as a quality condition, not as a reason to retain a sentence.

## Contents

1. Core rule
2. Audit units
3. Sentence gates
4. Dispositions
5. Section allocation
6. Position and emphasis
7. Integrity safeguards
8. Working ledger and verification
9. Worked case

## Core Rule

Judge a sentence at four levels at once:

```text
sentence -> paragraph -> section -> whole manuscript
```

A sentence earns its place only when it is supported, performs a necessary function, occupies the best available location, and receives emphasis proportional to its importance. A true sentence can still be redundant, misplaced, overemphasized, or unnecessary. An awkward sentence can still carry information that must be preserved through rewriting or relocation.

Do not use reader comfort, favorable appearance, or narrative smoothness as grounds for hiding a limitation, negative result, or boundary condition.

## Audit Units

- Audit every prose sentence in `standard` and `deep` work.
- Treat a proposition-bearing heading, list item, caption, table note, footnote, or callout as a sentence-equivalent unit.
- Audit distinct propositions separately when one grammatical sentence contains multiple claims with different evidence or functions.
- Treat displayed equations and material inline formulas as technical units: audit their function, necessity, placement, definition, and later use while preserving their mathematical semantics. For Word files, apply `word-equation-typesetting.md`; do not rewrite mathematics as part of a prose-only edit.
- Create identifiers for protected propositions when they may move, such as `P-LIM-01`, `P-RESULT-03`, or `P-SCOPE-02`.

## Sentence Gates

Apply all gates before choosing a disposition:

| Gate | Required question | Failure signal |
|---|---|---|
| Evidence | Is every factual or inferential claim supported and correctly scoped? | Unsupported claim, altered certainty, detached citation, or invented detail |
| Function | What exact job does the unit perform? | It can only be described as “background,” “transition,” or “emphasis” without a reader need |
| Necessity | What necessary information or reasoning would be lost if it disappeared? | Nothing unique is lost |
| Uniqueness | Is the same proposition already stated more effectively elsewhere? | Repetition without a different rhetorical purpose |
| Placement | Does this function belong in the current paragraph and section? | The information is valid but interrupts the local job or belongs elsewhere |
| Emphasis | Does wording and position give the proposition proportionate weight? | A minor point occupies a strong position, or a material boundary is buried |
| Sequence | Does it follow from the preceding unit and prepare what follows? | Missing premise, abrupt topic change, or delayed qualification |

Use concrete function labels: define, scope, motivate, identify a gap, state a question, claim a contribution, describe a method, report evidence, interpret evidence, compare, qualify, transition, or conclude. Do not treat an empty transition or generic emphasis marker as an independent function.

Apply the deletion test explicitly:

> If this unit were removed, which necessary fact, inference, evidence attachment, qualification, or navigation cue would the reader lose?

If the answer is “none,” delete or merge it. If the answer is uncertain because the source or disciplinary context is incomplete, query the author.

Do not require every sentence to add a new fact. A topic sentence, synthesis, qualification, or navigation cue can be necessary when it reduces interpretive ambiguity or makes the reasoning recoverable.

## Dispositions

Assign one primary disposition to each audited unit. Record a linked secondary action when one source sentence contains propositions that must be split or allocated to different sections.

| Disposition | Use when | Required safeguard |
|---|---|---|
| `keep` | The unit is supported, necessary, well placed, and proportionate | Verify its links to adjacent units |
| `rewrite` | The information is necessary but expression, scope, or emphasis is defective | Preserve facts, claim strength, and citation attachment |
| `merge` | Necessary information is fragmented or duplicated | Do not merge claims supported by different evidence |
| `move` | The information is necessary but belongs elsewhere | Preserve dependencies, visibility, and the proposition identifier |
| `delete` | The unit contains no unique necessary information or valid rhetorical function | Confirm that no protected proposition, citation role, or logical step disappears |
| `query` | Necessity, evidence, intended emphasis, or authorial meaning cannot be resolved | Keep a provisional version and state the decision needed |

In `light`, flag content-bearing `move`, `delete`, and `query` decisions without applying them silently. In `standard`, apply only low-risk dispositions whose informational content and argumentative emphasis remain intact, and log every nonlocal change. In `deep`, show high-risk dispositions as explicit proposals and request confirmation where required by the integrity rules.

Use stable identifiers such as `E-001` for audited equations. A formula can receive a disposition, but changing its operators, operands, signs, scripts, conditions, or symbol meanings is a mathematical-content edit rather than a language rewrite and requires an explicit evidence trail and author confirmation when unresolved.

## Section Allocation

Use the following matrix as a default editorial model. Verified target-journal rules and article-type conventions take precedence.

| Section | Primary information | Common placement error |
|---|---|---|
| Title | Research object, problem, method, or differentiating scope | Unsupported evaluation, procedural detail, or generic wording |
| Abstract | Purpose, essential method, evaluation setting, principal evidence, and bounded conclusion | Long background, audit-style compliance statements, secondary limitations, or claims absent from the body |
| Introduction | Concrete problem, unresolved gap, research question, contribution, and necessary scope | Detailed procedures, result-by-result reporting, or slogans disconnected from the gap |
| Related work | Synthesis of relevant approaches, evidence, disagreements, and remaining gap | Chronological citation lists or material unrelated to the stated gap |
| Methods | Objects, assumptions, system boundaries, procedures, and reproducibility details | Results, unsupported benefits, or rationale repeated from the introduction |
| Results | Observations, measurements, comparisons, and material negative or mixed findings | Speculative mechanism, broad implication, or selective omission of relevant outcomes |
| Discussion or limitations | Interpretation, relation to prior work, alternative explanations, applicability boundaries, and validation limits | Repeating all results or introducing new unsupported evidence |
| Conclusion | Direct answer, main contribution at supported strength, important scope, and grounded next work | New evidence, abstract duplication, or generic future-work lists |

Give a proposition one primary home. Repeat it only when a second location serves a distinct reader need, and adapt the expression to that function instead of copying the sentence.

## Position and Emphasis

- Treat the title, abstract ending, section opening, paragraph opening, and paragraph ending as high-emphasis positions.
- Distinguish “must remain visible in the manuscript” from “must be stated explicitly in the abstract.”
- Prefer a direct positive scope statement in the abstract when it truthfully defines the evaluation setting. Place a fuller negative limitation in the discussion when that is the best location for interpretation.
- Keep an explicit limitation in the abstract when it materially changes how the main finding must be understood, directly conflicts with the paper's practical claim, or is required by the target journal.
- Do not bury a material boundary in a generic future-work sentence.
- Recheck emphasis after moving or merging text. A fact can remain present yet become misleadingly obscure or disproportionately prominent.

## Integrity Safeguards

- Preserve the proposition, not necessarily its original wording or location.
- Preserve exact numbers, technical objects, comparison conditions, claim strength, and citation attachment wherever the proposition moves.
- Do not delete an unfavorable but material result because it weakens the narrative.
- Do not retain a sentence solely because it states a limitation; decide whether to rewrite, merge, or move it while maintaining adequate visibility.
- Do not turn absence of evidence into evidence of absence, and do not turn a planned validation into completed work.
- Raise an author query when moving a proposition would change the manuscript's apparent contribution, risk profile, or conclusion strength.

## Working Ledger and Verification

Keep this ledger in task-local working notes for `standard` and `deep` work:

| ID | Original location | Function | Evidence or anchor | Necessity result | Placement and emphasis | Disposition | Reason or query |
|---|---|---|---|---|---|---|---|
| S-001 | | | | necessary / mergeable / unnecessary / uncertain | appropriate / move / rebalance | keep / rewrite / merge / move / delete / query | |

For a long manuscript, complete the ledger section by section. Do not use sampling as a substitute for an exhaustive audit when the requested level is `standard` or `deep`.

Verify in both directions:

1. **Coverage check**: Trace every protected proposition from the source to an appropriate location in the revision.
2. **Entitlement check**: Trace every sentence in the revision to a necessary rhetorical or evidentiary function.
3. **Redundancy check**: Confirm that each repeated proposition serves a distinct purpose.
4. **Placement check**: Read each section without the change log and confirm that information arrives where the reader needs it.
5. **Emphasis check**: Inspect high-emphasis positions for disproportionate caveats, secondary detail, unsupported novelty, or hidden boundaries.
6. **Formal-unit check**: Confirm that every retained equation performs a necessary technical function, is introduced and used, and remains semantically and structurally traceable.

Deliver the complete ledger only when the user requests it. Otherwise report changed, deleted, moved, high-risk, and unresolved units with concise reasons.

## Worked Case

Source sentence in an abstract:

`本文的验证仅采用离线数值仿真，尚未开展实体平台试验。`

Audit:

| Gate | Decision |
|---|---|
| Evidence | The statement may be true and must be checked against the manuscript |
| Function | It defines the validation boundary |
| Necessity | The boundary is necessary; this exact sentence is not necessarily necessary |
| Placement | The evaluation setting belongs in the abstract; the fuller limitation usually belongs in discussion |
| Emphasis | As an abstract-ending negative statement, it may overemphasize the limitation unless it is central to the paper's claim |
| Disposition | Primary `rewrite` in the abstract; record a linked `move` or distinct restatement of the protected limitation in discussion |

Possible allocation, using only facts present in the manuscript:

- Abstract: `在数值模型上的离线实验表明，……`
- Discussion: `本研究的验证范围限于离线数值实验，尚未开展实体平台验证，因此不对实际系统中的实时性与鲁棒性作进一步推断。`

Do not apply this allocation mechanically. If the paper claims physical deployment readiness, the lack of physical validation directly constrains the main claim and may require explicit abstract-level qualification.
