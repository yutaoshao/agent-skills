# Reviewer Guidelines

Understanding how reviewers evaluate papers helps authors write stronger submissions. This reference covers evaluation dimensions, scoring systems, common concerns, and rebuttal strategies for major CS/ML/AI venues.

---

## 4 Evaluation Dimensions

Most ML/AI venues evaluate papers on four core dimensions:

### 1. Quality (Soundness)

Is the paper technically sound? Are the claims well-supported?

- Are the experiments well-designed and fairly compared?
- Are the proofs correct (if applicable)?
- Are the baselines appropriate and up-to-date?
- Are the conclusions supported by the evidence?
- Are there significant flaws in the methodology?

### 2. Clarity

Is the paper well-written and easy to follow?

- Can a knowledgeable reader understand the paper in one pass?
- Is the notation consistent and clearly defined?
- Are the figures and tables informative and well-designed?
- Is the paper well-organized with a logical flow?
- Are the contributions clearly stated?

### 3. Significance

Does the paper make an important contribution?

- Does the paper address a meaningful problem?
- Are the results likely to be used or built upon by others?
- Does the work open new research directions?
- Is the contribution substantial enough for the venue?

### 4. Originality (Novelty)

Is the paper sufficiently novel?

- Does the paper present new ideas, methods, or results?
- Is the paper clearly differentiated from prior work?
- Does it provide new insights, even if the technique is not entirely new?
- Is the related work discussion thorough enough to establish novelty?

---

## NeurIPS Scoring System

NeurIPS uses a 1-10 scale for overall assessment:

| Score | Label | Description |
|-------|-------|-------------|
| 10 | Top 5% of accepted papers | Seminal, groundbreaking work |
| 8 | Top 15% of accepted papers | Strong accept, clear contribution |
| 6 | Marginally above acceptance threshold | Weak accept, some concerns but overall positive |
| 5 | Marginally below acceptance threshold | Borderline, could go either way |
| 4 | Below acceptance threshold | Weak reject, notable concerns |
| 3 | Clear reject | Significant issues in quality, clarity, or novelty |
| 1 | Trivial, wrong, or already published | Strong reject |

### Confidence Scale (NeurIPS)

| Score | Description |
|-------|-------------|
| 5 | Absolutely certain. Reviewer has published extensively on this exact topic. |
| 4 | Confident. Reviewer is very familiar with the area. |
| 3 | Fairly confident. Reviewer knows the area but may have missed some related work. |
| 2 | Willing to defend the evaluation but not absolutely certain. |
| 1 | Not confident. An educated guess. |

---

## ICML Review Structure

ICML reviewers are asked to provide:

1. **Summary** (3-5 sentences): What the paper does and claims
2. **Strengths** (bullet list): What the paper does well
3. **Weaknesses** (bullet list): Concerns and issues
4. **Questions** (bullet list): Clarifications needed from authors
5. **Limitations** (1-2 sentences): Did the authors adequately discuss limitations?
6. **Ethics** (1-2 sentences): Any ethical concerns?
7. **Overall Score**: 1-10 scale similar to NeurIPS
8. **Confidence**: 1-5 scale

### What ICML Reviewers Emphasize

- Reproducibility: Can results be reproduced from the paper alone?
- Baselines: Are comparisons fair and up-to-date?
- Statistical rigor: Are error bars and significance tests included?
- Writing quality: Is the paper clear and well-organized?

---

## ICLR OpenReview Process

ICLR uses a fully open review process on OpenReview:

### Review Timeline
1. Papers submitted and publicly visible
2. Reviews posted (publicly visible with reviewer identity hidden)
3. Author response period (typically 1-2 weeks)
4. Reviewer-author discussion period
5. Reviewers update scores based on discussion
6. Area Chair meta-review and decision

### ICLR Scoring

| Score | Label |
|-------|-------|
| 8 | Strong Accept |
| 6 | Weak Accept |
| 5 | Borderline |
| 3 | Weak Reject |
| 1 | Strong Reject |

### Key Difference from Other Venues

- Reviews are public (but anonymized)
- Authors can engage in multi-round discussion with reviewers
- Other researchers can post comments
- Reviewers can and do change scores based on rebuttals

---

## ACL Reviewer Guidelines

ACL reviewers evaluate papers on:

1. **Appropriateness**: Does the paper fit the venue?
2. **Clarity**: Is it well-written?
3. **Originality**: Is it novel?
4. **Soundness**: Is the methodology correct?
5. **Meaningful comparison**: Are baselines appropriate?
6. **Substance**: Is there enough content?
7. **Replicability**: Can results be reproduced?
8. **Overall recommendation**: Accept/Reject with confidence

### ACL-Specific Emphasis

- **Linguistic insight**: Does the paper provide insight about language, not just numbers?
- **Evaluation rigor**: Multiple evaluation methods beyond just automatic metrics
- **Multilinguality**: Is the work limited to English? Is this acknowledged?
- **Limitations section**: Mandatory. Reviewers explicitly check for it.
- **Responsible NLP**: Are societal impacts discussed?

---

## Common Reviewer Concerns and Pre-Emption Strategies

### Concern 1: Weak Baselines

**Reviewer complaint**: "The paper only compares against methods from 2018. Recent methods X and Y (2024) are missing."

**Pre-emption**:
- Include at least 2-3 baselines from the last 2 years
- If a well-known recent method is excluded, explain why (different problem setting, different modality, etc.)
- Check papers accepted at the last 2 editions of the target venue for recent baselines

### Concern 2: Missing Ablations

**Reviewer complaint**: "It is unclear which component of the proposed method contributes to the improvement."

**Pre-emption**:
- Include an ablation study removing each major component one at a time
- Show results for: full model, model without component A, without B, without C
- Discuss which components matter most and why

### Concern 3: No Error Bars

**Reviewer complaint**: "Results are reported for a single run. Without error bars, it is impossible to judge significance."

**Pre-emption**:
- Run experiments with at least 3 different random seeds (5 preferred)
- Report mean and standard deviation
- For close comparisons, include a statistical significance test (paired t-test, bootstrap)

### Concern 4: Hard to Follow

**Reviewer complaint**: "The paper is difficult to follow. The notation is inconsistent and the method section jumps between topics."

**Pre-emption**:
- Follow the Gopen & Swan 7 Principles (see `references/writing-philosophy.md`)
- Include a notation table
- Use a "road map" paragraph at the start of complex sections
- Have someone outside your group read the paper before submission

### Concern 5: Incremental Contribution

**Reviewer complaint**: "The contribution is incremental. The paper combines existing techniques X and Y without significant new insight."

**Pre-emption**:
- Clearly articulate why the combination is non-trivial
- Show that naive combinations of X and Y do not work (include negative results)
- Provide analysis or theory explaining why your specific combination succeeds
- Demonstrate results that could not be achieved by X or Y alone

### Concern 6: Narrow Evaluation

**Reviewer complaint**: "The method is only evaluated on one dataset / one task / one domain."

**Pre-emption**:
- Evaluate on at least 2-3 datasets
- Include at least one "out-of-distribution" or "transfer" evaluation
- If the method is domain-specific, acknowledge this and explain why broader evaluation is not applicable

### Concern 7: Overclaiming

**Reviewer complaint**: "The paper claims 'state-of-the-art' but only compares against 3 methods on 1 dataset."

**Pre-emption**:
- Make claims proportional to evidence
- Use hedged language when appropriate: "competitive with" rather than "state-of-the-art"
- Be explicit about the scope of claims: "the best among methods that do not use additional data"

### Concern 8: Missing Related Work

**Reviewer complaint**: "The paper fails to discuss closely related work X, creating a misleading impression of novelty."

**Pre-emption**:
- Thoroughly search for related work (use Semantic Scholar, Google Scholar, venue proceedings)
- Ask colleagues in the area if you have missed anything
- Discuss the most similar work explicitly, explaining how your approach differs

---

## Rebuttal Best Practices

### General Principles

1. **Be professional**: Never be defensive or dismissive. Thank reviewers for their time.
2. **Be concise**: Rebuttals have strict word/page limits. Prioritize the most important concerns.
3. **Be specific**: Reference exact sections, tables, and figures. Include new results if possible.
4. **Prioritize**: Address the concerns that could change the outcome. Do not spend space on minor points.
5. **Acknowledge valid concerns**: If a reviewer found a real problem, acknowledge it and describe how you will fix it.

### Rebuttal Template

```markdown
We thank all reviewers for their thoughtful feedback. We address the main concerns below.

## Response to Reviewer [X]

**[Concern 1, quoted or paraphrased]**

[Your response. Be specific. Include new results, table numbers, or figure references.]

**[Concern 2]**

[Response.]

## Response to Reviewer [Y]

...

## Summary of Changes

- [Change 1]: [Description] (Section X, page Y)
- [Change 2]: [Description] (new Table Z in appendix)
- ...
```

### What Makes Rebuttals Succeed

| Effective | Ineffective |
|-----------|-------------|
| New experiments addressing specific concerns | "We will add this in the final version" with no results |
| Pointing to existing content the reviewer may have missed | "The reviewer did not read our paper carefully" |
| Acknowledging limitations and explaining their impact | Denying that limitations exist |
| Clear, structured formatting | Wall of text without clear per-reviewer organization |

---

## Dennett's Review Rules (for Self-Review)

Philosopher Daniel Dennett proposed rules for constructive criticism. Apply these when self-reviewing your paper:

1. **Re-express**: Can you re-state the paper's contribution so clearly that the author says "I wish I had put it that way"? If not, the paper's framing may need work.

2. **List agreements**: Before criticizing, list what the paper does well. This helps identify which parts to preserve during revision.

3. **Mention what you learned**: Did writing this paper reveal something new? If not, the contribution may be unclear.

4. **Only then criticize**: After steps 1-3, identify weaknesses. This ensures criticisms are constructive and specific.

### Self-Review Simulation

Before submission, simulate a hostile reviewer by asking:

- What is the weakest experiment in the paper?
- Which claim has the least evidence?
- What is the most closely related work I might have missed?
- If I wanted to reject this paper, what reason would I give?
- Is there an obvious follow-up experiment that I should have included?

Answer these questions honestly and address the issues before submission.
