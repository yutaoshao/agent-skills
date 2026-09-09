# Evidence Review Guide

Use this guide for figures, tables, manuscript reviews, and submission preparation.

## Claim-to-Evidence Check

For each material contribution or result, identify the exact evidence that warrants it: a derivation, dataset, configuration, run record, source file, figure, table, or cited work. Check that the manuscript's wording does not exceed the evidence's scope.

| Manuscript claim | Evidence source | Transformation or comparison | Status | Finding |
|---|---|---|---|---|

## Numerical Tables and Figures

Trace numerical values to the source record and account for aggregation, units, random seeds, confidence intervals, and rounding when applicable. Check the caption, labels, legend, text discussion, and emphasis formatting against the values shown. Report a mismatch with its exact displayed location and expected value; do not silently repair a result whose provenance is unclear.

## Review Findings

Report findings in descending practical severity:

- `Blocking`: the build fails, a claim lacks its stated evidence, a result disagrees with its source, required venue material is missing, or anonymization is compromised.
- `Important`: a reader cannot reliably interpret or reproduce a material method or result, or a citation/visual/notation inconsistency changes understanding.
- `Improvement`: clarity, ordering, or presentation can improve without changing the scientific claim.

For each finding, include its location, the supporting evidence, and a proposed repair. Verify venue requirements against current official sources rather than a static checklist.
