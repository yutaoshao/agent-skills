# Module 02: Literature Review

Literature search, organization, and review writing. This module produces a thematically organized literature review that identifies research gaps and positions the contribution within the existing body of work.

## When to Load

Load this module when the user says: "literature review", "find papers", "related work", "survey", "search literature", "find references", or when executing Stage S2 of a full paper writing project.

## Prerequisites

- Confirmed contribution hypothesis from Module 01 (or equivalent user description)
- Target venue identified (affects scope and depth expectations)
- Load `references/citation-guide.md` alongside this module

## Procedure

### Step 1: Generate Search Strategy

Construct a systematic search plan tailored to the research contribution.

**Actions:**

1. From the confirmed contribution, extract 3-5 core concepts. For example, if the contribution is "a neural network for inverse kinematics using particle swarm optimization," the core concepts are: neural networks, inverse kinematics, particle swarm optimization, hybrid optimization, robotics.
2. For each core concept, generate:
   - **Primary keywords**: The exact technical term (e.g., "inverse kinematics")
   - **Synonyms and variants**: Alternative names, abbreviations, spellings (e.g., "IK", "inverse kinematic problem", "analytical IK", "numerical IK")
   - **Broader terms**: Parent categories (e.g., "robot motion planning", "kinematic analysis")
   - **Narrower terms**: Specific subtopics (e.g., "redundant manipulator IK", "6-DOF IK")
3. Construct Boolean search queries by combining concepts:
   ```
   Query 1 (intersection of main concepts):
   ("inverse kinematics" OR "IK") AND ("neural network" OR "deep learning") AND ("particle swarm" OR "PSO")

   Query 2 (method in domain):
   ("neural network" OR "deep learning") AND ("inverse kinematics") AND ("robot" OR "manipulator")

   Query 3 (competing approaches):
   ("inverse kinematics") AND ("learning-based" OR "data-driven") AND ("real-time")

   Query 4 (survey/overview):
   ("inverse kinematics") AND ("survey" OR "review" OR "overview" OR "tutorial")
   ```
4. Select appropriate databases for each query:

   | Database | Strengths | Access |
   |---|---|---|
   | Semantic Scholar | CS/AI papers, citation graphs, free API | WebSearch + API |
   | Google Scholar | Broadest coverage, good for interdisciplinary | WebSearch |
   | arXiv | Preprints, CS/ML latest work | WebSearch |
   | IEEE Xplore | Engineering, robotics, signal processing | WebSearch (abstracts free) |
   | ACM DL | Computer science, HCI | WebSearch (abstracts free) |
   | PubMed | Biomedical, if relevant | WebSearch |
   | DBLP | CS publication metadata, author disambiguation | WebSearch |

5. Record the search strategy in `plan/notes.md` under "Literature Search Strategy".

### Step 2: English Literature Search

Execute the search strategy using available tools.

**Actions:**

1. **WebSearch execution**: Run each Boolean query through `WebSearch`. For each query:
   - Search with the query string
   - Search with the query string + "2024" or "2025" to prioritize recent work
   - Search with the query string + target venue name (e.g., "NeurIPS", "ICML")

2. **Semantic Scholar API workflow** (preferred for structured data):
   ```
   For each key paper found:
   1. Search: WebSearch("Semantic Scholar [paper title]")
   2. Get paper ID from the Semantic Scholar URL
   3. Fetch citation data: WebFetch("https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,year,venue,citationCount,references,citations")
   4. Follow high-citation references and citations to discover related work
   ```

3. **Snowball search**: From 3-5 seed papers (the most relevant found so far):
   - **Backward snowball**: Check their reference lists for papers you missed
   - **Forward snowball**: Check who cites them for more recent follow-up work
   - Use Semantic Scholar citation/reference API for this

4. **Coverage targets**:
   - Find at least 5-8 papers per core concept
   - Ensure at least 30% of papers are from the last 3 years
   - Include at least 1-2 survey papers for context
   - Include the seminal/foundational paper for each technique used

5. For each paper found, record in a structured format:
   ```markdown
   - **[Author et al., Year]** "Title" -- Venue
     - Relevance: [one sentence explaining why this paper matters to our work]
     - Relation: [how it relates: same method, same domain, competing approach, foundational]
     - Key finding: [the main result or contribution]
     - BibTeX status: [found/needed/placeholder]
   ```

### Step 3: Chinese Literature Search Strategy

For Chinese-language literature, provide the user with a ready-to-use search strategy since Chinese academic databases (CNKI, Wanfang, CSCD) require authenticated access.

**Actions:**

1. Generate Chinese search keywords corresponding to each English core concept:
   ```
   English: "inverse kinematics" -> Chinese: "逆运动学", "反向运动学"
   English: "neural network" -> Chinese: "神经网络", "深度学习"
   English: "particle swarm optimization" -> Chinese: "粒子群优化", "粒子群算法", "PSO算法"
   ```

2. Construct Chinese Boolean queries for CNKI:
   ```
   主题 = ("逆运动学" + "神经网络") * ("机器人" + "机械臂")
   主题 = ("粒子群" + "运动学求解") * "优化"
   ```

3. Provide the user with a search instruction card:
   ```markdown
   ## Chinese Literature Search Card

   Please search the following databases and share the results:

   ### CNKI (知网) - https://www.cnki.net
   Queries:
   1. [Chinese query 1]
   2. [Chinese query 2]
   Settings: Sort by citation count, filter last 5 years, source = "核心期刊" + "CSCD"

   ### Wanfang (万方) - https://www.wanfangdata.com.cn
   Queries:
   1. [Chinese query 1]
   Settings: Filter "SCI/EI收录"

   ### Expected Output
   For each relevant paper, please provide:
   - Title (Chinese and English if available)
   - Authors
   - Journal name and year
   - DOI (if available)
   - One-sentence summary of relevance
   ```

4. **Critical rule**: NEVER generate Chinese citations from memory. Chinese paper metadata is especially prone to hallucination. Always wait for user-provided data.

### Step 4: Literature Organization

Organize found papers thematically, not paper-by-paper.

**Actions:**

1. **Thematic clustering**: Group all collected papers into 3-6 themes based on their relationship to the contribution. Common thematic structures:

   - **By methodology family**:
     - Analytical/geometric approaches
     - Optimization-based approaches
     - Learning-based approaches
     - Hybrid approaches (our work belongs here)

   - **By problem aspect**:
     - Problem formulation and representation
     - Solution accuracy and precision
     - Computational efficiency and real-time capability
     - Generalization and robustness

   - **By chronological evolution**:
     - Foundational work (established the problem)
     - Classical approaches (dominated for years)
     - Modern approaches (current state of the art)
     - Emerging directions (where the field is heading, our work included)

2. **Within each theme**, organize papers by:
   - Chronological order (oldest to newest) to show evolution
   - Logical progression (simpler to more complex) to build understanding
   - Relevance (least to most relevant to our work) to build toward our contribution

3. Record the thematic structure in `plan/notes.md` under "Literature Organization".

### Step 5: Gap Analysis

Identify what is missing in the existing literature that justifies the current work.

**Actions:**

Analyze the collected literature across four gap dimensions:

| Gap Type | Question | How to Identify | Maps to Paper |
|---|---|---|---|
| **Temporal Gap** | Is there recent work on this combination of ideas? | Check if the intersection of core concepts has papers from the last 2-3 years | Introduction (motivation for timeliness) |
| **Methodological Gap** | Has this specific approach been tried? | Check if the proposed method combination exists in the literature | Introduction (novelty claim) + Related Work |
| **Performance Gap** | Do existing methods fall short on specific metrics? | Compare reported results across papers | Introduction (problem statement) + Experiments |
| **Domain Gap** | Has this technique been applied to this domain? | Check for cross-pollination between method and application domains | Introduction (contribution) + Related Work |
| **Theoretical Gap** | Is there missing analysis or understanding? | Check for empirical-only work lacking theoretical grounding | Methods (if providing theory) |
| **Scale/Practical Gap** | Do existing methods work at practical scale? | Check for limitations in existing evaluations (toy problems, small datasets) | Experiments (if demonstrating scale) |

For each identified gap, write a one-paragraph statement:
```markdown
**[Gap Type] Gap:** [Description of what is missing]
- Evidence: [Which papers/absence of papers supports this gap]
- Our contribution addresses this by: [How our work fills this gap]
```

Record gap analysis in `plan/notes.md` under "Research Gaps".

### Step 6: Write Synthesized Literature Review

Draft the Related Work section as a synthesized narrative, not a paper-by-paper summary.

**Actions:**

Structure the review following this outline:

```
## Related Work

### Opening Paragraph (1 paragraph)
- State the scope: what areas of prior work are relevant
- Explain the organizational principle (by method, by aspect, etc.)
- Foreshadow the gap this paper addresses

### Theme 1: [Name] (1-3 paragraphs)
- Summarize the core idea and evolution of this approach family
- Cite key papers as part of the narrative, not as isolated summaries
- End with the limitation or gap that motivates the next theme or our work

### Theme 2: [Name] (1-3 paragraphs)
- Same structure as Theme 1
- Explicitly connect to Theme 1 where relevant (contrast, complement, extension)

### Theme 3: [Name] (1-3 paragraphs)
- Same structure

### [Additional themes as needed]

### Positioning Paragraph (1 paragraph)
- Clearly state how our work relates to and differs from each theme
- Articulate what combination of strengths our approach offers
- Do NOT claim novelty that the experiments have not validated
```

**Writing rules for the review:**

1. **Synthesize, do not summarize**: Group papers by what they contribute to understanding the problem, not by individual paper contents.
   ```
   BAD: "Smith et al. (2020) proposed method A. Jones et al. (2021) proposed method B. Lee et al. (2022) proposed method C."
   GOOD: "Optimization-based approaches to IK have evolved from classical Jacobian methods [Smith 2020] through learned initialization strategies [Jones 2021] to fully differentiable pipelines [Lee 2022], progressively trading analytical guarantees for computational speed."
   ```

2. **Show evolution**: Within each theme, papers should flow from earlier/simpler to later/more complex, showing the intellectual progression.

3. **Connect to our work**: Every theme should end with a sentence or two explaining what gap remains, setting up why our approach is needed.

4. **Cite generously but meaningfully**: Every citation should serve a purpose (establishing fact, crediting method, acknowledging prior art, contrasting approach). No citation dumping.

5. **Be fair to prior work**: Acknowledge strengths before discussing limitations. Do not misrepresent competitors.

## Citation Anti-Hallucination Protocol

This protocol applies throughout the entire module. Violations are unacceptable.

| Situation | Required Action |
|---|---|
| Found a paper via WebSearch with full metadata | Safe to cite. Fetch BibTeX via DOI if available. |
| Remember a paper but cannot find it via search | Do NOT cite. Mark as `[CITATION NEEDED: description of what should go here]`. |
| Found a paper but cannot verify authors/year/venue | Mark as `\cite{PLACEHOLDER_verify_[description]}` and inform user. |
| User provides a citation | Verify via WebSearch before adding to .bib. Trust user if verification fails but note the uncertainty. |
| Need "some paper about X" for a general claim | Search for it. If not found in 2 search attempts, rephrase the claim to not require a citation or mark as placeholder. |

## Deliverables

Upon completing this module:

1. **Literature database** (in `plan/notes.md` or a dedicated `plan/literature.md`):
   - All found papers in structured format
   - Thematic organization
   - Gap analysis
2. **Related Work draft** (in the paper `.tex` file or a staging file):
   - Synthesized, thematically organized review
   - All citations verified or marked as placeholders
3. **`references.bib`** updated with:
   - New BibTeX entries for all verified papers
   - Placeholder entries clearly marked
4. **`plan/progress.md`** updated with:
   - S2 Literature Review: COMPLETE
   - Number of papers found, organized, cited
   - Any placeholder citations requiring user verification
   - Next action: proceed to S3 (Paper Structure)

## Common Pitfalls

- **Pitfall:** Generating citations from memory. AI-generated citations have approximately 40% error rate. Every single citation must be verified through search.
- **Pitfall:** Writing a "list of summaries" instead of a synthesized review. Each paragraph should discuss multiple papers around a common theme or progression.
- **Pitfall:** Only finding papers that support the contribution. Actively search for competing approaches and strong baselines. Reviewers will notice if key competitors are absent.
- **Pitfall:** Ignoring non-English literature when it is relevant. For fields with significant Chinese research output (e.g., robotics, NLP), the Chinese literature search card is essential.
- **Pitfall:** Over-citing surveys and under-citing primary sources. Surveys establish context; primary sources establish credit and accuracy. Both are needed.
