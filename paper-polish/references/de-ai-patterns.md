# De-AI Writing Patterns Reference

Comprehensive catalog of AI-generated writing patterns commonly found in academic papers. Organized by category with detection heuristics and replacement strategies.

## Category 1: Bold-Label Paragraph Openers

**Detection**: Lines matching `\textbf{...}` or `**...**` at paragraph start, followed by a period or colon.

**Pattern**: Using bold-face labels to structure prose sections as implicit lists.
```latex
% BAD: Mechanical listing style
\textbf{Global exploration.} The algorithm uses ...
\textbf{Local exploitation.} As the error decreases ...
\textbf{Convergence guarantee.} Under mild conditions ...
```

**Fix**: Remove labels entirely. Merge paragraphs where logical, add transitional phrases that reflect actual relationships.
```latex
% GOOD: Flowing prose with natural transitions
The algorithm initially prioritizes global exploration by ...
As the error decreases, the search transitions to local exploitation, where ...
Under mild conditions, this adaptive behavior provides convergence guarantees because ...
```

## Category 2: Overused Transition Words

**Detection**: Paragraph or sentence starting with any of these words/phrases.

### High-frequency AI markers (replace on sight)
- "Furthermore," --> use: "Beyond this," / "This extends to" / rephrase to show logical connection / simply remove
- "Moreover," --> use: "A related advantage is" / "In addition to X, Y also" / merge sentences
- "Additionally," --> use: sentence restructuring without a leading adverb / "X also"
- "Notably," --> use: "Of particular relevance," / "One observation deserving emphasis is" / simply state the notable thing directly
- "Importantly," --> use: state why it is important rather than labeling it
- "Interestingly," --> use: explain what makes it interesting as part of the sentence
- "Crucially," --> use: "The critical factor is" / just state the point
- "Specifically," --> use: launch directly into the specifics
- "Consequently," --> use: "This leads to" / "As a result," / causal restructuring
- "Nevertheless," --> use: "Despite this," / "Even so," / "Yet" / contrastive restructuring

### Medium-frequency markers (vary, do not always replace)
- "However," -- acceptable in moderation (max 2-3 per section), alternate with "Yet," / "By contrast," / "On the other hand,"
- "In contrast," -- acceptable, alternate with "Unlike X, Y" / "Where X does Z, Y instead"
- "Therefore," -- acceptable, alternate with "It follows that" / "This implies" / "Hence,"

## Category 3: Filler Phrases and Hedging

**Detection**: Phrases that add no information content.

| AI Filler | Replacement |
|-----------|-------------|
| "It is worth noting that" | Delete; state the point directly |
| "It should be noted that" | Delete |
| "It is important to mention that" | Delete |
| "As can be seen from" | "Figure X shows" / "Table Y confirms" |
| "It can be observed that" | State the observation directly |
| "The results clearly demonstrate that" | "The results demonstrate" or just state what they show |
| "It is evident that" | Delete; state the evident thing |
| "plays a crucial role in" | "is essential for" / "enables" / "determines" |
| "in the context of" | "for" / "in" / "during" |
| "a wide range of" | "many" / "diverse" / specific description |
| "state-of-the-art" | "current best" / name the specific methods |
| "in a comprehensive manner" | Delete; describe what is actually comprehensive |

## Category 4: Overused AI Vocabulary

**Detection**: Word frequency analysis. Flag words appearing 3+ times per section.

| AI Word | Better Alternatives |
|---------|--------------------|
| leverage | use, employ, apply, exploit, adopt |
| utilize | use |
| harness | use, apply, channel |
| facilitate | enable, allow, support |
| comprehensive | thorough, extensive, systematic, detailed |
| robust | reliable, resilient, stable, consistent |
| novel | new, proposed, different (or omit -- let novelty speak for itself) |
| paradigm | approach, framework, method |
| seamless | smooth, integrated, unified |
| cutting-edge | recent, advanced |
| delve into | examine, study, analyze, investigate |
| landscape | field, domain, area |
| plethora | many, numerous, a large number of |
| synergy | combination, integration, complementarity |
| holistic | complete, integrated, unified |
| underscore | highlight, emphasize, show |
| elucidate | explain, clarify, show |
| pivotal | important, critical, key |
| myriad | many, numerous |
| foster | encourage, promote, support |

## Category 5: Mechanical Sentence Structures

**Detection**: Identical sentence patterns repeated in close proximity.

### The "X. Y. Z." Three-Sentence Pattern
```
% BAD: Three isolated declarative sentences
The method achieves high accuracy. The convergence is fast. The results are promising.
```
```
% GOOD: Varied structure with logical connections
The method achieves high accuracy while converging rapidly, yielding results that ...
```

### The "First, Second, Third" Enumeration
```
% BAD: Mechanical enumeration in prose sections
First, we design a network. Second, we train it with WTA loss. Third, we refine with PSO.
```
```
% GOOD: Integrated description
The framework begins with a multi-hypothesis network whose WTA training encourages ...
The resulting predictions then seed an adaptive PSO that ...
```

### Identical Sentence Openers
Flag when 3+ consecutive sentences begin with the same word (especially "The", "This", "We").

## Category 6: Summary/Conclusion Patterns

**Detection**: Formulaic conclusion structures.

| AI Pattern | Fix |
|-----------|-----|
| "In this paper, we proposed..." (restating abstract) | Start with the key insight or contribution |
| "The experimental results demonstrate that..." | Integrate results into the narrative flow |
| "Future work will focus on..." (listing 3+ items mechanically) | Discuss 1-2 most promising directions with reasoning |
| "In summary, the main contributions are: (1)... (2)... (3)..." | Weave contributions into a flowing narrative |

## Category 7: Discussion Section Patterns

**Detection**: Discussion that reads as a list of observations rather than connected argumentation.

- Each paragraph in Discussion should connect to at least one other paragraph (forward or backward reference)
- Avoid starting every Discussion paragraph with "The results show that..."
- Provide interpretation and reasoning, not just restatement of numbers
- Connect findings to the broader literature

## Category 8: Superlative and Absolute Claims

**Detection**: Unhedged absolute claims.

| BAD | BETTER |
|-----|--------|
| "significantly outperforms" (without statistical test) | "outperforms" / "achieves X% improvement over" |
| "dramatically improves" | "substantially improves" / use actual numbers |
| "the best performance" | "the best performance among the compared methods" |
| "perfectly handles" | "reliably handles" / "handles effectively" |

## Application Rules

1. Process one section at a time, never the whole paper at once.
2. After fixing patterns, re-read the section aloud (mentally) for flow.
3. Preserve all technical content, equations, citations, and LaTeX commands.
4. Do not over-correct: some "AI words" are perfectly valid in context. The goal is natural variation, not elimination of all formal vocabulary.
5. Maximum 2 of the same transition word per section.
6. Every paragraph should have a clear reason to follow the previous one.
