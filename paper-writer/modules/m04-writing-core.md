# English Section Drafting

Use this module to draft or substantially rewrite an English CS/ML/AI paper section. Read the surrounding text, target-template constraints, and evidence that supports the section before writing. Preserve technical meaning, equations, citations, notation, and numerical values unless an intentional correction is requested.

## Establish the Section's Job

Before drafting, identify the reader question, the claim the section may support, and the evidence that warrants it. Make the section answer that question directly. Separate facts, observed results, interpretations, and limits when they have different evidentiary status. Read [writing-philosophy.md](../references/writing-philosophy.md) for paragraph and sentence-level organization guidance.

## Abstract

Give a self-contained account of the problem or setting, the missing capability or difficulty, the technical idea, and the strongest supported result or implication. Include quantitative evidence only when the reported value, comparison, and evaluation setting are known. Define abbreviations that a general venue reader may not know. Select length and internal order from the venue and available evidence; omit any element that cannot be supported rather than filling it with generic claims.

## Introduction

Lead the reader from the consequential problem to a specific, evidence-grounded gap. Explain what existing approaches achieve in the relevant setting and why their limitation matters here. Present the paper's mechanism at a level that makes the claimed difference intelligible, then state contributions as precise, testable claims when this improves readability. Use cited related work and the paper's own evidence to keep the positioning fair. The introduction should make the experiments feel necessary rather than append a list of results.

## Method

Define the task interface before the mechanism: inputs, outputs, objective, assumptions, and any constraint that changes the setting. Introduce each component by its role, explain how it connects to the preceding component, then give the mathematical or algorithmic specification needed to implement it. Explain symbols near first use and account for key design choices, including what a component enables or trades off. Present the final method rather than an unstructured account of development history; use experiments or ablations to assess alternatives.

## Experiments and Results

Organize experiments around questions that test the paper's claims, such as comparative effectiveness, contribution of a component, robustness across conditions, efficiency, or a stated boundary. For each question, make the protocol recoverable: datasets or task instances, splits, metrics, baselines, implementation conditions, and statistical treatment where applicable. Report results with their comparison context, variation or uncertainty when available, and a direct interpretation that does not exceed the measurement. Distinguish a planned experiment from a completed result.

## Discussion, Limitations, and Conclusion

Use discussion to explain observations that matter to the central claim: what pattern occurred, what mechanism or constraint may account for it, and how far the evidence permits that explanation to go. State material limitations plainly, including conditions where the method or conclusion does not apply. Conclude by restating the supported contribution and its implication; do not introduce a new claim or turn future work into evidence for the paper.
