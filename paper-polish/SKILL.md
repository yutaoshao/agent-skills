---
name: paper-polish
description: This skill should be used when working on academic LaTeX papers that need quality improvement before journal submission. It provides workflows for removing AI-flavored writing patterns, expanding citations, verifying figures and tables, fixing LaTeX compilation issues, and conducting overall quality reviews. Triggers on requests to polish, review, improve, or prepare a LaTeX paper for submission.
---

# Paper Polish

Automate academic paper improvement for LaTeX submissions. This skill provides six modular workflows that can be invoked individually or combined into a full pre-submission review.

## Workflow Decision Tree

Determine which workflow(s) to invoke based on the request:

- Request mentions "de-AI", "AI writing", "natural writing", "polish text" --> **Module 1: De-AI Polishing**
- Request mentions "citations", "references", "bibliography" --> **Module 2: Citation Expansion**
- Request mentions "figures", "TikZ", "diagrams", "plots" --> **Module 3: Figure/Diagram Check**
- Request mentions "tables", "data", "numbers", "results" --> **Module 4: Table Verification**
- Request mentions "compile", "build", "warnings", "errors" --> **Module 5: LaTeX Compilation**
- Request mentions "review", "full check", "submission ready" --> **Module 6: Full Quality Review** (runs all modules)
- When uncertain, start with Module 6 to identify which areas need attention.

## Module 1: De-AI Text Polishing

Remove AI-flavored writing patterns and produce natural academic prose. This is the most impactful module for papers drafted with AI assistance.

### Procedure

1. Read the full `.tex` file to understand the paper scope and domain.
2. Load `references/de-ai-patterns.md` for the comprehensive pattern catalog.
3. Scan **Introduction**, **Discussion**, and **Conclusion** sections first (highest AI pattern density), then Related Work and Method sections.
4. For each section, identify and fix patterns in priority order:
   - **Structural patterns**: Remove `\textbf{Category.}` paragraph labels that create a mechanical listing feel. Convert bullet-list-style paragraphs into flowing prose with natural transitions.
   - **Vocabulary patterns**: Replace overused AI words (furthermore, moreover, notably, leveraging, harnessing, crucial, comprehensive, etc.) with domain-appropriate alternatives.
   - **Transition patterns**: Replace mechanical connectors ("Additionally,", "Furthermore,") with logical connectors that reflect actual argumentative relationships (contrast, causation, concession, elaboration).
   - **Hedging patterns**: Fix excessive hedging ("It is worth noting that") and remove filler phrases.
   - **Sentence structure**: Break up formulaic sentence patterns (subject-verb-object monotony, identical sentence openers).
5. Preserve all technical content, equations, citations, and LaTeX commands exactly.
6. After editing, re-read each modified section to verify coherence and flow.

### Quality Criteria

- No paragraph begins with a bold label followed by a period (e.g., `\textbf{X.}`)
- No two consecutive paragraphs start with the same transition word
- Discussion section reads as connected argumentation, not a list of observations
- Conclusion does not mechanically mirror the Introduction structure

## Module 2: Citation Expansion

Analyze citation coverage and integrate new references to meet journal expectations (typically 30-50 for a full research paper).

### Procedure

1. Read `references.bib` and count total references. Read the `.tex` file to map where each citation appears.
2. Load `references/citation-guide.md` for expansion methodology.
3. Identify citation gaps by analyzing:
   - **Temporal coverage**: Ensure recent works (last 2-3 years) are well-represented.
   - **Methodological coverage**: Each baseline or comparison method should cite its canonical reference.
   - **Foundational coverage**: Classic references for each technique used (optimization, neural networks, domain-specific).
   - **Claim support**: Every factual claim or performance comparison should have a citation.
4. For each gap, use `WebSearch` to find high-quality candidates (peer-reviewed journals, top conferences).
5. Add new BibTeX entries to `references.bib` with complete metadata (volume, pages, DOI when available).
6. Integrate citations naturally into existing sentences -- avoid citation-dumping (adding `\cite{a,b,c}` at the end of a sentence without context). Each new citation should be woven into the narrative.
7. After adding, verify: no orphan citations (cited but not in .bib), no unused .bib entries (in .bib but never cited), no duplicate keys.

### Target Metrics

- Total references: 30+ for letters/short papers, 40+ for full research papers
- Recent references (last 3 years): at least 30% of total
- Each section should have at least 2-3 citations

## Module 3: Figure/Diagram Quality Check

Verify visual elements for correctness, consistency with text, and publication quality.

### Procedure

1. Identify all figures referenced in the `.tex` file via `\includegraphics` and `\begin{tikzpicture}`.
2. For standalone TikZ files (`.tex` files in `figures/` directory):
   a. Read each TikZ source file completely.
   b. Cross-reference all labels, node text, and annotations against the paper text.
   c. Verify technical accuracy: method names, variable names, and mathematical notation must match the paper.
   d. Check architectural details: all components mentioned in the text (e.g., activation functions, normalization layers) should appear in the diagram.
   e. Identify common errors: mismatched method names, missing annotations, wrong dimensions.
3. For matplotlib/programmatic figures (PDF/PNG files):
   a. Verify the figure exists and is referenced correctly.
   b. Cross-check figure captions against what the text claims about the figure.
   c. Verify axis labels, legends, and units are consistent with the paper.
4. Check all `\ref{fig:...}` references resolve correctly.
5. Verify figure numbering is sequential and no figure is defined but never referenced.

### Common TikZ Issues

- Node labels not matching paper terminology
- Missing architectural annotations (activation functions, normalization)
- Color inconsistency between related diagrams
- Precision annotations not matching reported experimental numbers

## Module 4: Table Data Verification

Cross-check numerical data in paper tables against source data files.

### Procedure

1. Identify all tables in the `.tex` file.
2. Locate potential data source files: JSON results files, CSV data, Python scripts that generate results. Search the project directory recursively for `results/`, `data/`, `output/` directories.
3. For each table:
   a. Parse the LaTeX table to extract all numerical values.
   b. Find the corresponding source data (e.g., `results/comparison_results.json`).
   c. Verify each number matches the source within reasonable rounding.
   d. Check that bold/underline formatting correctly indicates best/second-best values.
   e. Verify units are consistent between table headers and the text.
4. Flag any discrepancies with the exact table cell location and expected vs. actual values.
5. Check table captions for accuracy and completeness.

## Module 5: LaTeX Compilation and Cleanup

Ensure clean compilation and fix common LaTeX issues.

### Procedure

1. Load `references/latex-checklist.md` for the full checklist.
2. Attempt compilation: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
3. Parse the `.log` file for:
   - **Errors**: Fix any compilation errors before proceeding.
   - **Warnings**: Address undefined references, multiply-defined labels, overfull/underfull hboxes.
   - **Missing citations**: `Citation 'X' undefined` warnings.
4. Check for common issues:
   - Orphan `\label{}` tags (defined but never `\ref`'d)
   - Duplicate labels
   - Figures/tables floating far from their first reference
   - Consistent use of `~` before `\cite` and `\ref` to prevent line breaks
   - Em-dash (`---`) vs. en-dash (`--`) usage
5. Verify the bibliography compiles correctly and all entries appear in the output.

## Module 6: Full Quality Review

Comprehensive pre-submission review combining all modules plus structural analysis.

### Procedure

1. Run Modules 1-5 in sequence.
2. Additionally check:
   - **Abstract**: Complete, self-contained, includes quantitative results, within word limit.
   - **Keywords**: 4-6 keywords, matching journal conventions.
   - **Section structure**: Logical flow, no orphan subsections (a single subsection under a section).
   - **Notation consistency**: Same symbol used for the same concept throughout (e.g., do not switch between `\mathbf{q}` and `\boldsymbol{q}`).
   - **Tense consistency**: Abstract in present/past tense, methods in present, results in past.
   - **Journal formatting**: Check against target journal template requirements.
   - **Declarations**: Competing interests, data availability, acknowledgments present as required.
3. Produce a structured report with findings organized by severity (error/warning/suggestion).

## Reference Files

- `references/de-ai-patterns.md` -- Comprehensive catalog of 50+ AI writing antipatterns with detection heuristics and replacement strategies. Load when executing Module 1.
- `references/latex-checklist.md` -- 80+ item checklist for LaTeX paper quality. Load when executing Module 5 or Module 6.
- `references/citation-guide.md` -- Citation expansion methodology including gap analysis framework, quality criteria for references, and integration techniques. Load when executing Module 2.
