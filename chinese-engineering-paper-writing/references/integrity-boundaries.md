# Integrity Boundaries

Use these rules before and after editing an existing manuscript. Apply comparisons to the affected scope; ordinary rewriting does not require an exhaustive sentence ledger. Preserve facts while making the research contribution clear.

## Protected Anchors

Record the anchors that appear in the input before polishing:

| Anchor | Preserve | Check after editing |
|---|---|---|
| Numerical evidence | Values, signs, ranges, units, uncertainty, sample sizes, dates | Every number remains attached to the same object and condition |
| Mathematical semantics | Operators, signs, term order, scripts, limits, conditions, symbols, dimensions | Mathematical structure and symbol meaning remain unchanged unless evidence proves a correction |
| Technical objects | Method names, datasets, metrics, model variants, algorithms, code identifiers | Names, definitions, and references remain consistent |
| Word equation links | OMML or OLE object type, equation order, visible number, `SEQ`/`REF` fields, bookmarks | No object is flattened and every number and reference still resolves |
| Citations | Citation keys, author-year pairs, quotation boundaries, source attribution | No citation is added, removed, moved, or repurposed without explanation |
| Logical scope | Population, dataset, scenario, baseline, assumptions, exceptions | Generality is not broadened by smoother wording |
| Claim strength | Observation, association, explanation, prediction, causation, proof | The revised claim stays at the same or a weaker justified level |
| Research record | Funding, ethics, conflicts, data availability, authorship, affiliations | Formal statements are not stylistically “normalized” into different facts |

Do not correct a suspected anchor from intuition. Keep the source wording and raise an author query unless the manuscript, source data, or a verified reference resolves the discrepancy.

## Preserve Information Without Freezing Prose

Protect different anchors at the appropriate level:

- Preserve atomic anchors such as numbers, signs, units, symbols, names, comparison directions, citation identifiers, and claim strength exactly.
- Preserve proposition-level anchors such as assumptions, limitations, negative results, scope, and conclusions in meaning and adequate visibility across the manuscript.
- Permit rewriting, merging, or relocation when the protected proposition remains traceable, correctly scoped, and proportionately emphasized.
- Do not interpret “preserve” as “retain the original sentence in the original section.” A factually correct sentence may still be redundant, misplaced, or rhetorically disproportionate.
- Do not interpret relocation as permission to hide an unfavorable result or material limitation. Keep it where the intended reader can evaluate its effect on the claim.

For an exhaustive sentence audit, assign identifiers to moved or merged protected propositions and record their revised locations. For ordinary rewriting, a concise record of material changes is sufficient.

## Claim-Strength Ladder

Keep claims on their supported rung:

1. **Description**: “结果显示”“观察到”“在该数据集上达到”
2. **Association**: “与……相关”“随……变化”
3. **Interpretation**: “可能源于”“可由……解释”
4. **Prediction or effect under stated conditions**: “在……条件下提高”“对……具有预测作用”
5. **Causation or proof**: “导致”“决定”“证实了机制”“证明”

Never move upward merely to make a sentence sound decisive. Preserve qualifiers such as “可能”“在一定条件下”“对所比较方法而言”“在本数据集上”. Remove an empty hedge when doing so preserves the supported claim; retain or accurately restate any qualifier that carries real uncertainty or scope.

Treat these edits as high risk:

- changing “相关” to “影响” or “导致”;
- changing “表明” to “证明”;
- changing “在所比较方法中最优” to “达到最优水平”;
- changing “可用于” to “能够解决”;
- deleting a limitation, boundary condition, or negative result, or relocating it so that its effect on interpretation becomes obscure;
- turning a hypothesis or future direction into a completed contribution;
- changing an equation's operator, sign, operand order, subscript or superscript attachment, limit, condition, dimension, or symbol meaning;
- deleting or relocating a formula when the change removes a necessary reasoning step or alters argumentative emphasis;
- converting an editable Word equation into plain text or an image, or detaching its number, bookmark, or cross-reference.

## Numbers and Statistical Language

- Preserve the original digits, decimal precision, sign, unit, and comparison direction.
- Keep absolute change, relative change, percentage, and percentage-point change distinct.
- Verify that table and figure values match every rewritten textual claim.
- Use “显著” as a statistical term only when a stated test supports it. A larger number alone does not establish statistical significance.
- Do not introduce `p` values, confidence intervals, standard deviations, or sample sizes that are absent from the source.
- Report suspicious arithmetic instead of silently recomputing the manuscript.

## Citations and Quotations

- Never construct Chinese or English references from memory.
- Verify a new reference through an authoritative bibliographic source or the publication itself before adding it.
- Verify that the source supports the exact claim, not merely the broad topic.
- Preserve page numbers and quotation marks for direct quotations.
- Mark unresolved gaps in the report as `[待核引]`; do not insert plausible-looking metadata.
- Do not move a citation across sentences when the move changes which proposition it appears to support.
- Do not add citations solely to meet an assumed reference-count target.

## Editing Authority and Unresolved Facts

Use the user's authorized scope. A request to rewrite or deeply edit authorizes restructuring, merging, deleting redundant wording, and moving supported propositions while preserving their meaning and adequate visibility. Do not request separate approval for each routine editorial decision.

When a change would require choosing between conflicting data, assigning a new technical meaning, changing a research conclusion, or supplying an unverified fact, identify the specific ambiguity and provide a provisional replacement or author query. Continue independent edits. Explicit authorization to edit does not supply missing evidence.

Explain material mathematical corrections and the supplied evidence supporting them. If the mathematics or consequences cannot be established, preserve the original and surface the question rather than silently making a correction.

## Post-Edit Comparison

Perform these checks after polishing:

1. Compare all original and revised numerical tokens, including numbers inside captions and notes.
2. Compare citation identifiers and their sentence-level attachment.
3. Compare equation semantics and order, then compare equation, figure, table, and section references.
4. For DOCX, compare native-math signatures, embedded-object hashes, visible numbers, `SEQ`/`REF` fields, and bookmarks; separately inspect rendered formula pages.
5. Trace every protected proposition from its source location to its revised location.
6. Re-read every change containing causal verbs, superlatives, novelty claims, limitations, negative results, or generalizations.
7. Confirm that no paragraph now claims evidence from a different experiment, sample, baseline, or source.
8. Confirm that no necessary proposition became misleadingly prominent or obscure solely because of its new position.
9. List any anchor that could not be checked because the source data or reference was unavailable.

Report completion honestly: “anchors compared with the supplied manuscript” is valid; “facts verified” is not valid unless independent evidence was actually checked.
