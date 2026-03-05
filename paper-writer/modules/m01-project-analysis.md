# Module 01: Project Analysis

Explore a research repository to extract contributions, methods, and results for paper writing. This module transforms a codebase into a structured understanding of what the paper should communicate.

## When to Load

Load this module when the user says: "analyze code", "extract contributions", "understand repo", "paper from code", "what does this project do", or when beginning a full paper writing project (Stage S1).

## Prerequisites

- Access to the research project repository (local path or cloned repo)
- User available for contribution confirmation (Step 3)

## Procedure

### Step 1: Explore Repository Structure

Map the project layout to understand what components exist and how they relate.

**Actions:**

1. Run `ls -la` on the project root to identify top-level structure.
2. Use `Glob` with patterns `**/*.py`, `**/*.ipynb`, `**/*.sh`, `**/*.yaml`, `**/*.json` to catalog all code and configuration files.
3. Identify the architectural layers:
   - `models/` or `networks/` or `architectures/` -- core method implementation
   - `data/` or `datasets/` or `loaders/` -- data pipeline
   - `train*.py` or `runners/` -- training logic
   - `eval*.py` or `test*.py` or `inference*.py` -- evaluation and inference
   - `configs/` or `*.yaml` -- hyperparameter and experiment configuration
   - `results/` or `outputs/` or `logs/` or `wandb/` -- experimental results
   - `scripts/` or `tools/` -- utility and orchestration scripts
   - `figures/` or `plots/` or `vis*/` -- visualization code or outputs
4. Record the structure in `plan/project-overview.md` under a "Repository Map" section.

**Output:** A directory tree annotated with the purpose of each major component.

### Step 2: Read Documentation and Results

Extract the existing narrative and quantitative evidence from the project.

**Actions:**

1. Read `README.md` (or `README.rst`, `docs/`) completely. Extract:
   - Stated purpose and contribution claims
   - Reported results (accuracy, latency, any metrics)
   - Method description and pipeline overview
   - Dependencies and environment requirements
2. Search for result files using `Glob` with patterns: `**/results*.json`, `**/metrics*.json`, `**/logs/*.csv`, `**/*.log`, `**/wandb/**summary*.json`.
3. Read any Jupyter notebooks (`**/*.ipynb`) that contain analysis, visualization, or result summaries.
4. Check for existing paper drafts: `**/*.tex`, `**/paper/`, `**/manuscript/`, `**/draft/`.
5. Read experiment configuration files to understand hyperparameters, baselines, and ablation settings.

**Output:** A "Findings Summary" with: (a) claimed contributions, (b) key quantitative results, (c) method pipeline description, (d) baselines compared against.

### Step 3: Identify Main Contribution with User

Present a contribution hypothesis for user confirmation. Do NOT proceed to outlining or writing without this confirmation.

**Actions:**

1. Based on Steps 1-2, draft a Contribution Hypothesis using the template below.
2. Present it to the user and ask for confirmation or correction.
3. If the user corrects or refines, update `plan/project-overview.md` with the confirmed contribution.

**Contribution Hypothesis Template:**

```markdown
## Contribution Hypothesis

### One-Sentence Contribution
[What this paper contributes, in one sentence. Example: "We propose X, a method that achieves Y by doing Z."]

### Research Question
[The question this work answers. Example: "Can neural implicit representations be efficiently optimized for real-time robotics applications?"]

### Methodology Summary
[2-3 sentences describing HOW the contribution works. What is the core technical idea?]

### Key Findings
1. [Primary result with numbers. Example: "Achieves 95.3% accuracy on benchmark X, outperforming prior best by 3.2%."]
2. [Secondary result or property. Example: "Runs at 120fps on a single GPU, 10x faster than baseline Y."]
3. [Additional finding if applicable. Example: "Ablation confirms that component Z accounts for 60% of the improvement."]

### Interpretation
[What do these findings mean for the field? Why should readers care?]

### Limitations
[Known limitations, failure cases, or scope restrictions.]

### Novelty Type
- [ ] New method/algorithm
- [ ] New application of existing method to new domain
- [ ] New theoretical result or analysis
- [ ] New dataset or benchmark
- [ ] Significant empirical study with new insights
- [ ] System/engineering contribution

### Target Venue (if known)
[Conference or journal name, page limit, deadline]
```

**Critical Rule:** If the user's description of the contribution differs from what the code suggests, trust the user. The user knows their research intent; the code may reflect intermediate experiments or incomplete implementations.

### Step 4: Find Existing Citations in Code

Identify references already embedded in the codebase.

**Actions:**

1. Search for citation-like patterns in code comments and docstrings:
   - `Grep` for patterns: `arxiv`, `doi`, `http.*paper`, `\[\d+\]`, `et al`, `(20\d\d)`, `reference`, `based on`, `following`, `adapted from`, `inspired by`
2. Search README and docs for reference lists, "Related Work" sections, or bibliography.
3. Check for existing `.bib` files: `Glob` for `**/*.bib`.
4. Extract and deduplicate all found references into a preliminary reference list.
5. Record findings in `plan/notes.md` under "Existing Citations from Code".

**Output:** A list of papers already referenced or acknowledged in the codebase, with as much bibliographic detail as available.

### Step 5: Search Additional Literature

Perform an initial literature scan to contextualize the contribution.

**Actions:**

1. Based on the confirmed contribution, generate 3-5 search queries targeting:
   - The specific method or technique name
   - The problem domain + "survey" or "review"
   - Key baseline method names + "comparison"
   - The application area + "state of the art"
2. Use `WebSearch` to find recent relevant papers (last 3 years priority).
3. For each found paper, record: title, authors, year, venue, and one-sentence relevance note.
4. Identify 3-5 papers that are most directly comparable (same problem, same approach family).
5. Record in `plan/notes.md` under "Initial Literature Scan".

**Important:** This is a preliminary scan, not the full literature review (that is Module 02). The goal here is to understand the competitive landscape enough to frame the contribution correctly.

### Step 6: Map Code Artifacts to Paper Sections

Create a mapping from repository files to paper sections. This mapping guides all subsequent modules.

**Actions:**

Use the following mapping guide to connect code artifacts to paper sections:

| Repository Artifact | Paper Section | What to Extract |
|---|---|---|
| `README.md`, project description | Abstract, Introduction | Contribution claims, motivation, high-level pipeline |
| `models/`, `networks/`, core algorithm files | Methods (Section 3-4) | Architecture details, algorithmic steps, design choices |
| `losses/`, `objectives/`, loss function code | Methods (subsection) | Loss function formulation, training objectives |
| `data/`, `datasets/`, data loading code | Experiments - Setup (Section 5.1) | Dataset descriptions, preprocessing, splits |
| `configs/`, hyperparameter files | Experiments - Setup (Section 5.1) | Hyperparameter values, training details |
| `train*.py`, training scripts | Methods + Experiments | Training procedure, optimization details |
| `eval*.py`, `test*.py`, evaluation scripts | Experiments - Metrics (Section 5.2) | Evaluation protocol, metrics used |
| `results/`, `outputs/`, result files | Experiments - Results (Section 5.3) | Quantitative results, comparison tables |
| `ablation*/`, ablation configs/results | Experiments - Ablations (Section 5.4) | Component-wise analysis, design justifications |
| `figures/`, `plots/`, visualization code | Figures throughout paper | Qualitative results, architecture diagrams, plots |
| `baselines/`, comparison code | Related Work + Experiments | Baseline descriptions, fair comparison setup |
| `scripts/demo*`, inference examples | Introduction (motivation) + Experiments | Use cases, practical demonstrations |
| Comments citing papers, docstrings | Related Work (Section 2) | Prior art, methodological lineage |
| `requirements.txt`, `environment.yaml` | Experiments - Setup (footnote) | Software stack, compute environment |
| `LICENSE`, `NOTICE` | Paper metadata | Open-source commitment, reproducibility |

Record this mapping in `plan/project-overview.md` under "Artifact-to-Section Mapping". Include specific file paths, not just directory names.

## Five-Dimension Analysis Framework

Throughout the analysis, evaluate the project along five dimensions to ensure comprehensive coverage. Each dimension maps to specific paper content:

| Dimension | Questions to Answer | Maps to Paper Section |
|---|---|---|
| **Research Question** | What problem is being solved? Why does it matter? What gap does it fill? | Introduction (problem statement, motivation) |
| **Methodology** | What is the technical approach? What are the key design choices? What is novel vs. borrowed? | Methods (algorithm, architecture, training) |
| **Findings** | What are the quantitative results? How do they compare to baselines? What patterns emerge? | Experiments (tables, figures, analysis) |
| **Interpretation** | What do the results mean? Why does the method work? What are the failure modes? | Discussion, Analysis subsections |
| **Limitations** | What does the method NOT do? Where does it fail? What assumptions does it make? | Limitations section, Future Work |

## Deliverables

Upon completing this module, the following should be ready:

1. **`plan/project-overview.md`** updated with:
   - Repository Map (annotated directory structure)
   - Confirmed Contribution Hypothesis
   - Artifact-to-Section Mapping (specific file paths to paper sections)
   - Five-Dimension Analysis summary
2. **`plan/notes.md`** updated with:
   - Existing Citations from Code
   - Initial Literature Scan
   - Open questions or ambiguities for user
3. **`plan/progress.md`** updated with:
   - S1 Project Analysis: COMPLETE
   - Key decisions made (contribution framing, target venue)
   - Next action: proceed to S2 (Literature Review) or S3 (Paper Structure)

## Common Pitfalls

- **Pitfall:** Assuming the latest code is the final method. Research repos often contain abandoned experiments. Always confirm with the user which components are part of the contribution.
- **Pitfall:** Overcomplicating the contribution. If the code does one thing well, the paper should claim one thing. Resist inflating a single contribution into three.
- **Pitfall:** Ignoring negative results. Check for disabled experiments, commented-out baselines, or result files that show the method underperforming. These inform the Limitations section.
- **Pitfall:** Missing the "so what." Technical novelty alone is not enough. Always articulate why the contribution matters to the target audience (practical impact, theoretical insight, enabling new capabilities).
