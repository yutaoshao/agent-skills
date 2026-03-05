# LaTeX Paper Quality Checklist

Structured checklist for ensuring LaTeX paper quality before submission. Items are organized by priority. Covers both journal and conference submissions.

---

## Compilation (Critical)

- [ ] Paper compiles without errors using the full pipeline: `pdflatex -> bibtex -> pdflatex -> pdflatex`
- [ ] Alternative: `latexmk -pdf main.tex` completes without errors
- [ ] No undefined references (`\ref` or `\cite` warnings in log)
- [ ] No multiply-defined labels
- [ ] All figures exist at their referenced paths
- [ ] Bibliography compiles: all `\cite` keys match entries in `.bib` file
- [ ] No "Citation undefined" warnings in `.log` file
- [ ] No "Reference undefined" warnings in `.log` file
- [ ] All packages resolve correctly (no missing `.sty` files)
- [ ] Output PDF is the correct number of pages

## References and Cross-References

- [ ] Every `\label{...}` has at least one corresponding `\ref{...}` or `\eqref{...}`
- [ ] No orphan labels (defined but never referenced)
- [ ] No orphan citations (in `.bib` but never `\cite`'d) -- some venues reject unused bib entries
- [ ] No duplicate citation keys
- [ ] `~` (non-breaking space) before `\cite{}` and `\ref{}` to prevent line breaks
  ```latex
  % GOOD
  as shown in Fig.~\ref{fig:pipeline}
  previous work~\cite{craig2005robotics}
  ```
- [ ] Equation references use `\eqref` or `Eq.~(\ref{})` consistently (not mixing styles)
- [ ] Figure references use consistent abbreviation: "Fig." in mid-sentence, "Figure" at sentence start
- [ ] Table references: "Table" (not abbreviated per most style guides)
- [ ] Section references: "Section" or "Sec." -- consistent throughout
- [ ] Algorithm references: "Algorithm" -- not abbreviated
- [ ] Appendix references: "Appendix" or "App." -- consistent throughout
- [ ] Citation style matches venue requirements (natbib, biblatex, numeric, author-year)

## Typography and Formatting

- [ ] Em-dash `---` for parenthetical asides (not `-` or `--`)
- [ ] En-dash `--` for ranges: "pages 1--10", "2020--2024"
- [ ] Hyphen `-` only for compound words: "multi-hypothesis", "error-driven"
- [ ] Consistent number formatting: thousands separator, decimal places
- [ ] Math mode for all variables, even inline: $K$, $N$, not K or N
- [ ] Vectors in bold: `\bm{q}` or `\boldsymbol{q}` -- consistent throughout
- [ ] Matrices in bold capital: `\bm{R}`, `\bm{J}`
- [ ] Sets in calligraphic: `\mathcal{S}`, `\mathcal{D}`
- [ ] Abbreviations defined on first use: "particle swarm optimization (PSO)"
- [ ] No orphan abbreviations (used before being defined)
- [ ] Consistent use of Oxford comma (or consistent omission)
- [ ] No double spaces in source (may cause irregular spacing in output)
- [ ] Proper use of `\text{}` inside math mode for non-variable text
- [ ] Percentage: "5\%" not "5 %" (no space before percent in most styles)
- [ ] Footnotes end with a period

## Figures

- [ ] All figures are vector format (PDF) or high-resolution raster (300+ DPI)
- [ ] Figure text is readable at print size (minimum ~8pt after scaling)
- [ ] Color choices are distinguishable in grayscale (for print)
- [ ] Color choices are colorblind-safe (see `references/color-palettes.md`)
- [ ] Every figure is referenced in the text with `\ref{fig:...}`
- [ ] Figure captions are self-contained (reader can understand without reading body text)
- [ ] Consistent style across all figures (font, colors, line styles, axis labels)
- [ ] TikZ diagrams: labels match paper terminology exactly
- [ ] TikZ diagrams: architectural details (activation functions, normalization) included
- [ ] Subfigures use `\subcaption` or `\subfloat` with (a), (b) labels
- [ ] Figure placement: `[t]` or `[h!]` preferred over `[H]` (which can cause issues)
- [ ] No figures extend beyond column/page margins
- [ ] Axis labels include units where applicable
- [ ] Legend does not obscure data points
- [ ] Figure 1 (the "hero figure") is especially polished -- reviewers see it first

## Tables

- [ ] Use `\toprule`, `\midrule`, `\bottomrule` from booktabs (no vertical lines)
- [ ] Best results indicated with `\textbf{}` (bold)
- [ ] Second-best indicated with `\underline{}` where applicable
- [ ] Column alignment: numbers right-aligned or decimal-aligned
- [ ] Units in column headers, not repeated in every cell
- [ ] Table captions are above the table (standard convention)
- [ ] Every table is referenced in the text
- [ ] Table data matches numbers reported in the text
- [ ] Standard deviation / confidence intervals included where appropriate
- [ ] Table fits within column/page width (use `\resizebox` or `\small` if needed)
- [ ] Consistent number of decimal places within each column

## Equations

- [ ] All important equations are numbered
- [ ] Equations referenced in text use `\eqref` for parenthetical format
- [ ] Punctuation after displayed equations: comma if sentence continues, period if it ends
- [ ] Consistent notation for common operations:
  - Transpose: $^\top$ or $^T$ (pick one)
  - Norm: $\|\cdot\|$
  - Expectation: $\mathbb{E}$
  - Probability: $\mathbb{P}$ or $P$
  - Real numbers: $\mathbb{R}$
- [ ] `\left(` and `\right)` for auto-sizing delimiters around tall expressions
- [ ] No equation overflows into margins (break long equations with `aligned` or `multline`)
- [ ] Consistent use of `\cdot` vs `\times` for multiplication
- [ ] Variables defined before or immediately after first use in equation

## Content Quality

- [ ] Abstract is self-contained (no citations, no undefined abbreviations, no `\ref{}`)
- [ ] Abstract includes quantitative results (specific numbers, not "significant improvement")
- [ ] Keywords match venue conventions (typically 4-6)
- [ ] No single-subsection sections (if 3.1 exists, 3.2 must exist)
- [ ] Consistent tense: methods in present, experiments/results in past
- [ ] No first-person singular ("I") in multi-author papers
- [ ] Author contributions statement included if required
- [ ] Acknowledgments section present if required
- [ ] All datasets properly cited
- [ ] All code/software dependencies cited
- [ ] Limitations discussed honestly

## Common Warnings to Address

| Warning | Cause | Fix |
|---------|-------|-----|
| `Overfull \hbox` | Line too wide | Reword, add `\allowbreak`, adjust tables/equations |
| `Underfull \hbox` | Paragraph too sparse | Usually ignorable unless badness > 5000 |
| `Float too large for page` | Figure/table exceeds page height | Reduce size or use `[p]` placement |
| `Citation X undefined` | Missing `.bib` entry or misspelled key | Check cite key spelling, run bibtex |
| `Label X multiply defined` | Two `\label{}` with same key | Rename one label |
| `Package hyperref Warning: Token not allowed in a PDF string` | Special chars in section titles | Use `\texorpdfstring{}{}` |
| `Font shape not available` | Missing font | Install font or use alternative |

## Conference-Specific Checks

### Anonymization (Double-Blind Review)

- [ ] No author names or affiliations in the paper
- [ ] No identifying information in headers/footers
- [ ] `\usepackage[anonymous]{...}` or equivalent flag enabled
- [ ] Self-citations in third person: "Smith et al. [1] showed..." not "We showed in our previous work [1]..."
- [ ] No identifiable information in figure metadata (check PDF properties)
- [ ] No acknowledgments mentioning specific grants (save for camera-ready)
- [ ] Code/data links anonymized (use anonymous GitHub, Anonymous Submission on OpenReview)
- [ ] PDF metadata clean: `\hypersetup{pdfauthor={}, pdftitle={...}}`
- [ ] File name does not contain author names

### Page Limits

- [ ] Main paper within page limit (excluding references for most venues)
- [ ] Appendix/supplementary within supplementary page limit
- [ ] References formatted correctly (some venues exclude references from page count, others do not)

### Mandatory Checklists

- [ ] NeurIPS: Paper checklist filled out (16 items) -- see `references/conference-checklists.md`
- [ ] ICML: Broader impact statement included
- [ ] ICLR: Reproducibility statement included
- [ ] ACL: Limitations section included (mandatory since 2023)

### Broader Impact / Ethics

- [ ] Broader impact statement if required by venue
- [ ] Ethics statement if working with human data
- [ ] IRB approval noted if applicable
- [ ] Potential negative societal impacts discussed
- [ ] LLM usage declaration if required (NeurIPS, ICLR)

## Pre-Submission Final Checks

- [ ] Page count within venue limits
- [ ] Author information matches submission system (or anonymized for review)
- [ ] Supplementary materials referenced correctly from main paper
- [ ] All TODO/FIXME/XXX comments removed from source
- [ ] No commented-out text or debug content
- [ ] No `\textcolor{red}{...}` or other editing markup
- [ ] PDF metadata is clean (no author info in anonymous review)
- [ ] Filename follows venue conventions
- [ ] Paper compiles from a clean directory (no stale auxiliary files)
- [ ] PDF opens correctly in multiple viewers
- [ ] All fonts embedded in PDF (`pdffonts main.pdf` shows no non-embedded fonts)
- [ ] File size within venue limits (typically <50MB for main paper)
- [ ] Supplementary code/data packaged and anonymized
- [ ] Camera-ready: update author block, acknowledgments, remove anonymization flags
