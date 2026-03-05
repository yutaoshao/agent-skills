# Module 08: LaTeX Compilation

LaTeX template setup, compilation pipeline management, and quality verification. This module ensures the paper compiles cleanly, follows the target venue's formatting requirements, and passes a comprehensive checklist before proceeding to submission.

## Template Setup Workflow

Setting up a conference or journal template correctly is the foundation for a clean paper. Follow these six steps exactly, in order.

### Step 1: Copy the Full Template Directory

Download and copy the entire template package, not just the main `.tex` file. Conference templates include `.sty` files, `.cls` files, `.bst` bibliography styles, example figures, and sometimes required supplementary files.

```bash
# GOOD: Copy the entire directory
cp -r neurips_2024_template/ my_paper/

# BAD: Copy only the main file
cp neurips_2024_template/neurips_2024.tex my_paper/main.tex  # MISSING DEPENDENCIES
```

### Step 2: Verify the Template Compiles As-Is

Before making any changes, compile the unmodified template to confirm it works in your environment.

```bash
cd my_paper/
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

If the template does not compile, fix the environment issue (missing packages, outdated TeX distribution) before proceeding. Do not attempt to modify the template to work around environment problems.

### Step 3: Read the Example Content

Read the template's example content carefully. It often contains:
- Required formatting instructions (page limits, font sizes, margin requirements).
- Examples of how to use custom commands defined in the `.sty` file.
- Required sections or statements (e.g., NeurIPS requires a broader impact section).
- Comments explaining formatting conventions specific to that venue.

### Step 4: Replace Content Section by Section

Replace the template content one section at a time, compiling after each replacement to catch errors immediately.

```
Replacement order:
1. Title and author block (or anonymous placeholder for blind review)
2. Abstract
3. Introduction
4. Methods / Approach
5. Experiments / Results
6. Related Work
7. Conclusion
8. Appendix / Supplementary
9. Bibliography
```

After replacing each section, compile and verify:
- No new errors or warnings introduced.
- Page layout has not shifted unexpectedly.
- Cross-references still resolve.

### Step 5: Keep Template Comments as Reference

Do not delete the template's comments and formatting instructions until the paper is finalized. They serve as a reference for formatting decisions and required sections.

```latex
% NeurIPS requires: The paper should be 9 pages including figures and tables,
% with an optional 10th page for references only.
% DELETE THIS COMMENT BEFORE SUBMISSION
```

### Step 6: Clean Up at the End

Only after the paper is content-complete and verified:
- Remove all template example text and comments.
- Remove unused package imports.
- Remove any `\usepackage` that was part of the template example but is not used by your paper.
- Verify one final time that the paper compiles cleanly.

## Template Pitfalls

These are common mistakes that cause hours of debugging. Avoid all of them.

### Do Not Copy Only main.tex

Conference templates depend on `.cls` and `.sty` files that define the formatting. Copying only the `.tex` file will produce compilation errors or incorrect formatting.

### Do Not Modify .sty or .cls Files

Style and class files are provided by the conference. Modifying them can lead to format violations and desk rejection. If you need custom commands, define them in the preamble of your `.tex` file, not in the style files.

```latex
% GOOD: Custom commands in preamble
\newcommand{\method}{\textsc{MyMethod}}

% BAD: Editing the conference style file
% neurips_2024.sty -- DO NOT EDIT
```

### Do Not Add Random Packages

Adding packages that conflict with the template's style file causes subtle formatting errors. Common conflicts:
- `geometry` package overriding template margins.
- `hyperref` loading order conflicts (must be loaded last in most templates).
- `titlesec` conflicting with template section formatting.
- `setspace` overriding template line spacing.

Only add packages that are genuinely needed and test compilation after each addition.

### Do Not Delete Example Content Too Early

Keep the template's example content (commented out) until you have replaced each section with your own content. The examples show proper usage of custom environments, figure placement, and citation style.

## Compilation Pipeline

### Standard Pipeline

The standard LaTeX compilation requires multiple passes to resolve references and citations.

```bash
pdflatex main.tex      # First pass: generates .aux file with citation/reference keys
bibtex main            # Processes .bib file, generates .bbl
pdflatex main.tex      # Second pass: incorporates bibliography
pdflatex main.tex      # Third pass: resolves all cross-references
```

### Using latexmk

`latexmk` automates the multi-pass compilation and determines the correct number of passes automatically.

```bash
latexmk -pdf main.tex          # Standard compilation
latexmk -pdf -interaction=nonstopmode main.tex  # Non-interactive (for scripts)
latexmk -C                      # Clean all generated files
```

### XeLaTeX Pipeline (for Unicode/CJK support)

When the paper requires Unicode characters or CJK fonts:

```bash
xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex
# or
latexmk -xelatex main.tex
```

### LuaLaTeX Pipeline

Some modern templates require LuaLaTeX:

```bash
lualatex main.tex && bibtex main && lualatex main.tex && lualatex main.tex
# or
latexmk -lualatex main.tex
```

## Log Parsing

After compilation, parse the `.log` file systematically for issues at each severity level.

### Errors (Must Fix)

Errors prevent successful compilation. Common errors and their fixes:

| Error Message | Likely Cause | Fix |
|--------------|-------------|-----|
| `! Undefined control sequence` | Misspelled command or missing package | Check spelling; add required `\usepackage` |
| `! Missing $ inserted` | Math symbol used outside math mode | Wrap in `$...$` or `\(...\)` |
| `! File not found` | Wrong figure path or missing file | Verify path; check filename case sensitivity |
| `! LaTeX Error: Environment X undefined` | Missing package that defines the environment | Add the required package |
| `! Too many }'s` | Unbalanced braces | Count opening and closing braces; use editor matching |

### Warnings (Should Fix)

Warnings indicate potential problems that do not prevent compilation but affect output quality.

| Warning | Meaning | Fix |
|---------|---------|-----|
| `Citation 'X' undefined` | `\cite{X}` has no matching `.bib` entry | Add entry to `.bib` or fix cite key spelling |
| `Reference 'X' undefined` | `\ref{X}` has no matching `\label{X}` | Add the `\label` or fix the key |
| `Label 'X' multiply defined` | Two `\label{}` with the same key | Rename one of the duplicate labels |
| `Overfull \hbox` | Line too wide for the column | Reword, add `\allowbreak`, or adjust table/equation |
| `Underfull \hbox (badness XXXXX)` | Paragraph too sparse | Usually ignorable unless badness > 5000 |
| `Float too large for page` | Figure/table exceeds page height | Reduce size or use `[p]` float placement |

### Undefined References

After the final compilation pass, search the log for any remaining undefined references:

```bash
grep -c "undefined" main.log
grep "Citation.*undefined" main.log
grep "Reference.*undefined" main.log
```

All undefined references must be resolved before proceeding to review (M09).

### Overfull Hbox

Overfull hbox warnings indicate text extending beyond the margin. For camera-ready submissions, these should be eliminated. Strategies:

1. Reword the sentence to be shorter.
2. Use `\allowbreak` in long URLs or technical terms.
3. For tables: reduce font size with `\small` or `\footnotesize`, or restructure the table.
4. For equations: break long equations across lines using `align` or `multline`.
5. Use `\sloppy` as a last resort for a specific paragraph (not globally).

## Comprehensive Checklist Reference

Load `references/latex-checklist.md` for the full 80+ item checklist. That file organizes checks by category: Compilation, References, Typography, Figures, Tables, Equations, and Content Quality.

## Quick Checklist Summary

For rapid verification, check these high-priority items that cover the most common issues.

### Compilation

- [ ] Compiles without errors using full pipeline (pdflatex/bibtex/pdflatex/pdflatex).
- [ ] No undefined `\ref` or `\cite` warnings in log.
- [ ] No multiply-defined labels.
- [ ] All figure files exist at their referenced paths.
- [ ] Bibliography compiles: all cite keys match `.bib` entries.

### References and Cross-References

- [ ] Every `\label{}` has at least one corresponding `\ref{}` or `\eqref{}`.
- [ ] Non-breaking space (`~`) before `\cite{}` and `\ref{}`.
- [ ] Consistent figure reference style: "Fig." mid-sentence, "Figure" at sentence start.
- [ ] Equation references use `\eqref` consistently.
- [ ] No orphan labels (defined but never referenced) or orphan citations (in `.bib` but never cited).

### Typography

- [ ] Em-dash (`---`) for parenthetical asides, en-dash (`--`) for ranges, hyphen (`-`) for compound words.
- [ ] All variables in math mode, even inline: $K$, $N$, not K or N.
- [ ] Vectors in bold (`\bm{q}` or `\boldsymbol{q}`) consistently.
- [ ] Abbreviations defined on first use.

### Figures

- [ ] Vector format (PDF) or high-resolution raster (300+ DPI, preferably 450 DPI).
- [ ] Figure text readable at print size (minimum ~8pt).
- [ ] Consistent style across all figures.
- [ ] Self-contained captions.

### Tables

- [ ] Uses `booktabs` rules (`\toprule`, `\midrule`, `\bottomrule`). No vertical lines.
- [ ] Best results in `\textbf{}`. Second-best underlined where applicable.
- [ ] Units in column headers, not repeated in cells.
- [ ] Table captions above the table.

### Equations

- [ ] Important equations numbered.
- [ ] Punctuation after displayed equations (comma if sentence continues, period if it ends).
- [ ] Consistent notation for common operations (transpose, norm, etc.).

### Content Quality

- [ ] Abstract is self-contained (no citations, no undefined abbreviations).
- [ ] Abstract includes quantitative results.
- [ ] No single-subsection sections.
- [ ] All TODO/FIXME comments removed from source.
- [ ] No commented-out text or debug content.
- [ ] Page count within venue limits.

## Conference Format Conversion Workflow

When converting a paper from one conference format to another (e.g., NeurIPS submission rejected, resubmitting to ICML), follow this procedure. The critical rule is: **never copy preambles between templates.**

### Step 1: Start Fresh with the Target Template

Download the complete target conference template. Compile it as-is to verify it works.

### Step 2: Copy Only Content

From your existing paper, copy only the content (text between `\begin{document}` and `\end{document}`), not the preamble. Specifically copy:
- Section text (between `\section{}` and the next `\section{}`).
- Figure environments (`\begin{figure}...\end{figure}`).
- Table environments.
- Equation environments.
- Bibliography entries (the `.bib` file can be reused directly).

Do NOT copy:
- `\usepackage` declarations (use the target template's packages).
- Custom command definitions (redefine them in the target template's preamble if needed).
- Page layout commands (`\geometry`, `\setlength`, margin settings).
- Header/footer definitions.

### Step 3: Adjust for Target Venue Requirements

- Update page limits (e.g., NeurIPS 9+1 pages vs. ICML 8+unlimited appendix).
- Add or remove required sections (broader impact, ethics statement, limitations).
- Adjust bibliography style to match the target venue.
- Update any venue-specific formatting (e.g., line numbering for review, anonymization).

### Step 4: Compile and Verify

Compile the converted paper and carefully check:
- Margins and page layout match the target template.
- Fonts and sizes are correct.
- Section numbering and formatting follow the target style.
- No formatting artifacts from the source template remain.

## Chinese LaTeX Support

For papers written in Chinese or containing Chinese text.

### ctex Package

The `ctex` package provides comprehensive Chinese typesetting support:

```latex
\usepackage[UTF8]{ctex}  % Basic Chinese support

% Or use a ctex document class directly:
\documentclass{ctexart}   % For articles
\documentclass{ctexrep}   % For reports
\documentclass{ctexbook}  % For books
```

### CJK Font Configuration

```latex
% Using ctex with font presets
\usepackage[UTF8, fontset=adobe]{ctex}    % Adobe fonts
\usepackage[UTF8, fontset=fandol]{ctex}   % Fandol fonts (open source, good default)
\usepackage[UTF8, fontset=windows]{ctex}  % Windows system fonts
\usepackage[UTF8, fontset=mac]{ctex}      % macOS system fonts

% Manual font configuration (XeLaTeX/LuaLaTeX)
\setCJKmainfont{SimSun}           % Main Chinese font (Song)
\setCJKsansfont{SimHei}           % Sans-serif Chinese (Hei)
\setCJKmonofont{FangSong}         % Monospace Chinese (FangSong)
```

### GB/T 7714 Bibliography Style

For Chinese academic papers following the national standard:

```latex
% Using gbt7714 package
\usepackage{gbt7714}
\bibliographystyle{gbt7714-numerical}  % Numbered style [1]
% or
\bibliographystyle{gbt7714-author-year}  % Author-year style (Author, 2024)

% Alternative: using natbib with the custom .bst
\usepackage[numbers,sort&compress]{natbib}
\bibliographystyle{gbt7714-numerical}
```

### Compilation for Chinese Documents

Chinese LaTeX documents typically require XeLaTeX or LuaLaTeX for proper Unicode and font handling:

```bash
xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex
```

pdfLaTeX with `ctex` and `UTF8` option works but has limited font selection and may produce suboptimal output.

## Post-Compilation Verification

After a clean compilation, perform these final checks:

1. **Visual inspection**: Open the PDF and visually verify page layout, margins, fonts, and figure placement.
2. **Page count**: Confirm the paper is within the venue's page limits.
3. **Hyperlinks**: If `hyperref` is used, verify all internal links (citations, references, TOC) work correctly in the PDF.
4. **PDF metadata**: For anonymous submissions, ensure the PDF metadata does not contain author names. Check with:
   ```bash
   pdfinfo main.pdf  # Check Author, Creator, Producer fields
   ```
5. **File size**: Ensure the PDF is within any file size limits imposed by the submission system. Large figures may need compression.
