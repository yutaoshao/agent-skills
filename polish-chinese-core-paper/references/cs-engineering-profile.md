# Computer Science and Engineering Profile

Use this profile as rhetorical and evidentiary guidance for computer science and engineering manuscripts. Do not treat it as a journal format or impose it when the target journal specifies a different structure.

## Contribution Chain

Keep the manuscript's core chain explicit and consistent:

```text
practical or scientific problem
-> limitation of existing approaches
-> proposed technical idea
-> implementation or analytical method
-> evaluation design
-> measured evidence
-> bounded conclusion
```

Flag a break in the chain instead of filling it with invented content. Common breaks include an introduction that promises robustness without a robustness test, an abstract that reports gains absent from the results, and a conclusion that generalizes beyond the tested datasets.

## Title and Abstract

- Name the research object and technical contribution precisely; remove generic claims such as “研究与实现” when they add no scope.
- Keep the abstract self-contained according to the target journal's rules.
- Express the problem, method, evaluation setting, principal evidence, and bounded conclusion when the manuscript supplies them.
- Distinguish the evaluation setting from a limitation statement. Name a simulation, benchmark, prototype, or physical platform directly; do not use an audit-style negative sentence unless the absence itself is essential to interpreting the claim.
- Preserve exact metric names and comparison conditions.
- Include quantitative results only when they appear in the verified body or source data.
- Avoid citations, undefined abbreviations, equations, and unsupported novelty claims unless the target journal permits or requires them.

## Evidence-Boundary Placement

- Keep the evaluation setting visible in the abstract whenever it limits the reported evidence.
- State missing physical, field, online, longitudinal, or external validation explicitly in the discussion or limitations section when it constrains applicability.
- Qualify the abstract explicitly when the missing validation directly conflicts with a deployment, real-time, robustness, safety, or generalization claim.
- Do not infer real-system performance from simulation results, or empirical mechanism from an observed performance difference.
- Avoid repeating the same boundary sentence in the abstract, discussion, and conclusion. Use each location for a distinct purpose: scope the evidence, interpret the limitation, and motivate grounded next work.

## Introduction

- Move from the concrete problem to the unresolved technical limitation.
- Describe related limitations fairly; do not create a weak straw-man baseline to strengthen the proposed method.
- State the research gap separately from the proposed solution.
- Make each claimed contribution testable against a method section, result, analysis, or released artifact.
- Keep contribution lists only when the journal permits them and the items are genuinely parallel.

## Methods

Check whether the prose makes these items recoverable where relevant:

- input, output, symbols, and assumptions;
- system boundary and operating conditions;
- architecture or algorithm stages and their dependencies;
- objective functions, constraints, and parameter meanings;
- training, optimization, simulation, or experimental procedure;
- computational complexity, hardware, software, and implementation details needed for interpretation;
- differences from cited baselines or prior versions.

Do not repair missing reproducibility details by guessing common defaults. Raise specific author queries.

## Experiments and Results

- Keep dataset versions, sampling, train/validation/test splits, preprocessing, and exclusion rules precise.
- Ensure baselines, metrics, hyperparameters, and evaluation protocols are comparable.
- Tie every “better” claim to a baseline, metric, condition, and value.
- Distinguish absolute improvement, relative improvement, and percentage-point change.
- Reserve statistical “显著” for an identified test and threshold.
- Connect ablation, sensitivity, robustness, efficiency, and error analyses to the claims they are intended to support.
- Preserve negative and mixed results; interpret them rather than deleting them for narrative smoothness.

## Discussion and Conclusion

- Interpret why the evidence supports the stated contribution rather than restating every result.
- Compare findings with relevant prior work without citation dumping.
- Separate empirical explanation from demonstrated mechanism.
- State limitations in terms of affected populations, conditions, datasets, resources, or deployment settings.
- Preserve necessary validation boundaries while choosing a location and emphasis proportionate to their effect on the paper's main claim.
- Keep future work grounded in unresolved limitations, not a generic list of possible extensions.
- End at the generality supported by the evaluated conditions.

## Terminology and Notation

- Use one Chinese term for each concept unless a distinction is intentional.
- Define an English abbreviation at first use and apply it consistently thereafter.
- Give each displayed equation a necessary modeling, derivation, constraint, definition, or evidentiary role; query equations that are repeated, unused, or disconnected from the method and results.
- Introduce an equation before or with its first use, then explain the nonstandard symbols, assumptions, conditions, inputs, and outputs needed to reproduce the reasoning.
- Use one symbol for one meaning, and keep operators, subscripts, superscripts, index ranges, dimensions, vector and matrix styles, and equation references consistent.
- Do not collapse a necessary derivation into a result-only formula or expand a standard identity into decorative steps merely to change manuscript length.
- Preserve official dataset, method, product, protocol, and standard names.
- Follow the verified journal rules for quantities, units, punctuation, capitalization, and Chinese-English spacing.

## Claim-to-Evidence Audit

Use this table for `standard` and `deep` reviews:

| Claim | Location | Required evidence | Available evidence | Status | Action |
|---|---|---|---|---|---|
| | | experiment / analysis / citation / derivation | | supported / partial / missing | |

Do not rewrite `partial` or `missing` claims as supported. Narrow the language with author approval or request the missing evidence.
