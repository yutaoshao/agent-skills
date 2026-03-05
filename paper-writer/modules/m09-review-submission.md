# Module 09: Review and Submission

Comprehensive pre-submission review and submission package preparation. This module orchestrates checks from M06 (Citation Management), M07 (Polish), and M08 (LaTeX Compilation), then adds structural and venue-specific checks to ensure the paper is submission-ready.

## Review Execution Order

Run the following checks in sequence. Each check category produces findings classified by severity (see Severity Report Format at the end of this module).

### Phase 1: Automated Checks (M06 + M07 + M08)

Execute the verification procedures from the three preceding modules:

1. **M06 Citation Verification**: Run the 5-step verification workflow on all citations. Identify any remaining placeholders. Check citation gap analysis metrics (temporal, methodological, foundational, claim support). Verify reference count targets.

2. **M07 Polish Check**: Run the style check against the de-AI pattern catalog. Verify all 8 English categories (or 4 Chinese categories) have been addressed. Confirm the three-round quality check passes.

3. **M08 Compilation Check**: Execute the full compilation pipeline. Parse the log for errors, warnings, and undefined references. Verify the quick checklist items all pass.

Collect all findings from these three modules before proceeding to Phase 2.

### Phase 2: Structural and Content Checks

These checks go beyond the individual module scopes to assess the paper as a whole.

#### Abstract Completeness

The abstract must be self-contained and complete. Verify:

- **Problem statement**: The research problem or question is clearly stated.
- **Approach summary**: The proposed method or contribution is described.
- **Key results**: At least one quantitative result is included (specific numbers, not vague claims).
- **Significance**: A sentence explaining why the results matter.
- **Self-containment**: No citations (`\cite{}`), no undefined abbreviations, no references to figures or tables.
- **Word count**: Within venue limits (typically 150-250 words for conferences, up to 300 for journals).

#### Keywords

- 4-6 keywords provided (if required by the venue).
- Keywords match the venue's conventions (check recent published papers).
- Keywords are specific enough to be useful for indexing ("deep learning" is too broad; "graph neural network for molecular property prediction" is better).

#### Section Structure

- **Logical flow**: Sections follow a natural progression (Introduction, Related Work, Methods, Experiments, Discussion/Conclusion, or the venue's expected order).
- **No orphan subsections**: If section 3.1 exists, section 3.2 must also exist. A section should not have only one subsection.
- **Balanced sections**: No section is disproportionately long or short relative to its importance. Methods and Experiments should receive the most space.
- **Section depth**: Avoid subsections deeper than three levels (e.g., 3.2.1 is acceptable; 3.2.1.1 is too deep for most venues).

#### Notation Consistency

Scan the entire paper for notation conflicts:

- The same symbol must represent the same concept throughout. Do not switch between `\mathbf{q}` and `\boldsymbol{q}` for the same vector.
- Define all notation on first use, either inline or in a notation table.
- Verify that notation in equations matches notation in the text.
- Check that figure labels and table headers use the same notation as the body text.

#### Tense Consistency

- **Abstract**: Present tense for general statements and the approach; past tense for specific results.
- **Introduction**: Present tense for established facts and the research problem; past tense for what others have done.
- **Methods**: Present tense (describing the approach as it exists).
- **Experiments/Results**: Past tense (reporting what was done and observed).
- **Discussion**: Present tense for interpretations; past tense for specific findings.
- **Conclusion**: Present tense for contributions and implications; future tense for future work (sparingly).

#### Journal/Conference Formatting

- Page count within venue limits.
- Font sizes match the template requirements.
- Margins have not been modified from the template defaults.
- Line spacing matches the template (single-spaced for most conferences, sometimes 1.5 or double for journal submissions).
- Required sections are present (e.g., broader impact, limitations, ethics statement).
- Forbidden content is absent (e.g., acknowledgments during blind review).

#### Declarations and Statements

Check whether the venue requires any of the following and verify their presence:

- Author contributions statement (CRediT format or free text).
- Competing interests / conflicts of interest declaration.
- Data availability statement.
- Code availability statement.
- Ethics approval statement (for human subjects or animal research).
- Funding / acknowledgments (check if required or forbidden during review).

## Conference-Specific Checklists

Load `references/conference-checklists.md` for the complete conference-specific checklists. The following is a summary of mandatory items for major venues.

### NeurIPS (16-Item Mandatory Checklist)

NeurIPS requires authors to submit a paper checklist covering:

1. Claims: Main claims clearly stated in abstract and introduction.
2. Limitations: Discussion of limitations included.
3. Theory: Assumptions and proofs clearly stated (if applicable).
4. Experiments: Reproducibility information (compute, hyperparameters, seeds).
5. Code: Code availability stated.
6. Data: Dataset details and licensing.
7. Experimental methodology: Error bars, statistical tests, significance.
8. Compute: Computational resources disclosed.
9. Ethics: Broader impact discussed.
10. Safeguards: Potential negative impacts addressed.
11. Licenses: Asset licenses respected.
12. New assets: Licensed appropriately.
13. Crowdsourcing: IRB approval and fair compensation (if applicable).
14. Human subjects: IRB approval (if applicable).
15. Consent: Consent obtained for data involving people.
16. Privacy: PII handling addressed.

The checklist must be filled out honestly. "Not Applicable" is acceptable where genuinely not applicable, but reviewers will flag suspicious blanket "N/A" responses.

### ICML

- Broader impact statement required.
- Reproducibility section expected (hyperparameters, compute, random seeds).
- Code submission encouraged (anonymous repository during review).
- Ethics review triggers on certain topics (fairness, privacy, dual use).

### ICLR

- LLM disclosure: If LLMs were used in the research or writing process, this must be disclosed.
- Reproducibility statement required.
- Ethics statement required for applicable work.
- Anonymous submission: no author identifying information anywhere in the paper or supplementary.

### ACL / EMNLP

- Limitations section required (mandatory, not optional).
- Ethics statement required.
- Responsible NLP checklist may be required.
- Supplementary materials must be anonymized.

### AAAI

- Ethics statement may be required.
- Reproducibility section expected.
- Supplementary materials submitted separately.

## Self-Review from Reviewer Perspective

Load `references/reviewer-guidelines.md` for the complete reviewer evaluation framework. Conduct a self-review by evaluating the paper against the four standard review criteria used at most ML/AI venues.

### Quality

- Are the claims well-supported by theoretical analysis or experimental results?
- Is the experimental evaluation thorough (sufficient baselines, ablation studies, statistical significance)?
- Are there obvious flaws in the methodology or analysis?
- Is the paper technically sound?

### Clarity

- Is the paper well-written and easy to follow?
- Are the key ideas and contributions immediately clear from the abstract and introduction?
- Is the notation consistent and well-defined?
- Are figures and tables informative and well-designed?
- Could a knowledgeable researcher reproduce the work from the paper alone?

### Significance

- Does the paper address an important problem?
- Are the results a meaningful advance over the state of the art?
- Will the paper influence future research or practice?
- Is the contribution substantial enough for the venue (workshop paper vs. main conference vs. journal)?

### Originality

- Is the approach genuinely new, or an incremental combination of known techniques?
- Is the paper sufficiently distinguished from prior work?
- Does the paper clearly articulate what is new compared to the most similar existing work?

For each criterion, assign an honest self-assessment: Strong, Adequate, or Weak. Prioritize addressing any "Weak" areas before submission.

## Anonymization Check (for Blind Review)

For venues requiring single-blind or double-blind review, verify the following:

### Author Information

- [ ] No author names in the paper body, headers, or footers.
- [ ] The `\author{}` block uses "Anonymous" or is handled by the venue's anonymization command.
- [ ] No institutional affiliations that identify the authors.
- [ ] PDF metadata does not contain author names (check with `pdfinfo main.pdf`).

### Acknowledgments

- [ ] No acknowledgments section during review (or it is commented out / uses a venue-provided mechanism to hide it).
- [ ] No grant numbers or funding sources that identify the authors.

### Self-Citations

- [ ] Own prior work is cited in third person ("Previous work [X] showed..." not "Our previous work [X] showed...").
- [ ] The reference list does not disproportionately cite the authors' own papers in a way that reveals identity.
- [ ] No references to "our repository at github.com/..." or similar identifying URLs.

### Supplementary Materials

- [ ] Code repositories are anonymous (use anonymous GitHub or similar services during review).
- [ ] Supplementary PDF does not contain author information.
- [ ] File metadata of all supplementary files is clean.

### Hidden Identifiers

- [ ] No watermarks, institutional logos, or headers from the source template.
- [ ] LaTeX source comments do not contain author names or identifying information.
- [ ] Figure files do not contain metadata identifying the creator (check EXIF data for images).

## Submission Package Preparation

After all checks pass, prepare the submission package.

### Cover Letter Template

For journal submissions that require a cover letter:

```
Dear Editor(s) of [Journal Name],

We submit our manuscript titled "[Paper Title]" for consideration as a
[Article Type: Original Research / Review / Letter / Short Communication]
in [Journal Name].

[1-2 sentences on what the paper does and why it matters.]

[1 sentence on key results.]

[Statement on originality and prior publication status:]
This work has not been published previously and is not under consideration
for publication elsewhere.

[Statement on author agreement:]
All authors have read and approved the final manuscript.

[Optional: Suggested reviewers or excluded reviewers.]

Sincerely,
[Corresponding Author Name]
[Affiliation]
[Email]
```

### Author Contributions Statement

Use the CRediT (Contributor Roles Taxonomy) format when the journal supports it:

```
Author Contributions:
[First Author]: Conceptualization, Methodology, Software, Writing -- Original Draft.
[Second Author]: Validation, Formal Analysis, Writing -- Review & Editing.
[Third Author]: Supervision, Project Administration, Funding Acquisition.
```

CRediT roles: Conceptualization, Data Curation, Formal Analysis, Funding Acquisition, Investigation, Methodology, Project Administration, Resources, Software, Supervision, Validation, Visualization, Writing -- Original Draft, Writing -- Review & Editing.

### Data Availability Statement

```
Data Availability:
[Choose one:]
- The datasets generated and analyzed during the current study are available
  in the [repository name] repository, [URL/DOI].
- The data that support the findings of this study are available from
  [source] but restrictions apply. Data are available from the authors
  upon reasonable request and with permission of [source].
- All data generated or analyzed during this study are included in this
  published article and its supplementary information files.
- Data sharing is not applicable as no datasets were generated or analyzed.
```

### Ethics Statement

```
Ethics Statement:
[Choose applicable:]
- This study was approved by the Institutional Review Board of [Institution]
  (Protocol #[Number]).
- This study does not involve human subjects or animal experimentation.
- Informed consent was obtained from all participants.
- This work uses publicly available datasets and does not raise ethical concerns.
```

### Competing Interests Declaration

```
Declaration of Competing Interests:
[Choose one:]
- The authors declare that they have no known competing financial interests
  or personal relationships that could have appeared to influence the work
  reported in this paper.
- [Author Name] has received research grants from [Organization].
  [Other Author Name] is a consultant for [Company]. The remaining authors
  declare no competing interests.
```

## Severity Report Format

All findings from the review process should be organized into a structured report using three severity levels.

### Errors (Must Fix Before Submission)

Issues that will cause desk rejection, compilation failure, or serious credibility damage.

```
ERROR [E01]: Compilation fails with undefined reference \ref{fig:architecture}
  Location: main.tex line 142
  Fix: Add \label{fig:architecture} to the figure environment on line 87

ERROR [E02]: Citation \cite{smith2024method} is a placeholder -- paper not verified
  Location: main.tex line 256, references.bib line 89
  Fix: Verify the paper exists or remove the citation

ERROR [E03]: Paper exceeds page limit (10 pages, limit is 9+1)
  Location: Overall document
  Fix: Reduce content by approximately 0.5 pages
```

### Warnings (Should Fix Before Submission)

Issues that will not cause rejection but may negatively affect review scores.

```
WARNING [W01]: Discussion section has 5 paragraphs all starting with "The results..."
  Location: main.tex lines 310-380
  Fix: Apply M07 polish to Discussion section

WARNING [W02]: Only 22% of references are from the last 3 years (target: 30%+)
  Location: references.bib
  Fix: Add 3-5 recent references following M06 gap analysis

WARNING [W03]: Overfull hbox (15pt too wide) in Table 2
  Location: main.tex line 198
  Fix: Reduce table font size or restructure columns
```

### Suggestions (Nice to Have)

Improvements that would strengthen the paper but are not blocking.

```
SUGGESTION [S01]: Abstract could include a specific accuracy number instead of "competitive results"
  Location: main.tex line 12
  Benefit: Quantitative abstracts attract more reads

SUGGESTION [S02]: Consider adding an ablation study for component X
  Benefit: Addresses likely reviewer question about X's contribution

SUGGESTION [S03]: Figure 3 caption could be more self-contained
  Location: main.tex line 167
  Benefit: Readers often scan figures before reading the full text
```

### Summary Table

End the report with a summary:

```
Review Summary:
  Errors:      [N] (must fix)
  Warnings:    [N] (should fix)
  Suggestions: [N] (nice to have)

  Blocking issues: [list of error codes]
  Estimated effort: [time estimate to address all errors and warnings]
```
