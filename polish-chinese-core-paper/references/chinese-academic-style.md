# Chinese Academic Style

Use this guide to improve precision, coherence, and readability without applying a uniform voice. Diagnose expressions in context; do not treat any word as proof of AI authorship.

## Contents

1. Editing priorities
2. Section-level guidance
3. Paragraph construction
4. Sentence construction
5. Mechanical and AI-flavored patterns
6. Terminology and mechanics
7. Revision examples

## Editing Priorities

Apply changes in this order:

1. Preserve factual meaning and claim strength.
2. Make the research question, reasoning, and evidence traceable.
3. Give each paragraph a clear rhetorical job.
4. Make subjects, references, conditions, and logical relations explicit.
5. Remove redundancy and awkwardness.
6. Refine rhythm and stylistic variety.

Do not trade a precise technical expression for a shorter but broader synonym. Do not manufacture variety by rotating terms that should remain consistent.

## Section-Level Guidance

### Title

- Identify the research object, problem, method, or scope that distinguishes the paper.
- Remove evaluative adjectives that the manuscript does not establish.
- Avoid stacked generic nouns such as “分析、研究与应用” unless each denotes real content.
- Follow target-journal rules for title length, subtitles, abbreviations, and English translation.

### Abstract

- Derive the final abstract from the polished body.
- Present purpose, method, principal evidence, and conclusion when the article type and journal call for them.
- Keep conditions and comparison scope attached to reported results.
- Avoid background that does not help interpret the research problem.
- Preserve numbers exactly and do not add a “representative” result from memory.
- Follow verified rules for length, person, abbreviations, citations, and structured headings.

### Introduction and Related Work

- Move from the concrete problem to the unresolved gap, not from broad slogans to a predetermined solution.
- Synthesize literature by question, method, evidence, or disagreement rather than listing authors chronologically.
- Distinguish what prior work did from the manuscript author's evaluation of it.
- Make the proposed contribution answer the stated gap.

### Methods, Results, and Discussion

- Keep procedures chronological when execution order matters and causal only when causation is established.
- Describe results before interpretation when the distinction prevents overclaiming.
- Attach comparisons to baselines and conditions.
- Use discussion to explain implications, contradictions, boundaries, and relation to prior work; do not repeat the results section sentence by sentence.

### Conclusion

- Answer the research question at the level supported by the evidence.
- Retain limitations that constrain interpretation.
- Avoid copying the abstract or listing generic future directions.

## Paragraph Construction

- Assign each paragraph one primary job: define, motivate, compare, explain, report, interpret, qualify, or conclude.
- Put known context before new information when doing so improves continuity.
- Keep the grammatical subject stable until the focus genuinely changes.
- Replace generic transitions with the actual relation between adjacent propositions.
- Split a paragraph when it changes object, evidence base, time stage, or argumentative role.
- Merge short paragraphs when they separate a claim from its evidence or qualification.
- Preserve deliberate enumeration when the items are truly parallel; prose is not automatically better than a list.

Test paragraph flow by asking:

1. What does this paragraph contribute?
2. What sentence carries its main claim?
3. What evidence or reasoning supports that claim?
4. Why does it follow the previous paragraph?
5. What information prepares the next paragraph?

## Sentence Construction

### Make the Actor and Object Clear

Repair sentences in which “通过”“基于”“针对” introduces a long phrase but leaves the main actor ambiguous. Prefer a concrete research object, method, experiment, or result as the subject.

### Control Modifier Depth

Break nested `的` phrases when the reader must hold several conditions before reaching the head noun. Move secondary conditions into a preceding sentence or a parenthetical definition only when meaning remains exact.

### Prefer Informative Verbs

Replace empty frames such as “进行……方面的研究”“开展……相关工作” with the actual operation: construct, compare, estimate, optimize, measure, verify, or analyze. Keep domain-standard nominalizations when they name recognized concepts.

### Preserve Logical Relations

Use conjunctions only when the relation is real:

- cause: 由于、因而、由此；
- condition: 当、在……条件下、仅当；
- contrast: 尽管、相比之下、而；
- progression: 在此基础上、进一步；
- example or specification: 例如、具体而言；
- qualification: 但该结论仅适用于、这一解释仍受限于。

Do not alternate connectors mechanically. Recast the sentence if no connector is needed.

### Retain Necessary Caution

Keep language such as “可能”“提示”“在所测试场景中”“对所比较方法而言” when it encodes uncertainty or scope. Concision does not justify removing epistemic boundaries.

## Mechanical and AI-Flavored Patterns

Treat these as review signals, not automatic errors:

- repeated paragraph openings such as “首先、其次、最后” when no real ordered sequence exists;
- empty emphasis such as “值得注意的是”“需要指出的是”“不容忽视的是”;
- repetitive frames such as “本文提出……本文设计……本文验证……”;
- paragraph-label prose in which each sentence announces a category but does not build an argument;
- conclusions that repeat the abstract and append a generic future-work list;
- superlatives such as “首次”“领先”“最优”“填补空白” without bounded comparison or verification;
- highly regular sentence length and syntax that obscures the actual information hierarchy;
- translationese such as unnecessary passive constructions, abstract noun stacking, or literal English ordering.

Delete an expression only when deletion preserves the relation and emphasis. Replace it with evidence or a more exact relation when importance must remain visible. Keep “首先” for a real first procedural step and “此外” when it is the clearest non-mechanical addition.

## Terminology and Mechanics

- Build a terminology table for long manuscripts: preferred Chinese term, English term, abbreviation, symbol, first definition, and prohibited variants.
- Preserve named entities, standards, software, hardware, datasets, and methods exactly.
- Follow the target journal rather than a remembered universal rule for punctuation, spaces, units, headings, references, and bilingual typography.
- Keep figure, table, equation, and section names consistent with their labels and captions.
- Check that pronouns such as “其”“该方法”“上述结果” have one unambiguous antecedent.

## Revision Examples

### Empty Emphasis

Before: `值得注意的是，模型在数据集 A 上取得了较好的效果。`

After, when evidence exists: `模型在数据集 A 上的 F1 值为 91.2%，比基线高 2.4 个百分点。`

Do not invent the numbers shown in the example; use only manuscript evidence.

### Ambiguous Actor

Before: `通过对样本进行归一化处理，提高了模型的稳定性。`

After: `样本归一化后，模型在五次重复实验中的性能波动减小。`

Retain “提高稳定性” if the manuscript does not provide evidence for the more specific replacement; raise a query instead of inventing a measure.

### Unsupported Causation

Before: `该机制导致了识别精度的提升。`

After when only an ablation association exists: `消融结果显示，引入该机制后识别精度提高。`

### Scoped Comparison

Before: `本方法取得了最优性能。`

After: `在数据集 A 的准确率指标上，本方法优于表 3 所列的五种基线。`

### Mechanical Enumeration

Before: `首先构建特征。其次训练分类器。最后完成测试。`

After: `提取的特征用于训练分类器，训练完成后在独立测试集上评估其性能。`

Keep the original enumeration when the text is a procedural checklist and the order itself is the point.
