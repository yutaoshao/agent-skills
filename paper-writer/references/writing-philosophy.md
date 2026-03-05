# Writing Philosophy

A consolidated guide to academic writing principles for CS/ML/AI papers. Draws from established advice by Neel Nanda, Sam Farquhar, George Gopen, Judith Swan, Luis Perez, Zachary Lipton, Jacob Steinhardt, and others.

---

## The Narrative Principle (Nanda)

Every paper must answer three questions in order:

1. **What?** -- What did you do? (The contribution)
2. **Why?** -- Why does it matter? (The motivation)
3. **So What?** -- What are the implications? (The impact)

### The One-Sentence Contribution

Before writing anything, formulate the paper's contribution as a single sentence:

> "We show that [specific method/finding] achieves [specific result] on [specific problem], which matters because [specific reason]."

If you cannot write this sentence, the paper is not ready to write. Everything in the paper should serve this one sentence.

### Common failure modes

- **No "So What?"**: Paper describes a method and shows numbers but never explains why anyone should care.
- **Buried contribution**: The key insight appears on page 6 instead of page 1.
- **Multiple competing contributions**: Paper tries to claim 5 different things. Focus on 1-2.

---

## Time Allocation

How to allocate effort across paper sections (recommended by multiple senior researchers):

```
Abstract    = 25% of writing effort
Introduction = 25% of writing effort
Figures     = 25% of writing effort
Everything else = 25% of writing effort
```

This seems counterintuitive because the abstract is short, but per-word quality matters enormously for the abstract and introduction. Many reviewers form their opinion in the first page.

---

## Abstract Formula (Farquhar)

The abstract should consist of exactly 5 functional sentences:

| Sentence | Function | Example Start |
|----------|----------|--------------|
| 1 | **Context**: Establish the research area | "Large language models have become..." |
| 2 | **Problem**: State what is missing or broken | "However, existing approaches fail to..." |
| 3 | **Method**: Describe what you did | "We propose X, which..." |
| 4 | **Result**: Give the key quantitative finding | "On benchmarks A and B, X achieves..." |
| 5 | **Implication**: State the broader significance | "These results suggest that..." |

Rules:
- No citations in the abstract
- No undefined abbreviations
- Include at least one specific number
- Keep it under 250 words (150 for letters/short papers)
- Every word must earn its place

---

## Introduction Structure

### Length and Pacing

- 1-1.5 pages for conference papers, up to 2 pages for journal papers
- The reader should understand the paper's contribution by the end of page 1
- Methods should begin by page 2-3 at the latest

### Structural Template

| Paragraph | Content | Approximate Length |
|-----------|---------|-------------------|
| 1 | Broad context and motivation -- why this problem matters | 4-6 sentences |
| 2 | Specific problem statement -- what exactly is unsolved | 3-5 sentences |
| 3 | Limitations of existing approaches (briefly) | 3-5 sentences |
| 4 | Your approach and key insight (the "a-ha" moment) | 3-5 sentences |
| 5 | Contribution bullets (2-4 items) | 2-4 bullet points |
| 6 | Paper outline (optional, some venues expect it) | 1-2 sentences |

### Contribution Bullets

- 2-4 bullets maximum (not 6+)
- Each bullet should be a complete, specific claim
- Include numbers where possible
- Order by importance, not chronology

```latex
% GOOD: Specific and verifiable
\begin{itemize}
  \item We propose X, a method that [specific mechanism].
  \item We prove that X converges at rate $O(1/\sqrt{T})$ under assumptions A and B.
  \item On benchmarks C and D, X outperforms the previous best method by 5.2\% and 3.8\%, respectively.
\end{itemize}

% BAD: Vague and unverifiable
\begin{itemize}
  \item We propose a novel framework for the problem.
  \item We conduct comprehensive experiments.
  \item We achieve state-of-the-art results.
\end{itemize}
```

---

## Gopen & Swan 7 Principles of Reader Expectation

These principles are based on how readers process English prose. Following them makes your writing easier to read, not by simplifying content, but by placing information where readers expect to find it.

### Principle 1: Subject-Verb Proximity

Keep the grammatical subject close to its verb. Long separations force readers to hold the subject in memory while parsing intervening material.

| BAD | GOOD |
|-----|------|
| "The method, which was proposed by Smith et al. in 2020 and later extended by Jones et al. to handle multi-modal distributions, converges..." | "The method converges in O(n) steps. Originally proposed by Smith et al. (2020), it was later extended by Jones et al. to handle multi-modal distributions." |

### Principle 2: Stress Position

The most important information in a sentence should appear at the end (the "stress position"). Readers naturally emphasize the last thing they read.

| BAD | GOOD |
|-----|------|
| "A 15% improvement in accuracy was achieved by our method on ImageNet." | "On ImageNet, our method achieves a 15% improvement in accuracy." |

### Principle 3: Topic Position

The beginning of a sentence (the "topic position") should contain familiar information that links to what came before. This anchors the reader.

| BAD | GOOD |
|-----|------|
| "Novel attention mechanisms have been explored. BERT uses..." | "Several attention mechanisms have been explored. Among these, BERT uses..." |

### Principle 4: Old Information Before New

Each sentence should begin with information the reader already knows ("old") and end with new information. This creates a smooth left-to-right flow.

| BAD | GOOD |
|-----|------|
| "A transformer-based architecture is our proposed solution. The problem is cross-lingual transfer." | "Cross-lingual transfer remains challenging. We address this with a transformer-based architecture that..." |

### Principle 5: One Grammatical Unit, One Function

Each clause should serve one clear purpose. Do not overload sentences with multiple competing functions.

| BAD | GOOD |
|-----|------|
| "We train the model, which has 12 layers and uses ReLU activation, on the dataset that contains 1M examples and was collected from web sources, for 100 epochs." | "The model has 12 layers with ReLU activation. We train it for 100 epochs on a dataset of 1M web-sourced examples." |

### Principle 6: Action in the Verb

Express the main action of the sentence through its verb, not through a nominalization (noun form of a verb).

| BAD (nominalization) | GOOD (action in verb) |
|---------------------|----------------------|
| "The optimization of the loss function..." | "We optimize the loss function..." |
| "The investigation of convergence properties..." | "We investigate convergence properties..." |
| "The utilization of pre-trained features..." | "We use pre-trained features..." |

### Principle 7: Context Before New Information

When a sentence introduces complex new information, provide context first so the reader has a framework for understanding it.

| BAD | GOOD |
|-----|------|
| "$\mathcal{L} = \alpha \mathcal{L}_{\text{rec}} + \beta \mathcal{L}_{\text{KL}}$ is used." | "The total loss combines reconstruction and regularization terms: $\mathcal{L} = \alpha \mathcal{L}_{\text{rec}} + \beta \mathcal{L}_{\text{KL}}$." |

### Summary Table

| # | Principle | Quick Test |
|---|-----------|-----------|
| 1 | Subject-verb proximity | Can you find the verb within 5 words of the subject? |
| 2 | Stress position | Is the most important info at sentence end? |
| 3 | Topic position | Does the sentence start with familiar info? |
| 4 | Old before new | Does old info precede new info? |
| 5 | One unit, one function | Does each clause do exactly one thing? |
| 6 | Action in verb | Is the main action a verb, not a noun? |
| 7 | Context before new | Is context provided before complex new info? |

---

## Micro-Level Tips (Perez)

### Minimize Pronoun Ambiguity

When "it", "this", "they" could refer to multiple antecedents, replace the pronoun with the specific noun.

```
% BAD: "it" is ambiguous
The encoder processes the input and the decoder generates the output. It uses attention.
% GOOD
The encoder processes the input and the decoder generates the output. The decoder uses attention.
```

### Put Verbs Early

Prefer sentence structures where the main verb appears early. This helps readers grasp the sentence's action quickly.

```
% BAD: Verb at position 15+
The multi-hypothesis network, which is trained using a winner-take-all loss, generates...
% GOOD: Verb at position 3
The network generates multiple hypotheses, trained using a winner-take-all loss.
```

### Unfold Apostrophes

In formal academic writing, avoid contractions:
- "don't" -> "do not"
- "can't" -> "cannot"
- "it's" -> "it is"
- "won't" -> "will not"

### Delete Filler Words

Words that can almost always be deleted:
- "very" -- just use a stronger adjective
- "really" -- delete
- "quite" -- delete or be specific about the degree
- "rather" -- delete or rephrase
- "somewhat" -- be specific
- "basically" -- delete
- "essentially" -- delete or rephrase
- "actually" -- delete unless correcting a misconception

---

## Word Choice (Lipton)

### Be Specific

| Vague | Specific |
|-------|---------|
| "performs well" | "achieves 92.3% accuracy" |
| "large dataset" | "dataset of 1.2M examples" |
| "recent work" | "work since 2023" or cite specific papers |
| "various methods" | name the methods |
| "significant improvement" | "5.2% improvement (p < 0.01)" |

### Eliminate Hedging (Unless Genuinely Uncertain)

| Over-hedged | Direct |
|-------------|--------|
| "It seems that the results might suggest..." | "The results show..." |
| "We believe that our method may potentially..." | "Our method [does X]" |
| "It is possible that this could lead to..." | "[X] leads to [Y]" |

Keep hedging only for genuinely uncertain claims: "This suggests (but does not prove) that..."

### Avoid Incremental Vocabulary

Words that signal "this is a minor contribution" and should be avoided unless you truly mean it:
- "incremental" -> describe the specific advance
- "slight" -> give the number
- "modest" -> give the number
- "preliminary" -> if the results are preliminary, consider waiting to publish

---

## Precision (Steinhardt)

### Consistent Terminology

Pick one term for each concept and use it throughout the paper. Do not alternate between synonyms for the same thing.

| Inconsistent | Consistent |
|-------------|-----------|
| "model" / "network" / "architecture" / "system" (for the same thing) | Pick "model" and use it everywhere |
| "training" / "learning" / "optimization" (for the same process) | Pick "training" and use it everywhere |
| "performance" / "accuracy" / "results" (for the same metric) | Use the specific metric name |

Exception: It is acceptable to use a short form after defining it: "our multi-hypothesis network (MHN)" then use "MHN" throughout.

### State Assumptions Formally

| Informal | Formal |
|---------|--------|
| "We assume the data is nice" | "We assume the data is drawn i.i.d. from distribution $\mathcal{D}$" |
| "Under reasonable conditions" | "Under Assumptions 1-3 (stated in Section 3.1)" |
| "For typical inputs" | "For inputs satisfying $\|x\| \leq B$" |

---

## Mathematical Notation Conventions

### Standard Conventions

| Entity | Convention | Example |
|--------|-----------|---------|
| Scalars | Lowercase italic | $x$, $\alpha$, $n$ |
| Vectors | Lowercase bold | $\bm{x}$, $\bm{\theta}$ |
| Matrices | Uppercase bold | $\bm{A}$, $\bm{W}$ |
| Sets | Calligraphic uppercase | $\mathcal{S}$, $\mathcal{D}$ |
| Random variables | Uppercase italic | $X$, $Y$ |
| Functions | Lowercase roman or italic | $f(x)$, $\text{ReLU}(x)$ |
| Operators | Roman (upright) | $\operatorname{argmax}$, $\mathbb{E}$ |
| Constants | Roman (upright) | $\mathrm{e}$ (Euler's number), $\pi$ |

### LaTeX Implementation

```latex
% Recommended packages
\usepackage{bm}          % \bm for bold math
\usepackage{amsmath}      % Standard math environments
\usepackage{amssymb}      % \mathbb, \mathcal
\usepackage{mathtools}    % Extensions to amsmath

% Custom commands for consistency
\newcommand{\vect}[1]{\bm{#1}}           % Vectors
\newcommand{\mat}[1]{\bm{#1}}            % Matrices
\newcommand{\set}[1]{\mathcal{#1}}       % Sets
\newcommand{\real}{\mathbb{R}}           % Real numbers
\newcommand{\expect}{\mathbb{E}}         % Expectation
\newcommand{\prob}{\mathbb{P}}           % Probability
\newcommand{\transpose}{^\top}           % Transpose
```

### Notation Table

Include a notation table in the paper (or appendix) if using more than 10 symbols:

```latex
\begin{table}[h]
\caption{Notation used throughout this paper.}
\centering
\begin{tabular}{cl}
\toprule
Symbol & Description \\
\midrule
$\vect{x}$ & Input vector \\
$\vect{\theta}$ & Model parameters \\
$\mat{W}$ & Weight matrix \\
$\set{D}$ & Training dataset \\
$N$ & Number of training examples \\
$d$ & Input dimensionality \\
\bottomrule
\end{tabular}
\end{table}
```

---

## Figure Design Principles

### Technical Requirements

- **Format**: Vector graphics (PDF) for plots and diagrams. PNG (450+ DPI) only for photographs or screenshots.
- **Size**: Design for the final print size. A figure that looks good at full-screen may be unreadable in a two-column format.
- **Fonts**: Match the paper's body font size. Axis labels and legends should be at least 8pt at print size.
- **Line width**: Minimum 1pt for plot lines, 0.5pt for axes.

### Colorblind Safety

Use colorblind-safe palettes (see `references/color-palettes.md`). The Okabe-Ito palette is recommended:
- Never rely on color alone to distinguish data series -- also vary line style (solid, dashed, dotted) or marker shape.

### Self-Contained Captions

The caption should allow the figure to be understood without reading the body text:
- What the figure shows
- How to read it (what axes/colors/symbols mean)
- The key takeaway

```latex
% GOOD: Self-contained caption
\caption{Training loss (blue, left axis) and validation accuracy (orange, right axis)
over 100 epochs. The model converges after approximately 60 epochs, with validation
accuracy plateauing at 94.2\%.}

% BAD: Requires reading the paper
\caption{Training curves for our method.}
```

### Figure 1 is Critical

Figure 1 (the "hero figure" or "teaser figure") is the most important figure in the paper:
- Reviewers look at it first
- It should convey the paper's core idea at a glance
- It should be beautiful and polished
- Common choices: system overview, method comparison, key result visualization
- Invest 25% of your total figure-making effort on Figure 1

### Placement

- Figures should appear near their first reference in the text (same page or facing page)
- Use `[t]` (top of page) for most figures
- Never use `[h]` alone -- use `[ht]` or `[htbp]`
- Avoid `[H]` from the `float` package -- it can cause large blank spaces
