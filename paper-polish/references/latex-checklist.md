# LaTeX Paper Quality Checklist

Structured checklist for ensuring LaTeX paper quality before journal submission. Items are organized by priority.

## Compilation (Critical)

- [ ] Paper compiles without errors using the full pipeline: `pdflatex -> bibtex -> pdflatex -> pdflatex`
- [ ] No undefined references (`\ref` or `\cite` warnings in log)
- [ ] No multiply-defined labels
- [ ] All figures exist at their referenced paths
- [ ] Bibliography compiles: all `\cite` keys match entries in `.bib` file
- [ ] No "Citation undefined" warnings in `.log` file

## References and Cross-References

- [ ] Every `\label{...}` has at least one corresponding `\ref{...}` or `\eqref{...}`
- [ ] No orphan labels (defined but never referenced)
- [ ] No orphan citations (in `.bib` but never `\cite`'d) -- some journals reject unused bib entries
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

## Typography and Formatting

- [ ] Em-dash `---` for parenthetical asides (not `-` or `--`)
- [ ] En-dash `--` for ranges: "pages 1--10", "2020--2024"
- [ ] Hyphen `-` only for compound words: "multi-hypothesis", "error-driven"
- [ ] Consistent number formatting: thousands separator, decimal places
- [ ] Math mode for all variables, even inline: $K$, $N$, not K or N
- [ ] Vectors in bold: `\bm{q}` or `\boldsymbol{q}` -- consistent throughout
- [ ] Matrices in bold capital: `\bm{R}`, `\bm{J}`
- [ ] Abbreviations defined on first use: "particle swarm optimization (PSO)"
- [ ] No orphan abbreviations (used before being defined)

## Figures

- [ ] All figures are vector format (PDF) or high-resolution raster (300+ DPI)
- [ ] Figure text is readable at print size (minimum ~8pt)
- [ ] Color choices are distinguishable in grayscale (for print journals)
- [ ] Every figure is referenced in the text with `\ref{fig:...}`
- [ ] Figure captions are self-contained (reader should understand the figure from caption alone)
- [ ] Consistent style across all figures (font, colors, line styles)
- [ ] TikZ diagrams: labels match paper terminology exactly
- [ ] TikZ diagrams: architectural details (activation functions, normalization) included
- [ ] Subfigures use `\subcaption` with (a), (b) labels

## Tables

- [ ] Use `\toprule`, `\midrule`, `\bottomrule` from booktabs (no vertical lines)
- [ ] Best results indicated with `\textbf{}` (bold)
- [ ] Second-best indicated with `\underline{}` where applicable
- [ ] Column alignment: numbers right-aligned or decimal-aligned
- [ ] Units in column headers, not repeated in every cell
- [ ] Table captions are above the table (standard convention)
- [ ] Every table is referenced in the text

## Equations

- [ ] All important equations are numbered
- [ ] Referenced equations use `\eqref` for parenthetical format
- [ ] Punctuation after displayed equations: comma if sentence continues, period if it ends
- [ ] Consistent notation for common operations: transpose ($^T$ or $^\top$), norm ($\|\cdot\|$)
- [ ] `\left(` and `\right)` for auto-sizing delimiters around tall expressions

## Content Quality

- [ ] Abstract is self-contained (no citations, no undefined abbreviations)
- [ ] Abstract includes quantitative results (specific numbers)
- [ ] Keywords match journal conventions (typically 4-6)
- [ ] No single-subsection sections (if 3.1 exists, 3.2 must exist)
- [ ] Consistent tense: methods in present, experiments/results in past
- [ ] No first-person singular ("I") in multi-author papers
- [ ] Declaration of competing interest included
- [ ] Acknowledgments section present if required

## Common Warnings to Address

- `Overfull \hbox`: Line too wide. Fix with rewording, `\allowbreak`, or adjusting tables/equations.
- `Underfull \hbox`: Paragraph too sparse. Usually ignorable unless badness > 5000.
- `Float too large for page`: Figure/table exceeds page height. Reduce size or use `[p]` placement.
- `Citation X undefined`: Missing `.bib` entry or misspelled cite key.
- `Label X multiply defined`: Two `\label{}` with the same key.

## Pre-Submission Final Checks

- [ ] Page count within journal limits
- [ ] Author information matches submission system
- [ ] Supplementary materials referenced correctly
- [ ] All TODO/FIXME comments removed from source
- [ ] No commented-out text or debug content
- [ ] PDF metadata is clean (no author info in anonymous review)
- [ ] Filename follows journal conventions
