# Integrity Boundaries

Use these rules before and after every manuscript edit. Treat fluent prose as secondary to factual and argumentative integrity.

## Protected Anchors

Record the anchors that appear in the input before polishing:

| Anchor | Preserve | Check after editing |
|---|---|---|
| Numerical evidence | Values, signs, ranges, units, uncertainty, sample sizes, dates | Every number remains attached to the same object and condition |
| Technical objects | Equations, symbols, method names, datasets, metrics, model variants | Names and definitions remain consistent |
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

Assign a stable identifier to a protected proposition before moving or merging it, then record its revised location in the sentence audit.

## Claim-Strength Ladder

Keep claims on their supported rung:

1. **Description**: “结果显示”“观察到”“在该数据集上达到”
2. **Association**: “与……相关”“随……变化”
3. **Interpretation**: “可能源于”“可由……解释”
4. **Prediction or effect under stated conditions**: “在……条件下提高”“对……具有预测作用”
5. **Causation or proof**: “导致”“决定”“证实了机制”“证明”

Never move upward merely to make a sentence sound decisive. Preserve qualifiers such as “可能”“在一定条件下”“对所比较方法而言”“在本数据集上”. Remove a qualifier only when the evidence and author explicitly support doing so.

Treat these edits as high risk:

- changing “相关” to “影响” or “导致”;
- changing “表明” to “证明”;
- changing “在所比较方法中最优” to “达到最优水平”;
- changing “可用于” to “能够解决”;
- deleting a limitation, boundary condition, or negative result, or relocating it so that its effect on interpretation becomes obscure;
- turning a hypothesis or future direction into a completed contribution.

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

## Author Confirmation Boundaries

Apply local grammar, punctuation, and unambiguous redundancy fixes without confirmation when they preserve meaning. Mark or request confirmation before:

- changing a research question, hypothesis, contribution, limitation, or conclusion;
- merging claims supported by different evidence;
- deleting content that may carry disciplinary or legal significance;
- reordering paragraphs in a way that changes argumentative emphasis;
- moving a protected proposition between high- and low-emphasis locations when the move changes how readers assess the main claim;
- replacing a technical term with a near-synonym;
- changing an ambiguous numerical or citation statement;
- adding any factual content not present in the supplied sources.

In `deep` mode, provide a proposed revision and the reasoning, but keep unresolved substantive changes visibly provisional.

## Post-Edit Comparison

Perform these checks after polishing:

1. Compare all original and revised numerical tokens, including numbers inside captions and notes.
2. Compare citation identifiers and their sentence-level attachment.
3. Compare equation, figure, table, and section references.
4. Trace every protected proposition from its source location to its revised location.
5. Re-read every change containing causal verbs, superlatives, novelty claims, limitations, negative results, or generalizations.
6. Confirm that no paragraph now claims evidence from a different experiment, sample, baseline, or source.
7. Confirm that no necessary proposition became misleadingly prominent or obscure solely because of its new position.
8. List any anchor that could not be checked because the source data or reference was unavailable.

Report completion honestly: “anchors compared with the supplied manuscript” is valid; “facts verified” is not valid unless independent evidence was actually checked.
