# Module 07: Polish

De-AI text polishing and language refinement. This module transforms AI-assisted drafts into natural academic prose by detecting and replacing mechanical writing patterns, then verifying overall quality through a three-round review process.

## Overview

Before executing this module, load `references/de-ai-patterns.md` for the detailed pattern catalog with detection heuristics and replacement strategies. That file contains 50+ specific patterns organized by category with before/after examples.

This module provides the procedural framework for applying those patterns systematically across the paper.

## Processing Order

Process sections in order of typical AI pattern density (highest to lowest):

1. **Introduction** -- Highest density of mechanical transitions, filler phrases, and bold-label openers. AI tools tend to produce formulaic introductions with heavy use of "Furthermore," "Moreover," and "Notably."
2. **Discussion** -- Frequently structured as a list of observations rather than connected argumentation. AI-generated discussions often begin every paragraph with "The results show that..."
3. **Conclusion** -- Often a mechanical restatement of the abstract. AI conclusions frequently begin with "In this paper, we proposed..." and end with a numbered list of future work items.
4. **Related Work** -- Tends toward citation dumping and mechanical summaries ("X proposed Y. Z extended this by...").
5. **Methods** -- Generally lower AI pattern density because technical content constrains the writing. Still check for overused vocabulary and mechanical transitions between subsections.
6. **Experiments** -- Lowest priority. Focus on removing filler phrases and ensuring claims match the actual results.
7. **Abstract** -- Process last because it should reflect the polished paper, not the draft.

## English De-AI: 8 Categories

The following categories summarize the patterns detailed in `references/de-ai-patterns.md`. For each category, the reference file provides detection heuristics, specific examples, and replacement strategies.

### Category 1: Bold-Label Paragraph Openers

**What to detect**: Paragraphs beginning with `\textbf{Term.}` or `\textbf{Term:}` that create an implicit bulleted list.

**Why it matters**: This pattern makes prose sections read like PowerPoint slides. It signals AI generation because human writers rarely structure flowing text this way.

**Fix**: Remove the bold labels entirely. Merge short paragraphs where logical. Add transitional phrases that reflect the actual relationship between ideas (contrast, causation, elaboration, example).

```latex
% BAD
\textbf{Exploration.} The algorithm explores the search space by...
\textbf{Exploitation.} As the error decreases, the algorithm shifts to...

% GOOD
The algorithm initially prioritizes exploration of the search space by...
As the error decreases, the search transitions toward exploitation, where...
```

### Category 2: Overused Transition Words

**What to detect**: Sentences or paragraphs beginning with high-frequency AI markers.

**High-frequency markers (replace on sight)**:
- "Furthermore," / "Moreover," / "Additionally," -- merge sentences or use logical connectors
- "Notably," / "Importantly," / "Crucially," -- state the point directly without labeling its importance
- "Interestingly," -- explain what makes it interesting within the sentence itself
- "Specifically," -- launch directly into the specifics
- "Consequently," / "Nevertheless," -- use causal or contrastive restructuring

**Medium-frequency markers (vary, do not always replace)**:
- "However," -- acceptable 2-3 times per section; alternate with "Yet," / "By contrast," / "On the other hand,"
- "In contrast," -- acceptable; alternate with "Unlike X, Y" / "Where X does Z, Y instead"
- "Therefore," -- acceptable; alternate with "It follows that" / "This implies" / "Hence,"

### Category 3: Filler Phrases and Hedging

**What to detect**: Phrases that add zero information content. Common examples:
- "It is worth noting that" / "It should be noted that" / "It is important to mention that" -- delete entirely, state the point directly
- "As can be seen from" -- replace with "Figure X shows" or "Table Y confirms"
- "The results clearly demonstrate that" -- remove "clearly" or replace with a direct statement
- "plays a crucial role in" -- replace with "enables" / "determines" / "is essential for"
- "a wide range of" -- replace with "many" / "diverse" / the specific range
- "in a comprehensive manner" -- delete or describe what is actually comprehensive

### Category 4: Overused AI Vocabulary

**What to detect**: Words appearing 3+ times per section that are AI vocabulary favorites. Key offenders:
- leverage/utilize/harness -- replace with "use," "employ," "apply"
- comprehensive/robust/novel -- replace with specific descriptors
- paradigm/seamless/cutting-edge -- replace with "approach," "smooth," "recent"
- delve into/landscape/plethora -- replace with "examine," "field," "many"
- elucidate/pivotal/myriad/foster -- replace with plain equivalents

Do not over-correct: some of these words are legitimate in specific contexts. The goal is natural variation, not total elimination of formal vocabulary.

### Category 5: Mechanical Sentence Structures

**What to detect**: Identical sentence patterns repeated in close proximity.

- **Three-sentence declarative pattern**: "X is A. Y is B. Z is C." -- combine with logical connectors.
- **First/Second/Third enumeration**: Sequential numbering in prose -- integrate into a flowing description.
- **Identical sentence openers**: 3+ consecutive sentences beginning with the same word (especially "The," "This," "We") -- vary the sentence structure.

### Category 6: Summary/Conclusion Patterns

**What to detect**: Formulaic conclusion structures.

- "In this paper, we proposed..." at the start -- begin with the key insight instead.
- "The experimental results demonstrate that..." -- integrate results into the narrative.
- "Future work will focus on: (1)... (2)... (3)..." -- discuss 1-2 most promising directions with reasoning.
- "In summary, the main contributions are: (1)... (2)... (3)..." -- weave contributions into flowing narrative.

### Category 7: Discussion Section Patterns

**What to detect**: Discussion that reads as a disconnected list of observations.

- Every Discussion paragraph should connect to at least one other paragraph (forward or backward reference).
- No paragraph should begin with "The results show that..." without building on the previous paragraph's argument.
- Provide interpretation and reasoning, not restatement of numbers.
- Connect findings to the broader literature.

### Category 8: Superlative and Absolute Claims

**What to detect**: Unhedged absolute claims without statistical backing.

- "significantly outperforms" without a statistical test -- replace with "outperforms" or state the actual improvement.
- "dramatically improves" -- replace with "substantially improves" or use actual numbers.
- "the best performance" -- qualify as "the best performance among the compared methods."
- "perfectly handles" -- replace with "reliably handles" or "handles effectively."

## Chinese De-AI: 4 Categories

When polishing Chinese academic text, apply these additional categories.

### Category 1: Mechanical Transitions

**What to detect**: Rigid sequential connectors that create a formulaic listing feel.

| Mechanical Pattern | Better Alternatives |
|-------------------|-------------------|
| 首先...其次...最后... | Vary with: 一方面...另一方面...; use topical transitions that reflect logical relationships |
| 此外 / 另外 (used repeatedly) | Vary with: 同时; 在此基础上; or restructure to eliminate the need for additive connectors |
| 与此同时 (used as filler) | Use only when true simultaneity is meant; otherwise rephrase |

### Category 2: Emphasis Fillers

**What to detect**: Phrases that label importance without adding substance.

| Filler Pattern | Fix |
|---------------|-----|
| 值得注意的是 | Delete; state the noteworthy point directly |
| 需要指出的是 | Delete; make the point without announcing it |
| 值得一提的是 | Delete; integrate the point into the argument |
| 众所周知 | Delete or provide the actual evidence |

### Category 3: Subjective Phrases

**What to detect**: First-person subjective expressions inappropriate for formal academic Chinese.

| Subjective Pattern | Fix |
|-------------------|-----|
| 我认为 / 我觉得 | Replace with: 本文认为; 研究表明; 分析结果表明 |
| 我们发现 (overused) | Vary with: 实验结果表明; 数据分析显示; 从结果中可以观察到 |

### Category 4: Enumeration in Prose

**What to detect**: Numbered lists embedded in paragraph text where flowing prose would be more appropriate.

```
% BAD
本方法具有三个优势：（1）计算效率高；（2）精度高；（3）泛化性强。

% GOOD
本方法在保持高计算效率的同时实现了较高精度，且在多种测试条件下表现出良好的泛化性能。
```

## Three-Round Quality Check

After applying de-AI pattern fixes, perform three rounds of verification. Each round has a specific focus and must be completed before moving to the next.

### Round 1: Structure

Focus: Paragraph-level organization and logical flow.

- **Paragraph flow**: Read each section continuously. Does each paragraph follow logically from the previous one? Is there a clear reason each paragraph appears where it does?
- **Logical connections**: Are transitions between paragraphs content-based (building on the previous argument) rather than formulaic (just using a transition word)?
- **Section coherence**: Does each section have a clear arc (setup, development, conclusion)? Does the section deliver on what its opening paragraph promises?
- **Paragraph length**: Are paragraphs balanced (4-8 sentences for body sections)? Flag single-sentence paragraphs and overly long paragraphs (10+ sentences).
- **Topic sentences**: Does each paragraph have a clear topic sentence, preferably as the first or second sentence?

### Round 2: Language

Focus: Sentence-level writing quality.

- **Transition variety**: No two consecutive paragraphs should use the same transition pattern. Maximum 2 identical transition words per section.
- **Sentence variety**: Check for monotonous sentence length and structure. Mix short declarative sentences with longer complex ones. Vary sentence openers.
- **Precise vocabulary**: Replace vague terms with specific ones. "good performance" becomes "3.2% accuracy improvement." "many methods" becomes "transformer-based methods" or a specific count.
- **Active voice**: Prefer active constructions. "The model was trained by us" becomes "We trained the model." (Note: passive voice is acceptable in Methods sections by convention at some venues.)
- **Hedging calibration**: Ensure claims are neither too strong (unhedged superlatives) nor too weak (excessive hedging that undermines the contribution).

### Round 3: Formatting

Focus: LaTeX-level correctness preserved through the polishing process.

- **LaTeX commands intact**: Verify that no `\cite{}`, `\ref{}`, `\label{}`, `\eqref{}`, or math mode expressions were accidentally modified during text polishing.
- **Consistent notation**: Same symbol used for the same concept throughout (do not switch between `\mathbf{q}` and `\boldsymbol{q}`).
- **No orphan references**: Every `\ref` has a matching `\label`. Every `\cite` has a matching `.bib` entry.
- **Whitespace**: Non-breaking spaces (`~`) before `\cite` and `\ref`. No double spaces. No trailing whitespace.
- **Punctuation**: Correct use of em-dash (`---`), en-dash (`--`), and hyphen (`-`). Punctuation after displayed equations.

## Quality Criteria (Pass/Fail)

A section passes the polish module when all of the following are true:

- No paragraph begins with a bold label followed by a period (e.g., `\textbf{X.}`).
- No two consecutive paragraphs start with the same transition word.
- Maximum 2 uses of any identical transition word within a single section.
- Discussion section reads as connected argumentation, not a list of observations.
- Conclusion does not mechanically mirror the Introduction structure.
- Every paragraph has a clear reason to follow the previous one.
- No filler phrases remain (from the Category 3 list above).
- All LaTeX commands and cross-references are intact.

## Style Check Script

For automated detection of common patterns, reference `scripts/style_check.sh`. This script scans `.tex` files for:

- High-frequency AI transition words and their counts per section.
- Bold-label paragraph openers (`\textbf{...}` at line start).
- Filler phrases from the Category 3 list.
- Repeated sentence openers (3+ consecutive sentences with same first word).
- Overused AI vocabulary (words exceeding the threshold per section).

Run the script after manual polishing to catch any remaining patterns:

```bash
bash scripts/style_check.sh main.tex
```

The script produces a report listing detected patterns with line numbers and suggested actions. Address all findings before considering the section polished.

## Application Rules

1. Process one section at a time. Never attempt to polish the entire paper in a single pass.
2. After fixing patterns in a section, re-read the section for flow and coherence. Fixing patterns can introduce new awkwardness.
3. Preserve all technical content, equations, citations, and LaTeX commands exactly. When in doubt, leave the technical content unchanged and only modify the surrounding prose.
4. Do not over-correct. Some "AI words" are perfectly valid in specific contexts. The goal is natural variation, not the elimination of all formal vocabulary.
5. Maintain the author's voice and intent. Polishing should make the text sound like a better version of the same author, not like a different writer.
6. When multiple polishing approaches are possible, prefer the one that shortens the text. Academic writing benefits from conciseness.
