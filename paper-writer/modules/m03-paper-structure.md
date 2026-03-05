# Module 03: Paper Structure

Define the contribution precisely and generate a complete paper outline. This module bridges the gap between "we know what the project does" (Module 01) and "we write the paper" (Module 04) by establishing the narrative backbone.

## When to Load

Load this module when the user says: "outline", "structure", "plan paper", "organize", "paper skeleton", or when executing Stage S3 of a full paper writing project.

## Prerequisites

- Confirmed contribution hypothesis from Module 01
- Initial literature scan (from Module 01 Step 5 or Module 02)
- Target venue identified (determines page limits and structure)

## Procedure

### Step 1: Define the One-Sentence Contribution

The entire paper exists to communicate one core contribution. Everything else is supporting material.

**Actions:**

1. Draft the one-sentence contribution statement. It must:
   - Be a single grammatical sentence (no semicolons joining independent clauses)
   - State WHAT the contribution is (a method, a result, an analysis)
   - State WHY it matters (the problem it solves or the gap it fills)
   - Be falsifiable (a reader could, in principle, disagree with it)

2. Test the statement against three criteria:
   - **Specificity**: Could this sentence describe another paper? If yes, it is too vague. Add differentiating details.
   - **Completeness**: Does it capture the full contribution? If reading only this sentence, would a researcher understand what is new?
   - **Honesty**: Does the claim match what the experiments actually show? Do not overstate.

3. **Present to the user for confirmation.** Do NOT proceed without explicit user approval.

**Examples of good one-sentence contributions:**
```
GOOD: "We propose HyperIK, a multi-hypothesis neural network trained with winner-takes-all loss and refined by particle swarm optimization, that solves inverse kinematics for redundant manipulators in real time with sub-millimeter precision."

BAD: "We propose a novel deep learning approach for robot control." (too vague, could be any paper)

BAD: "We achieve state-of-the-art results on inverse kinematics benchmarks." (says nothing about how or why)
```

4. Record the confirmed statement in `plan/outline.md` at the top.

### Step 2: Apply the Narrative Principle

Every paper tells a story. Structure that story using the What/Why/So What framework (adapted from Neel Nanda's writing advice for ML papers).

**The Narrative Principle:**

| Element | Question | Paper Location | Length Guidance |
|---|---|---|---|
| **WHAT** | What did you do? What is the method/finding? | Abstract (sentence 1-2), Introduction (contribution bullets), Methods | State concisely upfront, detail in Methods |
| **WHY** | Why is this problem important? Why does the existing approach fall short? Why should the reader care? | Abstract (sentence 2), Introduction (paragraphs 1-2), Related Work (gaps) | Build motivation before presenting solution |
| **SO WHAT** | What are the implications? What changes because of this work? What should the reader do differently? | Abstract (sentence 4-5), Experiments (interpretation), Conclusion | Quantify impact, connect to broader picture |

**Actions:**

1. Write one paragraph for each element (WHAT, WHY, SO WHAT). These become the seed for the Abstract and Introduction.

2. Verify the narrative arc:
   - Does the WHY create tension (a problem that needs solving)?
   - Does the WHAT resolve that tension (here is the solution)?
   - Does the SO WHAT deliver payoff (here is the evidence and impact)?

3. Check for common narrative failures:
   - **Missing WHY**: Paper jumps to the method without establishing the problem. Reviewers ask "why should I care?"
   - **Weak SO WHAT**: Results are presented without interpretation. Reviewers ask "so what does this mean?"
   - **Disconnected WHAT**: The method described does not clearly solve the problem stated in the WHY. Reviewers ask "how does this address the stated problem?"

4. Record the WHAT/WHY/SO WHAT paragraphs in `plan/outline.md`.

### Step 3: Draft Figure 1 Concept

Figure 1 is the most important visual element in the paper. Many reviewers look at Figure 1 before reading any text. It must communicate the core idea at a glance.

**Actions:**

1. Determine what Figure 1 should show. Common effective patterns:

   | Figure 1 Type | When to Use | Example |
   |---|---|---|
   | **Method overview/pipeline** | The contribution is a new system or algorithm | Block diagram showing input -> components -> output |
   | **Problem illustration + solution** | The contribution solves a visible problem | Left: problem/failure case, Right: our solution |
   | **Key result teaser** | The contribution is a surprising empirical finding | One compelling plot or visualization that hooks the reader |
   | **Comparison** | The contribution outperforms existing methods | Side-by-side comparison with clear quality difference |
   | **Concept diagram** | The contribution is a new framework or abstraction | Visual metaphor or schematic of the key idea |

2. Write a textual description of the planned Figure 1:
   ```markdown
   ## Figure 1 Concept

   **Type:** [Method overview / Problem+Solution / Result teaser / Comparison / Concept]

   **Content:** [Describe what the figure shows, panel by panel if multi-panel]

   **Caption draft:** [Draft a self-contained caption. A reader should understand the figure
   from the caption alone without reading the paper body.]

   **Key message:** [What should a reader take away from glancing at this figure for 10 seconds?]

   **Data/artifacts needed:** [What code outputs, results, or diagrams are needed to create this figure?]
   ```

3. Record the Figure 1 concept in `plan/outline.md`.

4. If the project has visualization code or result images that could serve as Figure 1, note the specific file paths.

### Step 4: Generate Paper Outline

Produce the complete paper outline in `plan/outline.md`.

**Actions:**

1. Select the appropriate structure based on the target venue and contribution type:

   **Standard ML/AI Conference Structure (NeurIPS, ICML, ICLR):**
   ```
   1. Introduction (1-1.5 pages)
   2. Related Work (1-1.5 pages) [can also be after Methods]
   3. Methods / Approach (2-3 pages)
      3.1. Problem Formulation
      3.2. [Core Method Component 1]
      3.3. [Core Method Component 2]
      3.4. Training / Optimization
   4. Experiments (2-3 pages)
      4.1. Experimental Setup
      4.2. Main Results
      4.3. Ablation Studies
      4.4. Analysis / Qualitative Results
   5. Limitations
   6. Conclusion
   References
   Appendix (unlimited for NeurIPS/ICML/ICLR)
   ```

   **NLP Conference Structure (ACL, EMNLP, NAACL):**
   ```
   1. Introduction
   2. Related Work [often before Methods in NLP]
   3. Task Definition / Problem Setup
   4. Approach / Method
   5. Experimental Setup
   6. Results and Analysis
   7. Discussion [more common in NLP papers]
   8. Conclusion
   Limitations [required section at ACL venues]
   Ethics Statement [required at ACL venues]
   ```

   **Journal Structure (flexible, typically 8-15 pages):**
   ```
   1. Introduction
   2. Related Work
   3. Preliminaries / Background
   4. Proposed Method
   5. Experimental Evaluation
      5.1. Setup
      5.2. Results
      5.3. Analysis
   6. Discussion
   7. Conclusion
   ```

2. For each section in the outline, write:
   - **Purpose**: What this section accomplishes in the narrative
   - **Key points**: 3-5 bullet points of what must be covered
   - **Length target**: Expected page/paragraph count
   - **Artifact mapping**: Which code files inform this section (from Module 01 Step 6)
   - **Figure/Table placeholders**: What visual elements belong here

3. Map contributions to sections explicitly:
   ```markdown
   Contribution 1: [description] --> Sections 3.2, 4.2 (Table 1), 4.3 (Ablation Table)
   Contribution 2: [description] --> Sections 3.3, 4.2 (Table 1, rows 5-8)
   Contribution 3: [description] --> Sections 4.4, Figure 3
   ```

4. Write the outline to `plan/outline.md`.

**Outline Template:**

```markdown
# Paper Outline

## One-Sentence Contribution
[Confirmed statement from Step 1]

## Narrative Arc (WHAT / WHY / SO WHAT)
[From Step 2]

## Figure 1 Concept
[From Step 3]

## Target Venue
[Name, page limit, format]

---

## 1. Introduction (~1.5 pages)
**Purpose:** Hook the reader, establish the problem, present the contribution.
**Key points:**
- Opening: [problem context and importance]
- Gap: [what is missing in current approaches]
- Contribution: [what this paper offers -- 2-4 bullets]
- Results preview: [key numbers that demonstrate success]
- Paper organization: [brief roadmap, optional]
**Figures:** Figure 1 (method overview)
**Artifact mapping:** README.md, project overview

## 2. Related Work (~1 page)
**Purpose:** Position this work in the literature landscape.
**Key points:**
- Theme 1: [prior approaches family 1]
- Theme 2: [prior approaches family 2]
- Theme 3: [prior approaches family 3]
- Positioning: [how our work differs from each theme]
**Artifact mapping:** Literature from Module 02

## 3. Methods (~2.5 pages)
**Purpose:** Enable a reader to reimplement the method.
### 3.1 Problem Formulation
- [Define inputs, outputs, objective]
### 3.2 [Component 1 Name]
- [Core technical contribution, with equations]
### 3.3 [Component 2 Name]
- [Supporting technical contribution]
### 3.4 Training / Optimization
- [How the model is trained, loss functions]
**Figures:** Figure 2 (architecture detail)
**Artifact mapping:** [specific model/algorithm files]

## 4. Experiments (~2.5 pages)
**Purpose:** Provide evidence that the method works.
### 4.1 Setup
- Datasets, baselines, metrics, implementation details
### 4.2 Main Results
- Table 1: comparison with baselines
- Key finding: [what the numbers show]
### 4.3 Ablation Studies
- Table 2: component-wise analysis
- Key finding: [which components matter most]
### 4.4 Analysis
- Figure 3: [qualitative results / visualization]
- Discussion of when/why the method succeeds or fails
**Artifact mapping:** [specific result/eval files]

## 5. Limitations
**Purpose:** Honest assessment of scope and failure modes.
**Key points:**
- [Limitation 1]
- [Limitation 2]

## 6. Conclusion (~0.5 pages)
**Purpose:** Key takeaway and future outlook.
**Key points:**
- Core insight (not a summary of the paper)
- 1-2 promising future directions with reasoning

---

## Appendix Plan
- [Additional experiments]
- [Proof details]
- [Extended results tables]
- [Implementation details]
```

## Time Allocation Advice

From experienced ML paper writers, the rough time allocation for a paper should be:

| Component | Time Share | Explanation |
|---|---|---|
| Abstract | 25% | The abstract is read 100x more than the full paper. Every word must earn its place. |
| Introduction | 25% | The introduction determines whether a reviewer reads the rest carefully or skims. |
| Figures | 25% | Publication-quality figures communicate faster than text. Figure 1 alone may take days. |
| Everything else | 25% | Methods, Experiments, Related Work, Conclusion combined. |

This may seem extreme, but the reality is that most review decisions are formed by page 2 and the figures. Invest accordingly.

## Conference-Specific Structure Guidance

| Venue | Page Limit (Main) | Appendix | Key Structural Notes |
|---|---|---|---|
| NeurIPS | 9 pages | Unlimited | Broader Impact statement sometimes required. Checklist required. |
| ICML | 8 pages | Unlimited | Shorter than NeurIPS; be more concise in Related Work. |
| ICLR | 8-10 pages | Unlimited | Reviews are public. Extra emphasis on clarity and reproducibility. |
| ACL/EMNLP | 8 pages (long), 4 pages (short) | Limited | Limitations section mandatory. Ethics statement mandatory. |
| AAAI | 7 pages + 1 references | 3 pages appendix | Tightest page limit among top venues. Extremely concise writing needed. |
| COLM | 9 pages | Unlimited | Newer venue, follows NeurIPS-like format. |
| CVPR/ECCV/ICCV | 8 pages | 2-3 pages supplementary | Heavy emphasis on visual results and comparisons. |
| KDD | 8 pages | Varies | Applied track vs. research track have different expectations. |

**General rules by page limit:**
- 7-8 pages: Related Work can be compressed to 0.5-0.75 pages. Move extended results to appendix. No room for leisurely introductions.
- 9-10 pages: Standard structure works. Related Work can be 1-1.5 pages.
- Journal (no strict limit): Can afford a Preliminaries section, extended Discussion, and comprehensive Related Work.

## Deliverables

Upon completing this module:

1. **`plan/outline.md`** containing:
   - Confirmed one-sentence contribution
   - WHAT/WHY/SO WHAT narrative paragraphs
   - Figure 1 concept description
   - Complete section-by-section outline with key points, length targets, and artifact mapping
   - Contribution-to-section mapping
2. **`plan/progress.md`** updated with:
   - S3 Paper Structure: COMPLETE
   - Outline confirmed by user
   - Next action: proceed to S4 (Writing Core)

## Common Pitfalls

- **Pitfall:** Starting to write without a confirmed outline. The outline is a contract between the writer and the reader. Changing structure mid-draft is extremely costly.
- **Pitfall:** Making the Methods section too long relative to Experiments. Reviewers want evidence. A 4-page Methods section with 1 page of experiments signals a theory-heavy paper with weak validation.
- **Pitfall:** Forgetting the Limitations section. All major ML conferences now require or strongly encourage an explicit Limitations section. Omitting it signals lack of self-awareness.
- **Pitfall:** Not planning figures early. Figures take the longest to produce and have the highest impact. Plan them during outlining, not as an afterthought during writing.
- **Pitfall:** Treating Related Work as obligatory rather than strategic. The Related Work section should build the case for why your approach is needed, not just demonstrate you read papers.
