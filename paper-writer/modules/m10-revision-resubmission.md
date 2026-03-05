# Module 10: Revision and Resubmission

Handle reviewer feedback, prepare point-by-point responses, manage revisions, convert between conference formats, and prepare camera-ready versions. This module covers the full lifecycle from receiving reviews to final acceptance.

## Reviewer Response Matrix

For every reviewer comment, create a structured response matrix. This matrix serves as the planning document before writing the actual response letter.

### Classification System

Classify each reviewer comment into one of three categories:

| Category | Meaning | Action Required |
|----------|---------|-----------------|
| **Accept** | The reviewer's point is valid and we will fully address it. | Make the requested change. Describe the change in the response. |
| **Partial-Accept** | The reviewer raises a valid concern but the suggested fix is not the best approach, or the concern is partially addressed already. | Acknowledge the concern. Explain what change we will make and why it differs from what was suggested. |
| **Respectful Decline** | The reviewer's point is based on a misunderstanding, or the requested change would weaken the paper. | Politely clarify the misunderstanding or explain why the current approach is preferable, with evidence. |

### Matrix Template

```markdown
## Reviewer Response Matrix

| ID | Reviewer | Comment Summary | Category | Justification | Paper Change | Response Draft |
|----|----------|----------------|----------|---------------|-------------|----------------|
| R1-Q1 | R1 | Missing ablation for component X | Accept | Valid -- strengthens the paper | Add Table 4 in Section 4.3 | "We thank... We have added..." |
| R1-Q2 | R1 | Claims about Y are too strong | Partial-Accept | Fair point but results do support a moderate claim | Soften language in Section 5 | "We appreciate... We have revised..." |
| R2-Q1 | R2 | Method is similar to Z (2023) | Decline | Misunderstanding -- our approach differs in... | Add clarification in Section 3.1 | "We thank... We respectfully note..." |
```

Fill in this matrix completely before writing any response text. This prevents ad hoc responses and ensures consistent tone.

## Response Letter Template

The response letter (also called rebuttal or author response) follows a structured format. Use this template as the starting point.

### Header

```markdown
# Response to Reviewers

We sincerely thank all reviewers for their thoughtful and constructive feedback.
Their comments have helped us substantially improve the manuscript. Below, we
address each comment point by point. All changes in the revised manuscript are
highlighted in blue for easy identification.

**Summary of major changes:**
- [Major change 1: e.g., "Added ablation study (new Table 4)"]
- [Major change 2: e.g., "Clarified the relationship to method Z in Section 3.1"]
- [Major change 3: e.g., "Extended experiments with two additional baselines"]
```

### Per-Reviewer Section

```markdown
## Reviewer 1

We thank Reviewer 1 for the detailed and constructive review.

---

**R1-Q1: [Quoted or paraphrased concern]**

[Direct response]

[Evidence: experimental results, theoretical argument, or reference to specific
paper section/figure/table]

[Description of paper change, if any:]
*Change: We have added [description] in Section X.Y (page Z, paragraph N).*

---

**R1-Q2: [Quoted or paraphrased concern]**

[Direct response]

...

## Reviewer 2

We thank Reviewer 2 for the insightful comments.

---

**R2-Q1: [Quoted or paraphrased concern]**

...
```

### LaTeX Response Letter Format

For venues that require or prefer a LaTeX-formatted response:

```latex
\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{xcolor}

\newcommand{\rev}[1]{\textbf{#1}}  % Reviewer comment formatting
\newcommand{\resp}[1]{#1}           % Response formatting
\newcommand{\change}[1]{\textcolor{blue}{\textit{Change: #1}}}

\begin{document}

\section*{Response to Reviewers}

We sincerely thank all reviewers for their thoughtful feedback.

\subsection*{Reviewer 1}

\rev{R1-Q1: The paper lacks an ablation study for the proposed attention module.}

\resp{We appreciate this suggestion. We have conducted the requested ablation
study and present the results in Table~4 (Section~4.3 of the revised manuscript).
Removing the attention module reduces accuracy by 3.2\%, confirming its
contribution to the overall performance.}

\change{Added Table~4 and accompanying discussion in Section~4.3, page~7.}

\end{document}
```

## Rebuttal Best Practices

### Do

- **Thank reviewers genuinely.** Even critical reviews contain useful perspectives. A professional tone throughout the response demonstrates maturity.
- **Address every single comment.** Do not skip any concern, no matter how minor. Reviewers notice when their points are ignored, and it signals disrespect.
- **Provide evidence.** Back up responses with specific numbers, citations, or references to paper sections. "We believe our method is better" is weak. "As shown in revised Table 3, our method achieves 94.2% vs. 91.7% for the baseline" is strong.
- **Be concise.** Reviewers read many responses. Long-winded explanations dilute the impact. Get to the point quickly.
- **Quote the reviewer's concern.** This makes it easy for reviewers and editors to match responses to comments without switching between documents.
- **Acknowledge valid criticisms.** Saying "The reviewer is correct that..." before explaining the fix builds credibility.
- **Highlight changes clearly.** Use blue text, margin marks, or a change log so reviewers can quickly verify that changes were made.

### Do Not

- **Do not be defensive or combative.** Even when a reviewer is wrong, respond with evidence and professionalism, never with frustration.
- **Do not dismiss concerns.** "We disagree" without explanation is unacceptable. Always explain why.
- **Do not make promises without delivering.** If you say "We have added an ablation study," the ablation study must actually be in the revised paper.
- **Do not over-revise.** Making changes the reviewers did not ask for can introduce new problems and confuse the review process. Stick to addressing the actual concerns.
- **Do not change the core contribution.** If reviewers misunderstood the contribution, clarify it. Do not pivot to a different contribution.

## When to Accept Criticism vs. When to Push Back

### Accept When

- The reviewer identifies a genuine gap (missing experiment, unsupported claim, unclear explanation).
- The requested change strengthens the paper without altering the core contribution.
- Multiple reviewers raise the same concern (strong signal that the issue is real).
- The reviewer points out a factual error or inconsistency.

### Push Back (Respectfully) When

- The reviewer asks for experiments that are outside the paper's scope (politely explain scope boundaries).
- The reviewer misunderstands the method (provide a clearer explanation, not a change to the method).
- The reviewer requests changes that would weaken the paper's narrative or contradict the evidence.
- The reviewer suggests adding related work that is not actually related (explain why it is out of scope).

### How to Push Back

```markdown
**R2-Q3: The authors should compare against method Z (Smith et al., 2023).**

We appreciate the suggestion. We are aware of method Z and initially considered
including it. However, method Z addresses a fundamentally different problem
setting (supervised, with labeled data), while our work operates in the
unsupervised setting. A direct comparison would not be meaningful because the
methods require different inputs. We have added a discussion clarifying this
distinction in Section 2 (Related Work), paragraph 3.

*Change: Added clarification of the difference between our problem setting and
that of method Z in Section 2, page 3.*
```

## Change Log Generation

Track all modifications between the original and revised manuscript. The change log serves two purposes: it helps the response letter reference specific changes, and it helps the authors verify that all promised changes were actually made.

### Change Log Format

```markdown
# Change Log: Revision 1

## Summary Statistics
- Sections modified: 5 of 7
- New content added: Table 4, Figure 6, Section 4.3 (ablation study)
- Content removed: None
- Net page change: +0.5 pages (within limit)

## Detailed Changes

### Section 1: Introduction
| Location | Change Type | Before | After | Triggered By |
|----------|------------|--------|-------|-------------|
| p1, para 3 | Rewrite | "dramatically outperforms" | "achieves a 3.2% improvement over" | R1-Q4 |
| p2, para 1 | Addition | -- | New paragraph clarifying scope | R2-Q1 |

### Section 3: Methods
| Location | Change Type | Before | After | Triggered By |
|----------|------------|--------|-------|-------------|
| p4, Eq. 3 | Correction | Missing subscript | Added subscript $i$ | R3-Q2 |
| p5, para 2 | Clarification | "the loss function" | "the contrastive loss function (Eq. 3)" | R1-Q2 |

### Section 4: Experiments
| Location | Change Type | Before | After | Triggered By |
|----------|------------|--------|-------|-------------|
| p7 | Addition | -- | New Table 4 (ablation study) | R1-Q1 |
| p7, para 1 | Addition | -- | Discussion of ablation results | R1-Q1 |

### References
| Change | Details | Triggered By |
|--------|---------|-------------|
| Added | Chen et al. (2024), "..." | R2-Q3 |
| Added | Wang et al. (2023), "..." | R1-Q5 |
```

### Automated Change Tracking

Use `latexdiff` to automatically generate a visual diff between the original and revised manuscripts:

```bash
# Generate a diff document highlighting all changes
latexdiff original/main.tex revised/main.tex > diff.tex
pdflatex diff.tex && pdflatex diff.tex

# The output PDF shows additions in blue and deletions in red with strikethrough
```

For manual change highlighting in the revised manuscript:

```latex
% In preamble
\usepackage{xcolor}
\newcommand{\revised}[1]{\textcolor{blue}{#1}}

% In text
\revised{This sentence was added in response to Reviewer 1, Comment 3.}
```

## Conference Format Conversion Workflow

When a paper is rejected from one venue and will be resubmitted to another, or when converting from conference to journal format.

### Key Differences Between Major Venues

| Aspect | NeurIPS | ICML | ICLR | ACL | AAAI | Journal |
|--------|---------|------|------|-----|------|---------|
| Page limit (main) | 9 + refs | 8 + refs | 10 + refs | 8 (long) / 4 (short) | 7 + refs | Varies |
| Appendix | Unlimited | Unlimited | Unlimited | Unlimited | 2 pages | Varies |
| Broader impact | Required | Required | No | No | No | Rare |
| Limitations | Expected | Expected | Expected | Required | Expected | Expected |
| Ethics statement | Required | Required | Required | Required | Expected | Varies |
| LLM disclosure | No | No | Required | Expected | No | Rare |
| Review type | Double-blind | Double-blind | Double-blind | Double-blind | Double-blind | Varies |
| Line numbers | Required | Required | No | Required | Required | Varies |

### Content Migration Procedure

The critical rule from M08 applies here: **never merge template preambles.** Always start fresh with the target template.

1. **Set up target template**: Download the complete target venue template. Verify it compiles as-is.
2. **Copy content only**: Transfer text, figures, tables, equations, and bibliography from the source. Do NOT transfer preamble, package imports, or custom commands from the source template.
3. **Redefine custom commands**: If the source paper used custom commands (e.g., `\method`, `\dataset`), redefine them in the target template's preamble.
4. **Adjust page limits**: This is often the most significant change. Strategies for reducing page count:
   - Move detailed proofs or derivations to the appendix.
   - Consolidate similar tables (e.g., merge per-dataset tables into one combined table).
   - Reduce figure sizes while maintaining readability.
   - Tighten prose (remove redundancies identified during M07 polish).
   - Move supplementary experiments to the appendix.
5. **Add or remove required sections**: Check the target venue's requirements (see Key Differences table) and add any missing required sections or remove sections not appropriate for the target venue.
6. **Update framing if needed**: Different venues have different audiences. A systems paper at NeurIPS may need different framing than the same paper at ICML. Adjust the introduction and abstract to match the target audience.
7. **Re-run M08 and M09**: Compile the converted paper and run the full review checklist for the new target venue.

### Page Limit Adjustment Strategies

When the target venue has a lower page limit than the source:

| Strategy | Typical Savings | Risk |
|----------|----------------|------|
| Move proofs to appendix | 0.5-1.5 pages | Low (reviewers can still access proofs) |
| Consolidate tables | 0.25-0.5 pages | Low (if done carefully) |
| Reduce figure sizes by 15-20% | 0.25-0.5 pages | Medium (readability may suffer) |
| Tighten prose (remove filler) | 0.25-1 page | Low (usually improves the paper) |
| Move supplementary experiments to appendix | 0.5-1.5 pages | Medium (main paper loses some evidence) |
| Reduce Related Work section | 0.25-0.5 pages | Medium (may appear incomplete to reviewers) |
| Use `\small` for tables or algorithms | 0.1-0.3 pages | Low (within reason) |

When the target venue has a higher page limit:

- Expand the experimental section with additional baselines, ablations, or analysis.
- Add more detailed related work discussion.
- Include additional figures or visualizations.
- Expand the discussion of limitations and future work.

## Camera-Ready Preparation

After a paper is accepted (conditionally or unconditionally), prepare the camera-ready version.

### De-Anonymize

- Restore author names, affiliations, and email addresses in the `\author{}` block.
- Remove any anonymization commands (e.g., NeurIPS `\nipsfinalcopy` or ICLR `\iclrfinalcopy`).
- Restore self-citations to first person ("our previous work" instead of "Previous work [X]").
- Remove anonymous repository links and replace with actual links.

### Add Acknowledgments

- Restore the acknowledgments section (previously hidden for blind review).
- Include funding sources, grant numbers, and sponsor names.
- Acknowledge any computing resources provided.
- Thank colleagues who provided feedback (if applicable and customary).
- For NeurIPS/ICML: acknowledgments are typically placed after the conclusion, before references.

### Final Formatting

- Switch from review mode to camera-ready mode in the template (e.g., `\usepackage[final]{neurips_2024}`).
- Remove line numbers if they were required for review.
- Verify the paper still compiles cleanly and is within page limits after de-anonymization (author blocks can take significant space).
- Add any required copyright notices or conference headers.
- Generate the final PDF and verify:
  - Correct page size (usually US Letter for US conferences, A4 for some European venues).
  - All fonts are embedded in the PDF.
  - Hyperlinks work correctly.
  - PDF metadata is correct (title, authors).

### Camera-Ready Checklist

- [ ] Author names and affiliations correct and complete.
- [ ] Paper compiles in camera-ready mode without errors.
- [ ] All reviewer-requested changes incorporated.
- [ ] Acknowledgments section present with correct funding information.
- [ ] Page count within camera-ready limits (may differ from review limits).
- [ ] All TODO/FIXME comments removed.
- [ ] No blue revision highlighting remaining (from `\revised{}` commands).
- [ ] Supplementary materials prepared and uploaded separately if required.
- [ ] Copyright form signed and submitted (if required by venue).
- [ ] All co-authors have approved the final version.
- [ ] LaTeX source files prepared for upload (some venues require source in addition to PDF).
- [ ] Video or poster abstract submitted (if required by venue deadline).

## Revision Timeline Management

For journal revisions with a deadline:

### Typical Journal Revision Windows

| Response Type | Typical Deadline | Urgency |
|--------------|-----------------|---------|
| Minor revision | 30-60 days | Moderate -- usually straightforward changes |
| Major revision | 60-120 days | High -- may require new experiments |
| Revise and resubmit | 90-180 days | High -- significant changes expected |

### Recommended Workflow

1. **Day 1-3**: Read all reviews carefully. Create the reviewer response matrix. Do not start writing immediately -- let the feedback settle.
2. **Day 4-7**: Plan all changes. Identify which changes require new experiments (longest lead time). Start experiments immediately.
3. **Day 8-14**: Write response letter draft addressing each comment. Make text-only changes to the manuscript.
4. **Day 15-21**: Incorporate experimental results. Update tables and figures.
5. **Day 22-28**: Run M07 (polish) on revised sections. Run M08 (compilation check). Run M09 (review) on the complete revised paper.
6. **Day 29-30**: Final proofreading. All co-authors review and approve. Submit.

For conference rebuttals with short timelines (typically 5-7 days):

1. **Day 1**: Read reviews. Create response matrix. Identify must-address vs. nice-to-address items.
2. **Day 2-3**: Run any quick experiments that directly address reviewer concerns.
3. **Day 4-5**: Write concise, evidence-based responses. Every word counts in a page-limited rebuttal.
4. **Day 6**: All co-authors review the rebuttal.
5. **Day 7**: Final edits and submit.
