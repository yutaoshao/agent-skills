# Citation Expansion Guide

Methodology for analyzing citation gaps and integrating new references into academic papers.

## Gap Analysis Framework

### Step 1: Count and Categorize Existing References

Parse `references.bib` and classify each entry:
- **Foundational** (textbooks, seminal papers, >10 years old)
- **Methodological** (papers describing techniques used in this work)
- **Comparative** (papers describing baseline/comparison methods)
- **Recent survey** (review papers establishing the field context)
- **Recent advance** (papers from last 2-3 years showing state of the art)
- **Domain application** (papers applying similar methods to similar problems)

### Step 2: Identify Gaps

Check each of the following citation expectations:

**Introduction gaps:**
- Every named method or technique should have its canonical citation
- Every factual claim about limitations should cite evidence
- The problem statement should cite foundational works
- The related work survey should cite at least one survey paper
- Recent advances (last 2-3 years) should constitute 30%+ of Introduction citations

**Method section gaps:**
- Every algorithm, loss function, or architectural choice derived from prior work needs a citation
- Optimization techniques (Adam, SGD variants) should cite their papers
- Evaluation metrics should cite their definitions if non-standard

**Experiments gaps:**
- Every baseline method should cite its original paper
- Experimental setup details borrowed from other papers need citations
- Dataset sources need citations

**Discussion gaps:**
- Comparisons to other work should cite the compared papers
- Claims about practical implications should cite application-domain references
- Limitations discussed should cite papers that address those limitations

### Step 3: Source High-Quality References

Priority ranking for reference sources:
1. Peer-reviewed journal papers (target journal and related high-impact journals)
2. Top conference papers (domain-specific A*/A conferences)
3. Letters (short-form journals like IEEE RA-L)
4. arXiv preprints (only when no published version exists and the work is highly relevant)
5. Technical reports and theses (sparingly)

Avoid:
- Predatory journals
- Non-peer-reviewed blog posts or white papers
- Papers with incomplete bibliographic metadata

### Step 4: BibTeX Quality Standards

Every new BibTeX entry must include:
- Complete author names (not "et al." in the .bib file)
- Full journal/conference name
- Volume, number, pages (when available)
- Year
- Publisher
- Consistent formatting with existing entries in the .bib file

### Step 5: Natural Integration

**Integration strategies:**

1. **Inline narrative citation**: Weave the reference into the sentence as part of the argument.
   ```latex
   % GOOD
   Recent work on normalizing flows for IK \cite{ames2022ikflow} demonstrated that ...
   ```

2. **Parenthetical support**: Add citation to support a claim already made.
   ```latex
   % GOOD
   PSO convergence theory has been extensively studied \cite{clerc2002particle, poli2007pso_overview}.
   ```

3. **Contrastive citation**: Introduce a reference to highlight what this paper does differently.
   ```latex
   % GOOD
   Unlike \cite{jiang2022nn_nr}, which relies on a single-output network, our approach ...
   ```

**Anti-patterns to avoid:**

- **Citation dumping**: Adding `\cite{a,b,c,d,e}` at the end of a paragraph without context
- **Orphan citations**: Citing a paper but never discussing what it contributes
- **Disconnected citations**: Adding citations in places unrelated to the cited work

## Target Metrics by Paper Type

| Paper Type | Target Total | Minimum Recent (3yr) |
|-----------|-------------|---------------------|
| Letter / Short Paper | 20-30 | 8-10 |
| Full Research Paper | 35-50 | 12-18 |
| Survey / Review | 80-150+ | 30+ |

## Journal-Specific Considerations

When the target journal is known:
- Check the journal's typical reference count by examining 3-5 recent papers
- Match the citation style (numbered vs. author-year)
- Prefer citing papers published in the same journal (demonstrates relevance)
- Check if the journal has any reference formatting requirements
