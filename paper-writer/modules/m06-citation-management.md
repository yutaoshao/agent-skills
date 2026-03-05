# Module 06: Citation Management

Anti-hallucination citation verification and expansion workflow. This module ensures every reference in the paper is real, correctly attributed, and naturally integrated.

## CRITICAL WARNING

AI-generated citations have an approximately 40% error rate. Common failures include fabricated paper titles, wrong author lists, non-existent DOIs, incorrect publication years, and citations attributed to the wrong venue. A single hallucinated reference discovered by a reviewer can undermine the credibility of the entire paper. This module exists specifically to prevent that outcome.

## The Golden Rule

**NEVER generate BibTeX entries from memory.** Every BibTeX entry must be programmatically fetched from a verified source (Semantic Scholar API, CrossRef via DOI, DBLP, arXiv, or the publisher's export function). If a reference cannot be verified through at least two independent sources, it must be marked as a placeholder until the user confirms it manually.

## 5-Step Verification Workflow

Every citation added to the paper must pass through all five steps. No exceptions.

### Step 1: Search

Use programmatic search tools to locate the paper:

- **Primary**: Semantic Scholar API or `mcp__exa__web_search_exa` for academic paper search.
- **Secondary**: `WebSearch` with targeted queries: `"exact paper title" author:LastName site:semanticscholar.org OR site:arxiv.org`.
- **Tertiary**: DBLP (`dblp.org/search?q=...`) for computer science venues.

Search queries should include the exact title when known, or a combination of author names, key terms, venue, and year. Avoid vague queries that return ambiguous results.

```
Example search progression:
1. "Attention Is All You Need" Vaswani 2017
2. If no result: "transformer self-attention mechanism" Vaswani NIPS 2017
3. If still no result: search by DOI if available
```

### Step 2: Verify Existence in 2+ Sources

The paper must appear in at least two independent sources before it can be cited. Acceptable source combinations:

- Semantic Scholar + arXiv
- DBLP + publisher website (IEEE Xplore, ACM DL, Springer, Elsevier)
- Google Scholar + DOI resolution (doi.org redirect)
- CrossRef API + publisher page

Cross-check the following fields across sources:
- Paper title (exact match, accounting for capitalization differences)
- Author list (all authors, not just first author)
- Publication year
- Venue (journal name or conference name)

If the paper appears in only one source and cannot be independently verified, mark it as a placeholder (see Placeholder Marking below).

### Step 3: Retrieve BibTeX via DOI

Once verified, obtain the BibTeX entry programmatically:

- **Best method**: Fetch BibTeX from DOI using CrossRef.
  ```bash
  curl -LH "Accept: application/x-bibtex" https://doi.org/10.xxxx/xxxxx
  ```
- **Alternative**: Export BibTeX from Semantic Scholar, DBLP, or the publisher's page.
- **For arXiv papers**: Use the arXiv BibTeX export or construct from the arXiv metadata page.

Never manually type a BibTeX entry from memory. If automated retrieval fails, copy the BibTeX directly from the publisher's export function.

### Step 4: Validate Claim Appears in Paper

Before citing a paper to support a specific claim, verify that the cited paper actually contains the claimed information:

- Read the abstract and relevant sections of the cited paper (via Semantic Scholar abstract, arXiv PDF, or publisher preview).
- Confirm the specific claim, method, or result you are citing is actually present in that paper.
- If citing a specific number (e.g., "achieved 95% accuracy"), verify that number appears in the cited paper.

Common errors to catch:
- Citing paper A for a result that actually comes from paper B.
- Citing a paper for a method it merely references but did not propose.
- Attributing a dataset to the wrong paper.

### Step 5: Add to .bib

Add the verified BibTeX entry to the `.bib` file with the following quality standards applied (see BibTeX Quality Standards below). Then integrate the `\cite{}` command into the paper text using natural integration strategies.

## Placeholder Marking

When a citation cannot be fully verified through the 5-step workflow, mark it clearly so the user knows it requires manual verification before submission.

### LaTeX Placeholder Formats

For unverified citations in the `.tex` file:

```latex
% Option 1: Inline placeholder (visible in compiled PDF)
Recent work on neural architecture search [CITATION NEEDED: author2024title] has shown...

% Option 2: Cite key with verification flag
Recent work on neural architecture search~\cite{PLACEHOLDER_author2024title} has shown...

% Option 3: Comment-based placeholder (invisible in compiled PDF but visible in source)
Recent work on neural architecture search~\cite{author2024title} % UNVERIFIED: could not find in Semantic Scholar
```

For placeholder entries in the `.bib` file:

```bibtex
% PLACEHOLDER -- NEEDS VERIFICATION
% Could not verify: searched Semantic Scholar, DBLP, Google Scholar on 2024-01-15
@article{PLACEHOLDER_author2024title,
  title     = {Approximate Title From Memory},
  author    = {Author, First},
  year      = {2024},
  note      = {PLACEHOLDER -- VERIFY BEFORE SUBMISSION}
}
```

After processing all citations, provide the user with a summary of all placeholders using the Template C format from SKILL.md:

```
I've marked [N] citations as placeholders that need verification:
- [paper description] -- could not find in Semantic Scholar
- [paper description] -- found similar paper but different authors
Please verify these before submission.
```

## Citation Gap Analysis

Analyze the paper's existing citations for completeness across four dimensions. This analysis should be performed after the initial draft is complete and again before submission.

### Temporal Coverage

- Count references by publication year.
- At least 30% of references should be from the last 3 years (recent work).
- Identify decade-long gaps: if the paper uses techniques from the 2000s, there should be both the original foundational reference and recent follow-up work.
- Flag any section that cites only older papers (pre-2020) without acknowledging recent developments.

### Methodological Coverage

- Every method, algorithm, loss function, or architectural component borrowed from prior work must cite its canonical paper.
- Optimization methods (Adam, SGD, etc.) need citations.
- Non-standard evaluation metrics need citations.
- Each baseline or comparison method must cite its original paper, not a secondary source.

### Foundational Coverage

- Classic references for the core techniques used (e.g., backpropagation, attention mechanism, reinforcement learning foundations).
- At least one survey or review paper for the primary research area.
- Seminal papers that defined the problem space.

### Claim Support

- Every factual claim requires a citation. Scan each section for unsupported assertions:
  - "X is widely used in..." -- cite evidence of widespread use.
  - "Traditional methods suffer from..." -- cite specific traditional methods and their limitations.
  - "Recent advances have shown..." -- cite the specific advances.
- Performance comparisons must cite the source of the compared numbers.
- Statistical claims ("significantly better") must reference the statistical test used.

## Target Reference Counts

| Paper Type | Target Total References | Minimum Recent (last 3 years) | Minimum Per Section |
|-----------|------------------------|-------------------------------|---------------------|
| Letter / Short Paper | 20-30 | 8-10 (~30%) | 2-3 |
| Full Research Paper | 35-50 | 12-18 (~35%) | 3-5 |
| Survey / Review Paper | 80-150+ | 30+ (~25%) | 5-10 |

When the target venue is known, verify expected reference counts by examining 3-5 recent papers published at that venue.

## Natural Citation Integration Strategies

### Inline Narrative Citation

Weave the reference into the sentence as an active part of the argument. The cited work performs an action or demonstrates a result.

```latex
% GOOD: Citation as subject or active participant
Vaswani et al.~\cite{vaswani2017attention} introduced the transformer architecture,
which replaced recurrence with multi-head self-attention.

% GOOD: Citation integrated into comparative discussion
Unlike IKFlow~\cite{ames2022ikflow}, which uses normalizing flows for inverse kinematics,
our approach directly optimizes in the joint space.
```

### Parenthetical Support Citation

Add a citation to provide evidence for a claim already stated. The sentence should read naturally without the citation.

```latex
% GOOD: Citation supports the claim
PSO convergence theory has been extensively studied in both
continuous~\cite{clerc2002particle} and discrete~\cite{kennedy1997discrete} domains.

% GOOD: Multiple citations grouped logically
Neural network approaches to inverse kinematics have gained
traction~\cite{ames2022ikflow, jiang2022nn_nr, bensadoun2022neural}.
```

### Contrastive Citation

Introduce a reference to highlight a difference, limitation, or contrast with the current work.

```latex
% GOOD: Explicit contrast
Where prior work~\cite{wang2023method} requires labeled training data,
our method operates in a fully unsupervised setting.
```

## Citation Anti-Patterns

### Citation Dumping

Adding a cluster of citations at the end of a paragraph without contextualizing any of them.

```latex
% BAD: Citation dump
Many methods have been proposed for this problem~\cite{a,b,c,d,e,f,g}.

% GOOD: Contextualized citations
Methods for this problem span optimization-based~\cite{a,b},
learning-based~\cite{c,d}, and hybrid~\cite{e,f} approaches.
```

### Orphan Citations

A paper appears in the `.bib` file and is `\cite`'d but is never discussed or contextualized in the text.

### Disconnected Citations

A citation is placed in a context unrelated to the cited paper's actual contribution. This often results from AI hallucination or careless copy-pasting.

## Citation Format Support

### IEEE Style (Numbered)

```latex
\usepackage[numbers,sort&compress]{natbib}
% or
\bibliographystyle{IEEEtran}

% Usage: [1], [2], [1]-[5]
as shown in~\cite{vaswani2017attention}  % renders as [1]
```

### APA / Author-Year Style

```latex
\usepackage{natbib}
\bibliographystyle{apalike}

% Usage:
\citet{vaswani2017attention}  % Vaswani et al. (2017)
\citep{vaswani2017attention}  % (Vaswani et al., 2017)
\citeauthor{vaswani2017attention}  % Vaswani et al.
\citeyear{vaswani2017attention}  % 2017
```

### Common natbib Commands

| Command | Output (author-year) | Output (numbered) |
|---------|---------------------|-------------------|
| `\citet{key}` | Vaswani et al. (2017) | Vaswani et al. [1] |
| `\citep{key}` | (Vaswani et al., 2017) | [1] |
| `\citet*{key}` | Vaswani, Shazeer, ... (2017) | Vaswani, Shazeer, ... [1] |
| `\citep[see][]{key}` | (see Vaswani et al., 2017) | (see [1]) |
| `\citealt{key}` | Vaswani et al. 2017 | 1 |

## BibTeX Quality Standards

Every BibTeX entry in the `.bib` file must meet these standards:

### Required Fields

- **author**: Complete author list. Use `{LastName, FirstName}` format. Never abbreviate to "et al." in the `.bib` file; let LaTeX handle abbreviation in the output.
- **title**: Full title with correct capitalization. Protect proper nouns and acronyms with braces: `{ImageNet}`, `{BERT}`, `{GPU}`.
- **year**: Four-digit publication year.
- **journal** or **booktitle**: Full name, not abbreviated (unless the journal itself uses an abbreviation as its official name). Use `{Proceedings of the International Conference on Machine Learning}` not `{ICML}`.

### Strongly Recommended Fields

- **volume** and **pages**: For journal articles, these are essential for locating the paper.
- **doi**: Digital Object Identifier. Enables direct linking and permanent identification.
- **publisher**: Required for books and conference proceedings.
- **number** or **issue**: For journal articles when available.

### Formatting Consistency

- Use consistent cite key format throughout: `authorYEARkeyword` (e.g., `vaswani2017attention`).
- Maintain consistent field ordering across entries.
- Use braces `{}` for field values, not quotes `""`.
- Protect capitalization in titles with braces where needed:
  ```bibtex
  title = {Attention is All You Need},  % "You" may be lowercased
  title = {{Attention} is All You Need},  % "Attention" stays capitalized
  ```

### Common BibTeX Errors to Avoid

- Missing closing braces in author fields with institutional authors.
- Inconsistent author name formats (mixing "First Last" with "Last, First").
- Using `month = {June}` instead of `month = jun` (the latter is a BibTeX string, not a literal).
- Duplicate entries with slightly different keys referencing the same paper.

## Post-Processing Verification

After all citations have been added, perform a final verification pass:

1. **Compile check**: Run `bibtex` and check for warnings about undefined citations or unused entries.
2. **Orphan scan**: Every entry in `.bib` should have at least one `\cite` in the `.tex` file.
3. **Reverse orphan scan**: Every `\cite` in the `.tex` file should have a corresponding `.bib` entry.
4. **Duplicate check**: No two `.bib` entries should reference the same paper.
5. **Placeholder scan**: Search for all `PLACEHOLDER`, `CITATION NEEDED`, and `UNVERIFIED` markers and report them to the user.
6. **Recent ratio check**: Calculate the percentage of references from the last 3 years and report whether the target is met.
