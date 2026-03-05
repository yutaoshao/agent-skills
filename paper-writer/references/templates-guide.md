# Templates Guide

Conference and journal LaTeX template download links, compilation guides, and setup best practices. Load this file during M08 (LaTeX Compilation) for template selection and setup.

---

## Conference Template Downloads

| Conference | Year | Official Download URL | Key Files | Notes |
|-----------|------|----------------------|-----------|-------|
| NeurIPS | 2025 | https://neurips.cc/Conferences/2025/PaperInformation/StyleFiles | `neurips_2025.sty`, `neurips_2025.tex` | Uses natbib; 9 pages + unlimited refs |
| ICML | 2026 | https://icml.cc/Conferences/2026/AuthorInstructions | `icml2026.sty`, `example_paper.tex` | 8 pages + unlimited refs; check for updated year |
| ICLR | 2026 | https://github.com/ICLR/Master-Template | `iclr2026_conference.sty`, `iclr2026_conference.tex` | OpenReview submission; 9 pages + unlimited refs |
| ACL | Latest | https://github.com/acl-org/acl-style-files | `acl.sty`, `acl_latex.tex` | Shared style for ACL/EMNLP/NAACL; 8 pages long, 4 pages short |
| AAAI | 2026 | https://aaai.org/authorkit26/ | `aaai26.sty`, `aaai26-template.tex` | 7 pages + 1 page references; uses aaai bibliography style |
| COLM | 2025 | https://github.com/COLM-org/Template | `colm2025_conference.sty` | Based on ICLR template; 9 pages |
| CVPR | 2026 | https://cvpr.thecvf.com/Conferences/2026 | `cvpr.sty`, `cvpr_2026.tex` | 8 pages + unlimited refs; IEEE two-column |
| ECCV | 2026 | https://eccv2026.ecva.net/ | `eccv.cls` | 14 pages including refs; Springer LNCS format |
| AAAI (Spring Symposium) | 2026 | https://aaai.org/authorkit26/ | Same as main AAAI | Shorter page limits may apply |

**Note**: URLs may change year to year. Always verify by searching "[Conference] [Year] author kit" or "[Conference] [Year] style files".

---

## Page Limits Summary

| Venue | Main Paper | References | Appendix | Limitations |
|-------|-----------|------------|----------|-------------|
| NeurIPS | 9 pages | Not counted | Unlimited supp. | In main or appendix |
| ICML | 8 pages | Not counted | Allowed | In broader impact |
| ICLR | 9 pages | Not counted | Unlimited | In paper |
| ACL Long | 8 pages | Not counted | Not counted | Not counted (mandatory) |
| ACL Short | 4 pages | Not counted | Not counted | Not counted (mandatory) |
| AAAI | 7 pages | 1 page for refs | 1 page (paid extra) | Recommended |
| COLM | 9 pages | Not counted | Allowed | In paper |
| CVPR | 8 pages | Not counted | Supp. allowed | Recommended |
| ECCV | 14 pages | Included | Supp. allowed | Recommended |

---

## Compilation Guides

### Method 1: VS Code + LaTeX Workshop (Recommended for Daily Use)

**Setup**:
1. Install TeX Live (full) or MacTeX
2. Install VS Code extension: "LaTeX Workshop" by James Yu
3. Open the project folder in VS Code

**Configuration** (`.vscode/settings.json`):
```json
{
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex -> bibtex -> pdflatex x2",
      "tools": ["pdflatex", "bibtex", "pdflatex", "pdflatex"]
    },
    {
      "name": "latexmk",
      "tools": ["latexmk"]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": ["-synctex=1", "-interaction=nonstopmode", "-file-line-error", "%DOC%"]
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": ["%DOCFILE%"]
    },
    {
      "name": "latexmk",
      "command": "latexmk",
      "args": ["-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-pdf", "%DOC%"]
    }
  ],
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.view.pdf.viewer": "tab"
}
```

### Method 2: Command Line (pdflatex + bibtex)

The standard compilation pipeline:

```bash
# Full compilation (required for first build and after changing citations)
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Quick compilation (after minor text edits, no citation changes)
pdflatex main.tex
```

**Why run pdflatex three times?**
1. First run: Generates `.aux` file with citation/reference keys
2. `bibtex`: Resolves citations, generates `.bbl` file
3. Second run: Incorporates bibliography, updates references
4. Third run: Resolves any remaining cross-references

### Method 3: latexmk (Automated)

`latexmk` automatically determines the correct number of compilation passes:

```bash
# Compile to PDF
latexmk -pdf main.tex

# Continuous mode (recompile on file change)
latexmk -pdf -pvc main.tex

# Clean auxiliary files
latexmk -c main.tex

# Deep clean (remove output too)
latexmk -C main.tex
```

**Recommended `.latexmkrc`**:
```perl
$pdf_mode = 1;           # Use pdflatex
$bibtex_use = 2;         # Run bibtex when needed
$clean_ext = "bbl run.xml"; # Clean additional files
```

### Method 4: Overleaf (Cloud)

1. Create new project on overleaf.com
2. Upload the entire template directory (do not upload individual files)
3. Set the main document in Project Settings
4. Compilation happens automatically on save
5. Use "Recompile" button if the auto-compile seems stale

**Overleaf tips**:
- Use the "Download Source" option for local backup
- Share via link for collaboration (not email-based sharing)
- Enable "Track Changes" for co-author edits
- Use Git integration for version control

---

## Common Compilation Issues and Fixes

### Missing Package

**Error**: `! LaTeX Error: File 'somepackage.sty' not found.`

**Fix**:
```bash
# TeX Live
tlmgr install somepackage

# macOS (MacTeX)
sudo tlmgr install somepackage

# Ubuntu/Debian
sudo apt-get install texlive-full  # Nuclear option: install everything
```

### Undefined Citation

**Error**: `LaTeX Warning: Citation 'smith2024' on page 3 undefined.`

**Fix**:
1. Check that the cite key exists in your `.bib` file (exact spelling, case-sensitive)
2. Run the full pipeline: `pdflatex -> bibtex -> pdflatex -> pdflatex`
3. Check `main.blg` for bibtex errors

### Undefined Reference

**Error**: `LaTeX Warning: Reference 'fig:pipeline' on page 4 undefined.`

**Fix**:
1. Check that `\label{fig:pipeline}` exists somewhere in the source
2. Ensure the label is inside the correct environment (figure, table, equation)
3. Run pdflatex twice to resolve forward references

### Overfull/Underfull Hbox

**Warning**: `Overfull \hbox (5.2pt too wide) in paragraph at lines 142--158`

**Fix**:
- Reword the sentence to allow better line breaking
- Add `\allowbreak` at acceptable break points
- For URLs: use `\url{}` with the `url` package
- For tables: use `\resizebox{\columnwidth}{!}{...}` or switch to `tabularx`
- Last resort: `\sloppy` (but this creates loose spacing)

### Float Placement Issues

**Warning**: `Float too large for page` or figures appearing far from their reference.

**Fix**:
- Use `[t]` or `[htbp]` placement specifiers
- Add `\clearpage` before large sections to flush floats
- Reduce figure size with `\includegraphics[width=\columnwidth]{...}`
- Use the `placeins` package with `\FloatBarrier`

### BibTeX Errors

**Error in `.blg` file**: `I was expecting a '}' or a ','`

**Fix**:
- Check for unescaped special characters in `.bib` entries: `&`, `%`, `#`, `_`
- Ensure all braces are balanced
- Check for missing commas between fields
- Validate with: `biber --validate-datamodel main` (if using biblatex)

### Font Not Found

**Error**: `! Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable`

**Fix**:
```bash
# Install CM fonts
tlmgr install cm-super

# Or install the EC fonts
tlmgr install ec
```

---

## Template Setup Best Practices

### Initial Setup

1. **Copy the full template directory**, not just `main.tex`. Templates often depend on `.sty`, `.bst`, `.cls`, and other support files.
   ```bash
   cp -r neurips2025_template/ my_paper/
   cd my_paper/
   ```

2. **Verify the template compiles as-is** before making any changes:
   ```bash
   pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
   ```
   If the template itself does not compile, the issue is with your TeX installation, not your content.

3. **Replace content section by section**, keeping template comments as reference for formatting requirements.

4. **Clean up template artifacts only at the end** (sample text, example figures, template comments).

### File Organization

Recommended project structure:
```
my_paper/
  |-- main.tex              # Main document
  |-- references.bib        # Bibliography
  |-- neurips_2025.sty      # Style file (DO NOT MODIFY)
  |-- sections/
  |   |-- abstract.tex
  |   |-- introduction.tex
  |   |-- related_work.tex
  |   |-- methods.tex
  |   |-- experiments.tex
  |   |-- discussion.tex
  |   |-- conclusion.tex
  |   |-- appendix.tex
  |-- figures/
  |   |-- figure1.pdf
  |   |-- figure2.pdf
  |-- tables/
  |   |-- results.tex
  |-- .latexmkrc            # latexmk configuration
```

Use `\input{sections/introduction}` in `main.tex` to keep files modular.

### Style File Rules

- **NEVER modify the `.sty` or `.cls` file** provided by the conference. This can cause desk rejection.
- If you need custom commands, define them in the preamble of `main.tex` or in a separate `macros.tex` file.
- If the style file conflicts with a package you need, find a workaround or use the style file's provided alternatives.

---

## Anonymization Checklist for Blind Review

### Before Submission

- [ ] Enable anonymous mode in the style file (e.g., `\usepackage[anonymous]{neurips_2025}`)
- [ ] Remove author names and affiliations from `\author{}`
- [ ] Remove or anonymize acknowledgments
- [ ] Self-cite in third person: "Smith et al. [5] showed..." not "In our prior work [5]..."
- [ ] Anonymize code/data links: use Anonymous GitHub (https://anonymous.4open.science/) or state "will be released upon acceptance"
- [ ] Check PDF metadata:
  ```latex
  \hypersetup{
    pdfauthor={},
    pdftitle={Paper Title},
    pdfkeywords={keyword1, keyword2},
  }
  ```
- [ ] Check that the compiled PDF does not contain author names in headers/footers
- [ ] Remove any grant numbers or funding sources that could identify authors
- [ ] Check figure metadata (some tools embed author info in PDF/PNG files)
  ```bash
  # Check PDF metadata
  pdfinfo main.pdf

  # Check image metadata
  exiftool figure1.png
  ```

### Camera-Ready (After Acceptance)

- [ ] Disable anonymous mode
- [ ] Add full author names, affiliations, and emails
- [ ] Add acknowledgments section
- [ ] Add grant/funding information
- [ ] Remove "Anonymous Submission" from any headers
- [ ] Update code/data links to permanent, non-anonymous URLs
- [ ] Verify page count with camera-ready limits (sometimes different from review)
- [ ] Include any mandatory statements required by the venue (e.g., reproducibility, ethics)
