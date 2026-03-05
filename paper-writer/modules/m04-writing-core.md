# Module 04: Writing Core

Section-by-section paper drafting with integrated writing philosophy. This module produces a complete paper draft by applying established academic writing principles at every level, from section structure down to individual word choice.

## When to Load

Load this module when the user says: "write", "draft", "introduction", "methods", "experiments", "abstract", "conclusion", or when executing Stage S4 of a full paper writing project.

## Prerequisites

- Confirmed paper outline from Module 03 (`plan/outline.md`)
- Literature review and references from Module 02
- Code artifact mapping from Module 01
- Load `references/writing-philosophy.md` alongside this module (if available)

## Section-by-Section Drafting Procedures

### Abstract

The abstract is the most-read part of the paper. It appears in search results, review assignments, and proceedings. Every word must earn its place.

**The 5-Sentence Formula** (adapted from Tom Farquhar):

| Sentence | Purpose | Template |
|---|---|---|
| 1. Achievement | What did you accomplish? | "We present [method name], a [type] that [key capability]." |
| 2. Difficulty | Why is this hard? What makes existing approaches insufficient? | "[Problem] remains challenging because [specific difficulty]." |
| 3. Approach | How did you do it? Core technical idea. | "[Method name] addresses this by [key technical insight], enabling [capability]." |
| 4. Evidence | What are the results? Specific numbers. | "On [benchmark], [method] achieves [metric value], outperforming [baseline] by [margin]." |
| 5. Significance | Why does this matter? Remarkable result or implication. | "This demonstrates that [broader insight], opening [new possibility]." |

**Abstract rules:**
- Delete generic openings: "In recent years, X has attracted significant attention" adds zero information. Start with the contribution.
- Include specific numbers: "achieves 95.3% accuracy" not "achieves competitive performance."
- No citations in the abstract (violates most style guides).
- No undefined abbreviations. Define or spell out every abbreviation.
- Length: 150-250 words for conferences, check journal guidelines for specific limits.
- Write the abstract LAST (after all other sections), even though it appears first.

**Procedure:**
1. Read the completed Introduction and Experiments sections.
2. Draft using the 5-sentence formula.
3. Check: does every sentence add information not present in the previous one?
4. Check: could a reader understand the contribution from the abstract alone?
5. Trim to target word count. Cut adjectives and adverbs first.

### Introduction

The introduction must accomplish four things in 1-1.5 pages: establish the problem, motivate the reader, present the contribution, and preview the results.

**Structure (4-paragraph model):**

| Paragraph | Content | Length |
|---|---|---|
| 1. Context + Problem | What is the problem? Why does it matter? Who cares? Ground it in a real-world need or scientific question. | 4-6 sentences |
| 2. Gap + Motivation | What do existing approaches do? Where do they fall short? What specific limitation motivates this work? | 4-6 sentences |
| 3. Contribution | What does this paper propose? How does it work (high-level)? What are the specific contributions (2-4 bullets)? | 5-8 sentences including bullets |
| 4. Results Preview + Organization | What are the key results (numbers)? How is the paper organized? | 3-5 sentences |

**Introduction rules:**
- The reader should reach the Methods section by page 2-3 at the latest. If the Introduction bleeds onto page 3, it is too long.
- Contribution bullets: each bullet is a single, specific, verifiable claim. "We achieve X% on benchmark Y" not "We achieve strong results."
- Do NOT list contributions that are standard engineering. "We release our code" is not a contribution unless the code itself is the contribution.
- End paragraph 2 with the specific gap: "However, no existing method achieves [X] while maintaining [Y]."
- Paragraph 3 should name the method and state its key insight in one sentence before the bullet list.

**Procedure:**
1. Write paragraph 2 first (the gap). This is the hardest and most important.
2. Write paragraph 1 (context that leads to the gap).
3. Write paragraph 3 (contribution that fills the gap).
4. Write paragraph 4 (evidence and organization).
5. Read paragraphs 1-4 in sequence. Does each paragraph logically necessitate the next?

### Methods

The Methods section must enable reimplementation. A reader with the paper and no access to the code should be able to reproduce the method.

**Structure:**

```
3. Methods
   3.1 Problem Formulation
       - Define all inputs, outputs, and the optimization objective
       - Introduce notation that will be used throughout
       - State assumptions explicitly
   3.2 [Core Component 1]
       - Conceptual explanation (what it does and why)
       - Mathematical formulation (how it works formally)
       - Key design choices (why this specific approach)
   3.3 [Core Component 2]
       - Same structure as 3.2
   3.4 Training / Optimization Details
       - Loss functions with full mathematical definitions
       - Training algorithm (pseudocode if non-trivial)
       - Key hyperparameters and how they were selected
```

**Methods rules:**
- Present the FINAL design, not the research journey. Do not write "first we tried A, then B, then C." Just present C. Ablations in the Experiments section justify the design choices.
- Every equation should be preceded by a sentence explaining what it computes and why, and followed by a sentence explaining the key variables.
- Include pseudocode for non-trivial algorithms. Pseudocode is more readable than equations for procedural methods.
- State all hyperparameters. If a hyperparameter is set by cross-validation, say so. If it is fixed, explain why that value.
- Assumptions must be stated formally, not hidden in prose. "We assume the robot has N revolute joints" not "our robot has several joints."

**Procedure:**
1. Start with Section 3.1 (Problem Formulation). Define notation.
2. Draft each subsection by reading the corresponding code files (from artifact mapping).
3. For each code component, extract: input/output types, algorithm logic, key parameters.
4. Write the conceptual explanation first, then the math, then the design justification.
5. Add pseudocode for any algorithm longer than 5 steps.
6. Review: could a graduate student reimplement this from the paper alone?

### Experiments

The Experiments section provides evidence for every claim made in the Introduction.

**Structure:**

```
4. Experiments
   4.1 Experimental Setup
       - Datasets (with citations, sizes, splits, preprocessing)
       - Baselines (with citations, implementation details, fairness of comparison)
       - Evaluation metrics (with definitions or citations)
       - Implementation details (hardware, software, training time)
   4.2 Main Results
       - Table 1: Comprehensive comparison with baselines
       - Explicit statement of the claim each result supports
       - Statistical significance where applicable
   4.3 Ablation Studies
       - Table 2: Component-wise analysis
       - Each row removes/changes one component to measure its impact
       - Connects back to design decisions in Methods
   4.4 Analysis / Qualitative Results
       - Figure: Visualization of method behavior
       - Discussion of when/why the method succeeds or fails
       - Edge cases and failure modes
```

**Experiments rules:**
- **Explicit claim connections**: Every table and figure must be tied to a specific claim. "Table 1 demonstrates Contribution 1: [method] outperforms all baselines on [metric]." If a result does not support a contribution, either the result or the contribution list needs revision.
- **Error bars and methodology**: Report standard deviation over multiple runs (minimum 3, preferably 5). State the random seeds or methodology for variance estimation. If deterministic, state that.
- **Compute resources**: Document GPU type, training time, and inference time. This is increasingly required for reproducibility and is mandatory at NeurIPS.
- **Fair comparisons**: Use the same data splits, preprocessing, and evaluation protocol for all methods. If re-running baselines, explain why and how. If using published numbers, cite the source.
- **Ablation design**: Each ablation should test one hypothesis. The full method should always be included as a row for reference.

**Procedure:**
1. Start with Section 4.1 (Setup). Extract details from config files and training scripts.
2. Draft Table 1 from result files. Verify all numbers against source data (cross-reference Module 05).
3. Write the narrative for Section 4.2. For each row of Table 1, explain what it shows.
4. Draft ablation table from ablation result files.
5. Write Section 4.3 connecting ablations to design choices from Methods.
6. Select the most informative qualitative results for Section 4.4.
7. Review: does every Introduction claim have supporting evidence in this section?

### Related Work

The Related Work section positions this paper within the research landscape. It should be written as a synthesized narrative, drawing from the literature review (Module 02).

**Rules:**
- Organize methodologically, not paper-by-paper. Group papers by their approach family, not by individual paper.
- Cite generously. Under-citing frustrates reviewers. Aim for 5-15 citations per page of Related Work.
- End each thematic paragraph with the limitation that motivates the next paragraph or our work.
- Place Related Work before Methods (standard in ML venues) or after Methods (common in NLP, some journals). Follow venue convention.
- Be fair. Do not misrepresent competitors. Acknowledge their strengths before discussing limitations.

**Procedure:**
1. Import the draft from Module 02 Step 6.
2. Revise to match the final contribution framing from Module 03.
3. Ensure every theme connects to the final positioning paragraph.
4. Verify all citations are in `references.bib`.

### Limitations

Every major ML/AI conference now requires or strongly encourages an explicit Limitations section.

**Rules:**
- Be honest. Reviewers respect candor and penalize evasion.
- Distinguish between inherent limitations (fundamental to the approach) and current limitations (addressable with more engineering/data).
- Do not preemptively solve the limitations in this section (that belongs in Future Work or the next paper).
- 3-5 specific limitations is typical. Each should be 2-4 sentences.

**Template:**
```latex
\section{Limitations}

Our approach has several limitations that suggest directions for future work.
[Limitation 1: scope restriction.] [Limitation 2: computational cost.]
[Limitation 3: assumption that may not hold in all settings.]
[Limitation 4: evaluation gap -- what was not tested.]
```

### Conclusion

The Conclusion crystallizes the key insight and looks forward.

**Rules:**
- Do NOT start with "In this paper, we proposed..." This is the most generic, uninformative opening possible.
- Start with the key insight or the most important takeaway. What should the reader remember a month from now?
- Briefly restate the main result (1-2 sentences).
- Discuss 1-2 promising future directions with reasoning (not a laundry list).
- Length: 0.5-0.75 pages for conferences, up to 1 page for journals.

**Template:**
```latex
\section{Conclusion}

[Key insight: one sentence capturing the core lesson.]
[Method summary: one sentence naming the approach and its core idea.]
[Result summary: one sentence with the most impressive number.]
[Future direction 1: what is the most promising next step and why.]
[Future direction 2: optional, if a second direction is clearly motivated.]
```

## Writing Philosophy: Sentence-Level Clarity

Apply these principles during drafting and revision to produce clear, professional academic prose.

### Gopen and Swan: 7 Principles of Reader Expectation

These principles are based on how readers process English sentences. Violating them forces the reader to re-read, which degrades comprehension.

| Principle | Rule | Example |
|---|---|---|
| 1. Subject-Verb Proximity | Keep the grammatical subject and main verb close together. Do not separate them with long parenthetical clauses. | BAD: "The method, which builds on prior work by Smith et al. (2020) and extends the framework of Jones (2019) with several key modifications including attention-based pooling and multi-scale feature extraction, achieves state-of-the-art results." GOOD: "The method achieves state-of-the-art results by extending the framework of Jones (2019) with attention-based pooling and multi-scale feature extraction." |
| 2. Stress Position | Place the most important information at the end of the sentence, where the reader's attention naturally falls. | BAD: "State-of-the-art accuracy is achieved by our method on three benchmarks." GOOD: "Our method achieves state-of-the-art accuracy on three benchmarks." |
| 3. Topic Position | Place familiar or contextualizing information at the beginning of the sentence (the topic position). | BAD: "A 3.2% improvement over the previous best is observed when comparing our method." GOOD: "Compared to the previous best method, ours improves accuracy by 3.2%." |
| 4. Old Before New | Start each sentence with information the reader already knows, then introduce new information. This creates a chain of understanding. | "We train using a WTA loss (old). This loss encourages diversity among hypotheses (new). The resulting diversity enables the PSO to explore a broader solution space (newer)." |
| 5. One Unit, One Function | Each sentence or clause should serve one purpose. Do not pack multiple ideas into a single sentence. | BAD: "We use a ResNet backbone with 50 layers that achieves 95% accuracy and runs at 30fps while being easy to deploy." GOOD: "We use a ResNet-50 backbone. This architecture achieves 95% accuracy at 30fps inference speed." |
| 6. Action in Verb | Express the action of the sentence in the main verb, not in a nominalization. | BAD: "The optimization of the network is performed by Adam." GOOD: "Adam optimizes the network." |
| 7. Context Before New | Provide the reader with context or framing before presenting new, unexpected information. | BAD: "Our method fails completely on transparent objects." GOOD: "When applied to transparent objects, which violate the Lambertian surface assumption, our method fails to produce reliable depth estimates." |

### Micro-Level Writing Tips (from Perez)

Apply these during sentence-level revision:

| Tip | Action |
|---|---|
| Minimize pronouns | Replace "it", "this", "they" with the specific noun when any ambiguity exists. "This approach" not "This". "The loss function" not "It". |
| Verbs early | Move the main verb closer to the beginning of the sentence. Readers process meaning at the verb. |
| Unfold apostrophes | "the network's output" becomes "the output of the network" when the possessive creates ambiguity about which noun is the subject. |
| Delete filler words | Remove: "very", "really", "quite", "rather", "somewhat", "basically", "essentially", "actually", "in fact", "it turns out that". |
| One idea per sentence | If a sentence contains "and" connecting two independent ideas, consider splitting into two sentences. |
| Parallel structure | Lists and series should use identical grammatical structure. "We (1) design a network, (2) train it with WTA loss, and (3) refine predictions with PSO." |

### Word Choice (from Lipton)

| Principle | Action |
|---|---|
| Be specific | "ResNet-50" not "a deep neural network." "3.2% accuracy improvement" not "significant improvement." |
| Eliminate hedging | Remove "seems to", "appears to", "might", "could potentially" when the evidence is clear. If the evidence is unclear, say so directly instead of hedging. |
| Avoid incremental vocabulary | "We propose" not "we propose a novel approach." If it is in the paper, the reader already assumes it is novel. |
| Delete intensifiers | Remove "very", "highly", "extremely", "significantly" (when not statistical). Let the numbers speak. |
| Prefer active voice | "We train the model" not "The model is trained." Active voice is shorter, clearer, and more engaging. |
| Avoid "interesting" | If a result is interesting, explain WHY it is interesting. The word itself carries no information. |

### Precision (from Steinhardt)

| Principle | Action |
|---|---|
| Consistent terminology | Choose one term for each concept and use it throughout. Do not alternate between "model", "network", "architecture", and "system" for the same thing unless distinguishing different aspects. |
| State assumptions formally | "We assume the manipulator has $N$ revolute joints with known DH parameters" not "we consider a general robot arm." |
| Define before use | Every symbol, abbreviation, and technical term must be defined before or at first use. |
| Quantify claims | "Reduces training time by 40%" not "substantially reduces training time." |

## Section Drafting Order

The optimal drafting order is NOT the reading order. Draft sections in this order for maximum efficiency:

| Order | Section | Reason |
|---|---|---|
| 1 | Methods | You know the method best. Start here to establish notation and terminology. |
| 2 | Experiments - Setup | Captures implementation details while they are fresh. |
| 3 | Experiments - Results | Present the evidence. This often reveals which contributions are strongest. |
| 4 | Introduction | Now that you know the full story and evidence, you can write a compelling introduction. |
| 5 | Related Work | With the contribution clearly defined, you can position it precisely. |
| 6 | Limitations + Conclusion | Reflect on what was achieved and what remains. |
| 7 | Abstract | Distill the entire paper into 150-250 words. Write this last. |

## Deliverables

Upon completing this module:

1. **Complete paper draft** (`.tex` file) with all sections written:
   - Abstract (5-sentence formula)
   - Introduction (4-paragraph model)
   - Related Work (synthesized, thematic)
   - Methods (reimplementable)
   - Experiments (Setup, Results, Ablations, Analysis)
   - Limitations
   - Conclusion
2. **All placeholders clearly marked:**
   - `[CITATION NEEDED]` for unverified citations
   - `[TODO: figure X]` for missing figures
   - `[VERIFY: number]` for unverified results
3. **`plan/progress.md`** updated with:
   - S4 Writing Core: COMPLETE
   - Section completion status
   - Outstanding issues (missing figures, unverified citations, sections needing user input)
   - Next action: proceed to S5 (Figures & Tables)

## Common Pitfalls

- **Pitfall:** Writing the Abstract first. The abstract should be the last section drafted because it summarizes the entire paper. Writing it first leads to misalignment between the abstract and the actual content.
- **Pitfall:** Methods section that describes the research journey instead of the final method. Do not write "first we tried X, which did not work, so we tried Y." Present Y as the method. Use ablations to justify removing X.
- **Pitfall:** Experiments without explicit claim connections. Every figure and table must be tied back to a specific claim from the Introduction. If a result does not support a claim, either the result or the claim list needs revision.
- **Pitfall:** Introduction longer than 1.5 pages. A long introduction signals inability to identify the core message. Be ruthless about cutting context that does not directly support the gap-contribution narrative.
- **Pitfall:** Using AI-pattern language. Avoid "Furthermore," "Moreover," "Notably," "leverage," "harness," "comprehensive," "novel." See Module 07 and `references/de-ai-patterns.md` for the full list. These patterns are detectable by reviewers and AI-detection tools.
