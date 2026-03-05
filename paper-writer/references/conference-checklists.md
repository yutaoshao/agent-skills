# Conference Checklists

Venue-specific submission checklists for major CS/ML/AI conferences. Load this file during M09 (Review & Submission) to ensure compliance with venue requirements.

---

## NeurIPS Paper Checklist (16 Mandatory Items)

The NeurIPS checklist is mandatory since NeurIPS 2023. Every paper must include a completed checklist as an appendix (not counted toward page limit). Answer each item with Yes/No/NA and provide justification.

### 1. Claims and Contributions
- [ ] Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?
- **Justification**: State which claims are supported by which experiments/theorems.

### 2. Limitations
- [ ] Does the paper discuss the limitations of the work performed by the authors?
- **Justification**: Point to the specific section (usually Section 5 or 6) where limitations are discussed.

### 3. Theory (if applicable)
- [ ] For each theoretical result, does the paper include the full set of assumptions and a complete (or correct) proof?
- **Justification**: Reference the theorem statements and appendix proofs. Mark N/A if no theoretical results.

### 4. Experiments Reproducibility
- [ ] Does the paper fully disclose all the information needed to reproduce the main experimental results?
- **Justification**: Describe what is disclosed (hyperparameters, random seeds, hardware, etc.).

### 5. Code and Data
- [ ] Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results?
- **Justification**: Provide URL (anonymized for review) or explain why code/data cannot be released.

### 6. Experimental Setup and Details
- [ ] Does the paper specify all the training and test details necessary to understand the results?
- **Justification**: Reference the experimental setup section and any appendix details.

### 7. Experiment Statistical Significance
- [ ] Does the paper report error bars (e.g., with respect to the random seed after running experiments multiple times)?
- **Justification**: Describe the number of runs, what error bars represent (std dev, confidence interval).

### 8. Compute Resources
- [ ] For each experiment, does the paper provide sufficient information on the computer resources needed to reproduce the experiments?
- **Justification**: Report GPU type, number of GPUs, training time, total compute cost.

### 9. Code of Ethics
- [ ] Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics?
- **Justification**: Confirm compliance or discuss any potential concerns.

### 10. Broader Impacts
- [ ] Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?
- **Justification**: Point to the broader impact statement or explain why impacts are minimal.

### 11. Safeguards
- [ ] Does the paper describe safeguards that have been put in place for responsible release of data or models with high risk for misuse?
- **Justification**: Describe safeguards or explain why they are not needed (N/A for most papers).

### 12. Licenses
- [ ] Are the creators or original owners of assets (e.g., code, data, models) properly credited and are the license and terms of use explicitly mentioned?
- **Justification**: List all assets used and their licenses.

### 13. New Assets
- [ ] Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?
- **Justification**: Describe documentation for any new datasets, models, or code released. N/A if no new assets.

### 14. Crowdsourcing and Human Subjects
- [ ] For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots (if applicable)?
- **Justification**: N/A for most ML papers. If applicable, describe IRB approval and consent process.

### 15. IRB Approvals
- [ ] Does the paper describe potential risks to subjects, whether any coverage was provided, and whether informed consent was obtained?
- **Justification**: N/A for most ML papers. If applicable, provide IRB protocol number.

### 16. LLM Declaration
- [ ] If the paper uses Large Language Models (LLMs) for writing assistance, does it declare the usage?
- **Justification**: Disclose any LLM usage for writing, coding, or experimental assistance.

---

## ICML Checklist

### Broader Impact Statement
- [ ] Include a broader impact statement (1 paragraph minimum)
- [ ] Discuss potential positive and negative societal consequences
- [ ] If the work has potential for misuse, discuss safeguards

### Reproducibility
- [ ] All hyperparameters specified
- [ ] Random seeds reported
- [ ] Error bars or confidence intervals on all main results
- [ ] Code submission (strongly encouraged, not mandatory)

### Statistical Reporting
- [ ] Multiple runs with different random seeds
- [ ] Standard deviations or confidence intervals reported
- [ ] Statistical significance tests for close comparisons

### Anonymization
- [ ] No author names in paper or metadata
- [ ] Self-citations in third person
- [ ] No links to identifiable code repositories
- [ ] No acknowledgment section during review

### Format Compliance
- [ ] Maximum 8 pages (excluding references and appendix)
- [ ] Uses official ICML style file
- [ ] Appendix allowed but reviewers are not required to read it

---

## ICLR Checklist

### LLM Disclosure Policy
- [ ] Declare any use of LLMs for writing assistance
- [ ] Specify which LLM was used and how
- [ ] Authors take full responsibility for the content

### Reproducibility Statement
- [ ] Include a reproducibility statement (typically in appendix or after conclusion)
- [ ] Cover: data availability, code availability, hyperparameter details, compute requirements

### Reciprocal Reviewing
- [ ] All authors expected to serve as reviewers (ICLR policy)
- [ ] Emergency reviewers may be assigned from the author pool

### OpenReview Process
- [ ] Paper is publicly visible on OpenReview during review (ICLR is open review)
- [ ] Authors can respond to reviews during the discussion period
- [ ] Revisions can be uploaded during the discussion period

### Format Compliance
- [ ] Maximum 9 pages for main content (excluding references and appendix)
- [ ] Uses official ICLR style file (based on the Master Template)
- [ ] Appendix allowed, no page limit for appendix

---

## ACL Checklist

### Limitations Section (Mandatory since ACL 2023)
- [ ] Include a dedicated "Limitations" section after the conclusion
- [ ] Discuss methodological limitations
- [ ] Discuss data limitations
- [ ] Discuss evaluation limitations
- [ ] This section does NOT count toward the page limit

### Responsible NLP Checklist
- [ ] Discuss potential biases in data and models
- [ ] Discuss privacy considerations if applicable
- [ ] Discuss dual-use concerns if applicable
- [ ] Consider impacts on underrepresented languages/communities

### Multilingual Considerations
- [ ] If the work is English-only, acknowledge this limitation
- [ ] If multilingual, describe the language coverage
- [ ] Consider typological diversity in language selection

### Ethics Statement
- [ ] Include an ethics statement if the work involves:
  - Human subjects or human data
  - Potential for harmful applications
  - Sensitive demographic data
  - Automated decision-making systems

### Format Compliance
- [ ] Long papers: maximum 8 pages (excluding references, appendices, limitations)
- [ ] Short papers: maximum 4 pages (excluding references, appendices, limitations)
- [ ] Uses official ACL style files (acl-org/acl-style-files)

---

## Universal Pre-Submission Checklist

Use this for any venue. Items are organized by category.

### Paper Content
- [ ] Abstract is self-contained, includes quantitative results
- [ ] Introduction clearly states the contribution
- [ ] Related work is comprehensive and fairly represents prior work
- [ ] Methods section enables reimplementation
- [ ] Experiments include proper baselines
- [ ] Results include error bars or statistical tests
- [ ] Limitations are discussed honestly
- [ ] Conclusion does not overstate findings

### Formatting
- [ ] Correct template/style file used
- [ ] Page limit respected
- [ ] References are complete (no missing fields)
- [ ] All figures and tables are referenced in text
- [ ] Figure and table captions are self-contained
- [ ] Consistent notation throughout
- [ ] No typos in author names, affiliations, or email addresses (camera-ready)

### Technical
- [ ] All claims are supported by experiments or proofs
- [ ] Experimental setup is fully described
- [ ] Hyperparameters are reported
- [ ] Compute resources are disclosed
- [ ] Datasets are properly cited
- [ ] Code availability is stated

### Reproducibility
- [ ] Random seeds reported
- [ ] Number of runs reported
- [ ] Standard deviations or confidence intervals included
- [ ] Data preprocessing steps described
- [ ] Model architecture fully specified
- [ ] Training procedure fully specified

### Ethics and Compliance
- [ ] No fabricated or cherry-picked results
- [ ] All citations verified (no hallucinated references)
- [ ] Proper attribution for all borrowed ideas, code, and data
- [ ] IRB approval if human subjects involved
- [ ] LLM usage declared if required by venue

### Final Checks
- [ ] Paper compiles cleanly from scratch
- [ ] PDF renders correctly
- [ ] All fonts embedded
- [ ] No editing markup (colored text, margin notes, TODO comments)
- [ ] Anonymization verified (for blind review)
- [ ] Supplementary materials packaged and complete
- [ ] Paper uploaded to correct submission track
- [ ] All co-authors have approved the submission

---

## Page Limits Quick Reference

| Venue | Main Paper | References | Appendix/Supplementary | Limitations |
|-------|-----------|------------|----------------------|-------------|
| NeurIPS | 9 pages | Unlimited (not counted) | Unlimited supplementary | Included in main or appendix |
| ICML | 8 pages | Unlimited (not counted) | Appendix allowed | Encouraged in broader impact |
| ICLR | 9 pages | Unlimited (not counted) | Appendix allowed, unlimited | Included in paper |
| ACL (Long) | 8 pages | Not counted | Not counted | Not counted (mandatory section) |
| ACL (Short) | 4 pages | Not counted | Not counted | Not counted (mandatory section) |
| AAAI | 7 pages + 1 for references | 1 page for references | 1 page supplementary (paid) | Recommended |
| COLM | 9 pages | Unlimited (not counted) | Appendix allowed | Included in paper |
| CVPR | 8 pages | Not counted | Supplementary allowed | Recommended |
| ECCV | 14 pages | Included in page count | Supplementary allowed | Recommended |
| EMNLP (Long) | 8 pages | Not counted | Not counted | Not counted (mandatory) |
| NAACL (Long) | 8 pages | Not counted | Not counted | Not counted (mandatory) |

**Note**: Page limits may change year to year. Always verify with the current call for papers.
