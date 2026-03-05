# De-AI Writing Patterns Reference

Comprehensive catalog of AI-generated writing patterns commonly found in academic papers. This document merges English patterns (8 categories) and Chinese patterns (4 categories) into a single deep-dive knowledge base for Module M07 (Polish).

---

## Part I: English De-AI Patterns (8 Categories)

### Category 1: Bold-Label Paragraph Openers

**Detection**: Lines matching `\textbf{...}` or `**...**` at paragraph start, followed by a period or colon. This pattern turns prose sections into implicit bullet lists.

**Pattern**:
```latex
% BAD: Mechanical listing style
\textbf{Global exploration.} The algorithm uses ...
\textbf{Local exploitation.} As the error decreases ...
\textbf{Convergence guarantee.} Under mild conditions ...
```

**Fix**: Remove labels entirely. Merge paragraphs where logical, add transitional phrases that reflect actual relationships between ideas.

```latex
% GOOD: Flowing prose with natural transitions
The algorithm initially prioritizes global exploration by ...
As the error decreases, the search transitions to local exploitation, where ...
Under mild conditions, this adaptive behavior provides convergence guarantees because ...
```

**When labels are acceptable**: Method descriptions with clearly distinct components (e.g., "Encoder" / "Decoder" in an architecture). Even then, prefer subsections over bold labels when the descriptions exceed 2 paragraphs each.

### Category 2: Overused Transition Words

**Detection**: Paragraph or sentence starting with any of these words/phrases. Count occurrences per section.

#### High-frequency AI markers (replace on sight)

These transitions are the strongest signals of AI-generated text. Replace every occurrence:

| AI Transition | Replacement Strategies |
|--------------|----------------------|
| "Furthermore," | "Beyond this," / "This extends to" / rephrase to show the logical connection / simply remove |
| "Moreover," | "A related advantage is" / "In addition to X, Y also" / merge the two sentences |
| "Additionally," | Restructure the sentence without a leading adverb / "X also" |
| "Notably," | "Of particular relevance," / "One observation deserving emphasis is" / simply state the notable thing directly |
| "Importantly," | State *why* it is important rather than labeling it as important |
| "Interestingly," | Explain what makes it interesting as part of the sentence |
| "Crucially," | "The critical factor is" / just state the point without the label |
| "Specifically," | Launch directly into the specifics without preamble |
| "Consequently," | "This leads to" / "As a result," / restructure to show causation directly |
| "Nevertheless," | "Despite this," / "Even so," / "Yet" / contrastive restructuring |

#### Medium-frequency markers (vary, do not always replace)

These are legitimate English transitions but become AI signals when overused:

| Transition | Policy | Alternatives |
|-----------|--------|-------------|
| "However," | Max 2-3 per section | "Yet," / "By contrast," / "On the other hand," / "Still," / "That said," |
| "In contrast," | Acceptable, vary | "Unlike X, Y" / "Where X does Z, Y instead" / "Conversely," |
| "Therefore," | Acceptable, vary | "It follows that" / "This implies" / "Hence," / "Thus," |

#### Sentence-initial transition audit

After de-AI processing, perform a scan: no two consecutive paragraphs should begin with the same transition word. If they do, restructure one of them.

### Category 3: Filler Phrases and Hedging

**Detection**: Phrases that add no information content. These pad word count without contributing meaning.

| AI Filler Phrase | Action |
|-----------------|--------|
| "It is worth noting that" | **Delete entirely**; state the point directly |
| "It should be noted that" | **Delete entirely** |
| "It is important to mention that" | **Delete entirely** |
| "It is worth mentioning that" | **Delete entirely** |
| "As can be seen from" | Replace with "Figure X shows" / "Table Y confirms" |
| "It can be observed that" | State the observation directly |
| "The results clearly demonstrate that" | "The results show" or state what they show directly |
| "It is evident that" | **Delete**; state the evident thing |
| "plays a crucial role in" | "is essential for" / "enables" / "determines" |
| "in the context of" | "for" / "in" / "during" |
| "a wide range of" | "many" / "diverse" / give the specific range |
| "state-of-the-art" | "current best" / name the specific methods being compared to |
| "in a comprehensive manner" | **Delete**; describe what is actually comprehensive |
| "In order to" | "To" |
| "Due to the fact that" | "Because" / "Since" |
| "For the purpose of" | "To" / "For" |
| "In light of the fact that" | "Because" / "Given that" |
| "With regard to" | "About" / "Regarding" / "For" |

**Rule of thumb**: If deleting the phrase does not change the sentence's meaning, delete it.

### Category 4: Overused AI Vocabulary

**Detection**: Word frequency analysis. Flag words appearing 3+ times per section, or any occurrence of the highest-signal words.

#### Highest-signal AI words (replace on every occurrence)

| AI Word | Better Alternatives |
|---------|-------------------|
| leverage | use, employ, apply, exploit, adopt |
| utilize | use |
| harness | use, apply, channel |
| delve into | examine, study, analyze, investigate |
| paradigm | approach, framework, method |
| landscape | field, domain, area |
| plethora | many, numerous, a large number of |
| myriad | many, numerous, a variety of |
| synergy | combination, integration, complementarity |
| holistic | complete, integrated, unified |
| elucidate | explain, clarify, show |
| foster | encourage, promote, support |

#### Medium-signal AI words (reduce frequency, do not eliminate)

| AI Word | Better Alternatives |
|---------|-------------------|
| facilitate | enable, allow, support, make possible |
| comprehensive | thorough, extensive, systematic, detailed |
| robust | reliable, resilient, stable, consistent |
| novel | new, proposed, different (or omit -- let novelty speak for itself) |
| seamless | smooth, integrated, unified |
| cutting-edge | recent, advanced, latest |
| underscore | highlight, emphasize, show |
| pivotal | important, critical, key |

#### Context-dependent words

| Word | When OK | When to Replace |
|------|---------|----------------|
| "novel" | Rarely -- only if truly unprecedented | Most uses: omit or use "new" |
| "robust" | When specifically discussing robustness experiments | As a generic positive adjective |
| "significant" | When reporting statistical significance tests | As a generic intensifier |
| "comprehensive" | When describing a truly exhaustive analysis | As padding |

### Category 5: Mechanical Sentence Structures

**Detection**: Identical sentence patterns repeated in close proximity.

#### The "X. Y. Z." Three-Sentence Pattern

AI models frequently produce three consecutive short declarative sentences with parallel structure:

```
% BAD: Three isolated declarative sentences
The method achieves high accuracy. The convergence is fast. The results are promising.
```
```
% GOOD: Varied structure with logical connections
The method achieves high accuracy while converging rapidly, yielding results that ...
```

#### The "First, Second, Third" Enumeration

```
% BAD: Mechanical enumeration in prose sections
First, we design a network. Second, we train it with WTA loss. Third, we refine with PSO.
```
```
% GOOD: Integrated description showing how stages connect
The framework begins with a multi-hypothesis network whose WTA training encourages ...
The resulting predictions then seed an adaptive PSO that ...
```

#### Identical Sentence Openers

**Flag when 3+ consecutive sentences begin with the same word**, especially "The", "This", "We", "Our", or "It".

```
% BAD
The encoder processes the input. The decoder generates the output. The loss function measures the error.
```
```
% GOOD
After the encoder processes the input, the decoder generates corresponding output tokens.
Training minimizes the cross-entropy loss between predicted and reference sequences.
```

#### The "We" Overuse Pattern

In methods sections, every sentence starting with "We" creates a monotonous, report-like tone:

```
% BAD
We design the network. We train it for 100 epochs. We evaluate on three benchmarks. We observe improvements.
```
```
% GOOD
The network architecture follows [design rationale]. Training proceeds for 100 epochs with [optimizer details].
Evaluation on three benchmarks reveals consistent improvements, as detailed in Section 4.
```

### Category 6: Summary/Conclusion Patterns

**Detection**: Formulaic conclusion structures that echo the abstract verbatim.

| AI Pattern | Fix |
|-----------|-----|
| "In this paper, we proposed..." (restating the abstract) | Start with the key insight or the most surprising finding |
| "The experimental results demonstrate that..." | Integrate specific results into the narrative |
| "Future work will focus on..." (listing 3+ items mechanically) | Discuss 1-2 most promising directions with reasoning for why they matter |
| "In summary, the main contributions are: (1)... (2)... (3)..." | Weave contributions into a flowing narrative paragraph |
| "We hope that our work will inspire..." | Delete -- let the work speak for itself |
| "To the best of our knowledge, this is the first..." | Only if verifiably true; otherwise rephrase |

**Good conclusion openers**:
- Start with the core finding, not "In this paper"
- Connect to the broader research direction
- End with the most forward-looking implication

### Category 7: Discussion Section Patterns

**Detection**: Discussion that reads as a list of observations rather than connected argumentation.

**Structural requirements**:
- Each paragraph should connect to at least one other paragraph (forward or backward reference)
- Avoid starting every paragraph with "The results show that..."
- Provide interpretation and reasoning, not just restatement of numbers
- Connect findings to the broader literature

**AI pattern**: "Observation -> Possible explanation -> Future work" repeated N times as a list.

**Better pattern**: Build an argument across paragraphs:
1. Open with the most important finding and its implications
2. Address apparent contradictions or surprising results
3. Connect to related work -- how do your findings extend or challenge existing understanding?
4. Discuss limitations honestly, with analysis of their impact
5. Close with the strongest implication for the field

### Category 8: Superlative and Absolute Claims

**Detection**: Unhedged absolute claims without quantitative evidence.

| BAD | BETTER |
|-----|--------|
| "significantly outperforms" (without statistical test) | "outperforms by X%" / "achieves X% improvement (p < 0.05)" |
| "dramatically improves" | "improves by [specific number]" |
| "the best performance" | "the best performance among the compared methods" |
| "perfectly handles" | "reliably handles" / "handles effectively in X/Y cases" |
| "state-of-the-art results" | "results competitive with or exceeding [specific method]" |
| "groundbreaking" | Describe the actual advance and let the reader judge |
| "unprecedented" | Specify what was not possible before and cite the previous best |
| "orders of magnitude faster" | Specify the actual speedup factor |

**Rule**: Every comparative or superlative claim should be accompanied by a number, a citation, or a statistical test. If you cannot provide one, weaken the claim.

---

## Part II: Chinese De-AI Patterns (4 Categories)

### Category C1: Mechanical Transitions (机械连接词)

#### Banned transition words (正文段落禁用)

| Banned | Replacement Strategy |
|--------|---------------------|
| 首先/其次/最后 | 用逻辑关系词替代：因此/由于/鉴于/基于此 |
| 此外/另外 | 直接陈述新信息，不加引导词 |
| 接下来 | 用具体内容引出下文："在此基础上" / "进一步地" |
| 与此同时 | "同期" / "在同一实验条件下" / 直接并列 |
| 综上所述 | "这些结果表明" / "总体而言" (max 1次/文) |

#### Replacement principles

1. **因果关系用因果词**: "由于X，Y因此呈现..." 而非 "首先X，其次Y"
2. **并列关系用语义衔接**: "除X外，Y同样具有..." 而非 "此外，Y也..."
3. **转折关系用对比结构**: "尽管X表现优异，Y在Z方面仍存在不足" 而非 "然而..."
4. **递进关系用逻辑链**: "在X的基础上，进一步引入Y" 而非 "另外，还使用了Y"

#### Section-specific max counts

| Transition | Max per section |
|-----------|----------------|
| 然而/但是 | 2 |
| 因此/所以 | 2 |
| 同时 | 2 |
| 进一步 | 1 |
| 总之/综上 | 1 per paper |

### Category C2: Emphasis Fillers (强调性填充)

#### Banned phrases (全文禁用)

| Banned Phrase | Action |
|--------------|--------|
| 值得注意的是 | **删除**, 直接陈述 |
| 需要指出的是 | **删除**, 直接陈述 |
| 重要的是 | **删除**, 用数据/逻辑说明为何重要 |
| 必须强调的是 | **删除**, 让事实自己说话 |
| 不容忽视的是 | **删除** |
| 显而易见 | **删除**, 如果真的显而易见则无需强调 |
| 毋庸置疑 | **删除**, 在学术写作中应避免如此绝对的断言 |

#### Replacement strategy

不要"标签化"重要性。用以下方式代替:
- 用具体数据说明: "实验结果显示精度提升了15%"
- 用对比说明: "相比现有方法，本方法在X上表现更优"
- 用逻辑推导说明: "由于X的特性，Y自然成为首选方案"

### Category C3: Subjective Expressions (主观表达)

#### Formal academic text prohibitions (论文正文禁用)

| Banned Expression | Context | Replacement |
|------------------|---------|-------------|
| 我认为 | 论文正文 | "分析表明" / "实验结果支持" / "基于X可以推断" |
| 我觉得 | 论文正文 | 同上 |
| 我个人看法 | 论文正文 | 禁用, 学术论文不使用个人视角 |
| 我的研究 | 论文正文 | "本文" / "本研究" / "所提方法" |
| 我们发现 | 过度使用时 | "实验表明" / "结果显示" / "分析发现" (可交替使用) |

#### "我们" usage policy

"我们" (we) is acceptable in Chinese academic writing but should not start more than 30% of sentences in any section. Vary with:
- 被动句式: "通过X实验验证了..."
- 以方法/结果为主语: "所提方法在X上实现了..."
- 以实验为主语: "实验结果证实了..."

### Category C4: Enumeration in Prose (正文列表化)

#### Rule: Prose first, lists only when necessary

**正文段落优先使用连续叙述**. 列表仅在以下场景允许:

| Allowed for Lists | Must Use Prose |
|-------------------|---------------|
| 实验计划/步骤 | 方法描述 |
| 参数配置表 | 实验结果分析 |
| 对比清单 | 相关工作综述 |
| 贡献要点 (Introduction) | 讨论与结论 |

#### Converting lists to prose

```
% BAD: List in discussion
本文的主要发现包括:
1. 方法A在数据集X上表现最优
2. 参数Y对结果影响显著
3. 模型在Z场景下存在局限

% GOOD: Flowing prose
在所有测试数据集中，方法A在数据集X上表现最优，精度达到92.3%。
参数Y的敏感性分析表明其对最终结果有显著影响: 当Y从0.1增至0.5时，
精度下降了8.7个百分点。尽管如此，模型在Z场景下仍存在一定局限，
主要体现在...
```

---

## Part III: Application Rules

### Processing Order

1. Process one section at a time. Never process the whole paper in a single pass.
2. Within each section, apply categories in order: 1 (bold labels) -> 2 (transitions) -> 3 (fillers) -> 4 (vocabulary) -> 5 (structures) -> 6-8 (section-specific).
3. After fixing all patterns, re-read the section for flow. Mechanical pattern replacement can itself create awkward prose.

### Preservation Rules

- **Never alter**: equations, citations (`\cite{}`), cross-references (`\ref{}`), figure/table data, technical terminology, method names, dataset names, metric names.
- **Preserve meaning**: Every replacement must be semantically equivalent. When uncertain, keep the original.
- **Preserve author voice**: Some authors legitimately use certain "AI words." If the word appears in a context where it is the most precise choice, keep it.

### Quantitative Targets

| Metric | Target |
|--------|--------|
| Max identical transition per section | 2 |
| Max "We" sentence openers per section | 30% of sentences |
| Bold-label paragraphs in prose | 0 (except clearly itemized components) |
| Filler phrases per section | 0 |
| Highest-signal AI vocabulary per paper | 0 |
| Consecutive identical sentence openers | Max 2 |

### Quality Check After De-AI

- [ ] Technical content unchanged
- [ ] All equations, citations, and references intact
- [ ] Flow is natural when read aloud
- [ ] No new grammatical errors introduced
- [ ] Paragraph transitions have clear logical motivation
- [ ] Every paragraph has a clear reason to follow the previous one
- [ ] Section reads like it was written by an experienced researcher, not generated
