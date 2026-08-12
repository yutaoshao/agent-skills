# Word Equation Editing and Typesetting

Use this protocol whenever a Chinese academic manuscript in `.docx` contains equations, mathematical symbols, equation numbers, or equation cross-references. It governs editorial decisions, Word object integrity, layout, and verification. It is not a universal style for all Chinese core journals.

## Contents

1. Rule precedence
2. Equation-level editorial audit
3. Pre-edit inventory
4. Mathematical integrity
5. Word object handling
6. Inline and displayed equations
7. Numbering and cross-references
8. Typography, punctuation, and definitions
9. Long equations and paragraph layout
10. Creating or repairing equations
11. Structural and visual verification
12. Delivery record

## Rule Precedence

Apply requirements in this order:

1. the current official target-journal template and author instructions;
2. explicit user instructions for the manuscript;
3. the manuscript's internally consistent, dominant convention;
4. the fallback guidance in this file.

Treat formats observed in published papers as `observed`, not `hard`, unless the journal states the rule officially. Do not infer a common equation format from a journal's 北大核心, CSCD, CSSCI, or other index status.

## Equation-Level Editorial Audit

An equation is a proposition-bearing technical unit, not an automatically protected ornament. In `standard` and `deep`, audit every displayed equation and each material inline formula:

| Gate | Required question |
|---|---|
| Function | Does it define, model, constrain, derive, transform, estimate, or support a claim? |
| Necessity | What technical fact or reasoning step would disappear if it were removed? |
| Placement | Is the formula introduced before use and located near the prose that motivates or interprets it? |
| Granularity | Should this be inline, displayed, split into a derivation, or expressed in prose? |
| Use | Is the result, definition, or relation used later, or is it an unexplained dead end? |
| Evidence | Are assumptions, sources, derivation status, and applicability stated at the strength the manuscript supports? |

Do not retain an equation merely because it is mathematically valid. A repeated definition, unused intermediate step, or decorative restatement may be unnecessary. Conversely, never delete or compress a formula when that would remove a reproducibility-critical definition, condition, or derivation step.

Assign `keep`, `rewrite`, `merge`, `move`, `delete`, or `query` as with prose, but treat a change to mathematical content, a formula deletion, or a formula relocation that changes argumentative emphasis as high risk. Propose it and obtain author confirmation unless the supplied evidence makes the correction and its consequences unambiguous.

## Pre-Edit Inventory

Before modifying a DOCX, record for each equation-bearing paragraph:

- part and paragraph location;
- inline or displayed role;
- object representation: native OMML, embedded OLE/MathType candidate, drawing or image candidate, or plain-text notation;
- exact formula order and a structural or semantic signature when tooling permits;
- visible equation number, numbering field, bookmark, and incoming references;
- surrounding definition, assumptions, punctuation, and `式中` explanation;
- paragraph style, indentation, tab stops, spacing, line spacing, and pagination controls.

Run `scripts/audit_word_equations.py` before editing when the input is `.docx`. The script is an inventory aid, not proof that the mathematics or visual layout is correct.

The script reports all scanned `SEQ` and `REF` instructions because field names alone do not reliably distinguish equations from figures or tables. Interpret field targets in context rather than treating the aggregate count as equation-only.

Mixed representations are a risk signal, not permission to normalize them. If a document contains OMML, OLE, and image equations, preserve each object until the user supplies editable source or authorizes a controlled conversion.

## Mathematical Integrity

Freeze these semantic anchors unless the manuscript or an authoritative supplied source proves a correction:

- operators, relation direction, delimiters, and term order;
- signs, coefficients, constants, exponents, roots, limits, and bounds;
- subscript and superscript attachment, including prescripts;
- vectors, matrices, tensors, sets, domains, indices, and dimensions;
- cases, constraints, boundary or initial conditions, and quantifiers;
- equation labels and the prose claims that cite them.

Preserve more than visible characters. `x_i^2`, `x_i2`, and `x^2_i` can contain similar glyphs while representing different structures. A before-and-after text extraction alone is therefore insufficient; compare native math structure or signatures as well.

Do not silently "correct" a suspicious equation from disciplinary intuition. Keep the source object and raise an author query that identifies the exact symbol, operation, or condition at issue.

## Word Object Handling

### Native OMML

Prefer preserving native Office Math Markup Language (`m:oMath` or `m:oMathPara`) because it remains editable in Word. When polishing surrounding prose:

- edit text runs or OOXML nodes narrowly;
- retain the complete OMML subtree and its order;
- retain bookmarks, field boundaries, tabs, and paragraph properties;
- compare the equation inventory before and after the edit.

Do not assign to `paragraph.text`, rebuild an equation-bearing paragraph from plain text, or round-trip an existing DOCX through Markdown, HTML, or whole-document Pandoc conversion. Those operations can discard math objects, fields, bookmarks, comments, and revision metadata.

### Embedded OLE or MathType Candidates

Treat `w:object`, `o:OLEObject`, and files under `word/embeddings/` as opaque editable-object candidates. Do not mutate or replace them unless the selected tool explicitly preserves the object, relationship, binary part, and visible preview. If the object must be edited and no compatible editor is available, preserve it and request editable source or author action.

An OLE equation can contain a WMF, EMF, or other preview image while still being an embedded editable object. Do not classify it as a raster-only equation solely because a preview relationship or VML picture is present.

### Drawing or Image Candidates

Do not silently accept a rasterized equation as equivalent to editable math. Preserve an existing image when no source is available, flag its editability and resolution, and request the source before content changes. Never convert native OMML or OLE equations to images merely to stabilize appearance.

## Inline and Displayed Equations

Use inline notation for short expressions that function grammatically within a sentence and do not disrupt line height or readability. Use a displayed equation when the expression is referenced, structurally complex, central to the reasoning, or clearer on its own line.

For displayed equations, follow the official template. When no verified rule exists and the manuscript has no stable convention:

- center the equation in the text area and right-align its number;
- use real center and right tab stops or a verified equation style, never repeated spaces;
- avoid layout tables unless the official template already uses or requires them;
- remove first-line indentation from the equation paragraph;
- keep the equation together on one page when possible without forcing unrelated following prose to remain with it.

Do not classify every short expression as a displayed equation, and do not number every displayed equation. Number equations that are important to the argument or referenced later, subject to the target journal's convention.

## Numbering and Cross-References

Record the journal's numbering system explicitly: continuous, section-based, chapter-based, or unnumbered; ASCII or full-width parentheses; and any spacing or punctuation rule. Preserve the manuscript's internally consistent system when the journal rule is unknown.

For generated or repaired documents, prefer real Word fields when the workflow supports them:

- use `SEQ` for equation numbering;
- wrap the target number or equation in a stable bookmark;
- use `REF` for cross-references;
- preserve field instructions and cached visible results;
- update all fields in desktop Word before final delivery when possible.

Headless rendering may show stale or blank cached field results. A rendered number is not proof that the underlying `SEQ`, bookmark, and `REF` chain is valid. Conversely, do not replace a valid field with static text merely because a headless renderer cannot update it.

Static numbers are acceptable only when the source already uses them or the document is intentionally frozen, the equation order will not change, and every reference has been audited. Never renumber by search-and-replace without checking bookmarks, fields, visible references, and references in captions or notes.

## Typography, Punctuation, and Definitions

The official template controls equation font, size, and notation. Do not apply the surrounding Chinese body font indiscriminately to OMML or embedded equations.

When the journal provides no contrary rule and the notation is unambiguous:

- keep variables conventionally italic;
- keep numerals, standard mathematical functions, operators, and units upright;
- distinguish scalars, vectors, matrices, sets, and tensors consistently;
- use one symbol for one meaning and do not reuse it silently;
- define nonstandard symbols at first material use and state units or dimensions where needed.

Treat an equation as part of its sentence. Supply the comma, semicolon, or full stop required by the surrounding syntax, following the target journal's practice. Keep prose punctuation outside the mathematical subtree when it is not mathematically meaningful.

Check that `式中` or equivalent explanations define only symbols that need definition, follow formula order when practical, and do not repeat universally understood operators. Do not invent definitions that are absent or ambiguous; raise an author query.

## Long Equations and Paragraph Layout

For fractions, matrices, integrals, summations, limits, and stacked scripts:

- avoid fixed line spacing that clips the top or bottom of the equation;
- use the template's equation style or sufficient automatic/minimum line height;
- verify the line box above and below the formula after rendering;
- do not shrink a complex equation until it becomes illegible merely to keep one line.

Break a long equation only at logical operators or relation points. Use native OMML aligned structures where available; keep operator alignment and continuation indentation consistent. Do not simulate alignment with spaces or manual line breaks inside plain text. A multi-line derivation normally carries one number unless the journal or mathematical logic requires separately referenced steps.

Test every displayed equation at the actual single- or double-column width. Check that the number remains at the right edge without colliding with the equation, and that a wrapped or split equation does not strand its explanation or punctuation on another page.

## Creating or Repairing Equations

Create or reconstruct a formula only from retained, inspectable source such as author-supplied LaTeX, MathML, or a verified original equation. Use a proven converter or Word math API rather than hand-building complex OOXML when possible.

For conversion to OMML:

1. retain the source expression in task-local working files;
2. require exactly the expected number of native math objects;
3. surface converter errors and warnings;
4. reject visible raw TeX commands or delimiters in the generated equation;
5. verify prescripts, scripts, fractions, radicals, matrices, cases, large operators, and delimiters structurally and visually;
6. keep the equation number outside the mathematical subtree;
7. compare the result with the source expression and rendered page.

Do not use a successful conversion exit code as the sole acceptance criterion. If representation or meaning cannot be verified, preserve the original and report the limitation.

## Structural and Visual Verification

Verification has two independent gates.

### Structural gate

- compare native OMML count, order, and semantic signatures before and after;
- compare embedded-object count and `word/embeddings/` hashes;
- confirm that no equation became drawing-only or plain text unintentionally;
- check visible numbers for duplication and, when applicable, sequence;
- check `SEQ` and `REF` instructions, bookmarks, and dangling references;
- search native math text for leaked TeX commands or delimiters;
- confirm that intentionally changed formulas are listed and author-approved.

### Visual gate

Render the final DOCX to page images or PDF, then inspect every page containing a formula at 100% scale. At final delivery, inspect all pages because equation edits can repaginate later content. Check:

- glyphs, operators, delimiters, accents, scripts, matrices, and fractions;
- inline baseline and surrounding line height;
- display centering, number right alignment, and number collisions;
- line wrapping, column overflow, clipping, and page breaks;
- punctuation and proximity of definitions or explanations;
- cross-reference display after fields are updated.

Structural checks cannot detect clipping; visual checks cannot prove editability or field integrity. Both must pass. When desktop Word is available, open the final file, update all fields, save, and repeat the final render. Report when that Word-specific step was unavailable.

Treat headless LibreOffice or another non-Word renderer as a screening tool. If fonts are missing, fields are stale, pagination differs, or OMML/OLE rendering changes, the visual gate remains unverified until the file is checked in the application required by the journal, normally desktop Word or a specified WPS workflow. Do not rewrite a structurally valid equation merely to compensate for a defect seen only in an alternate renderer.

Before declaring rendering unavailable, check the current environment's documented bundled runtime or workspace dependencies as well as the system path. Do not install or substitute a renderer silently; record the application and version used for the visual check.

## Delivery Record

For a formula-bearing DOCX, add an equation audit to the delivery report:

```markdown
## Word 公式核对

- 原生 OMML / 嵌入对象 / 图片候选：
- 编号、书签与交叉引用：
- 有意修改的公式及依据：
- 结构比较结果：
- 逐页渲染结果：
- Word 字段更新：已执行 / 未执行（原因）
- 待作者确认：
```

Describe only the checks actually performed. `No structural differences detected` does not mean the mathematics is correct, and `rendered without visible defects` does not mean the equations remain editable.
