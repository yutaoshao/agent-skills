# Citation Guide

Comprehensive reference for citation management in academic papers. Covers anti-hallucination protocols, verification workflows, gap analysis, integration strategies, target metrics, and API usage.

---

## Part 1: Anti-Hallucination Protocol (CRITICAL)

**AI-generated citations have an approximately 40% error rate.** This is the single most important rule in citation management. Errors include:

- Fabricated papers that do not exist
- Real authors attributed to non-existent papers
- Correct paper titles with wrong authors, years, or venues
- Plausible-sounding DOIs that resolve to nothing
- Correct papers cited for claims they do not actually make

### Absolute Rules

1. **NEVER generate BibTeX entries from memory.** Every BibTeX entry must come from a verified source (DOI resolution, publisher page, or Semantic Scholar/arXiv metadata).
2. **NEVER assert a paper exists without verification.** If you recall a paper but cannot verify it, mark it as a placeholder.
3. **Placeholder marking format**:
   ```latex
   % In the .tex file:
   Prior work on neural IK~\cite{PLACEHOLDER_neural_ik_2022}

   % In the .bib file:
   @misc{PLACEHOLDER_neural_ik_2022,
     title = {[UNVERIFIED] Neural IK approach, ~2022, verify before submission},
     note = {PLACEHOLDER - DO NOT SUBMIT}
   }
   ```
4. **Always inform the user** about any placeholder citations, including a count and list of descriptions.

### Why This Matters

A single fabricated reference can:
- Lead to desk rejection
- Damage the authors' credibility
- Trigger plagiarism/fabrication investigations
- Undermine reviewer trust in all other citations

---

## Part 2: 5-Step Verification Workflow

Every citation must pass through this pipeline:

### Step 1: Search

Query multiple sources to find the paper:

```
Primary:   Semantic Scholar API (semanticscholar.org)
Secondary: Google Scholar (via WebSearch)
Tertiary:  arXiv search (arxiv.org)
Fallback:  CrossRef (crossref.org), OpenAlex (openalex.org)
```

Search strategies:
- **By title**: Use the exact title in quotes
- **By author + topic**: `author:LastName topic_keywords`
- **By DOI**: Direct lookup if DOI is known

### Step 2: Verify

Confirm the paper exists using 2+ independent sources:

| Verification Level | Sources Required | Use Case |
|-------------------|-----------------|----------|
| Confirmed | 2+ sources agree on title, authors, year, venue | Safe to cite |
| Partially verified | 1 source found, details match | Acceptable, note uncertainty |
| Unverified | 0 sources found | Mark as PLACEHOLDER |

Cross-check these fields:
- Title (exact match)
- Author list (at least first author matches)
- Year (exact match)
- Venue (conference/journal name)

### Step 3: Retrieve BibTeX via DOI

The most reliable path to correct BibTeX:

```python
import requests

def doi_to_bibtex(doi: str) -> str:
    """Fetch BibTeX from DOI via CrossRef content negotiation."""
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"DOI {doi} not found or no BibTeX available")
```

Alternative BibTeX sources (in priority order):
1. DOI content negotiation (above)
2. Semantic Scholar API (returns structured data, convert to BibTeX)
3. Publisher page "Cite this article" button
4. arXiv abstract page "BibTeX" link
5. DBLP (dblp.org) for CS conference/journal papers

### Step 4: Validate Claim

After obtaining the paper, verify that it actually supports the claim being made:

- Read the abstract and relevant sections
- Confirm the specific finding being cited
- Check that the citation context accurately represents the paper's contribution
- Flag any misrepresentations

### Step 5: Add to Bibliography

- Insert the BibTeX entry into the `.bib` file
- Ensure the cite key follows the project's naming convention (e.g., `lastname2024keyword`)
- Verify no duplicate keys exist
- Add the `\cite{}` command in the appropriate location in the `.tex` file

---

## Part 3: Gap Analysis Framework

### Step 1: Count and Categorize Existing References

Parse `references.bib` and classify each entry into 6 types:

| Category | Description | Example |
|----------|------------|---------|
| **Foundational** | Textbooks, seminal papers, >10 years old | Goodfellow et al. 2016 (Deep Learning textbook) |
| **Methodological** | Papers describing techniques used in this work | The optimizer paper, the architecture paper |
| **Comparative** | Papers describing baseline/comparison methods | Methods compared against in experiments |
| **Recent Survey** | Review papers establishing field context | "A Survey of X" papers |
| **Recent Advance** | Papers from last 2-3 years showing SOTA | Latest results on the same benchmarks |
| **Domain Application** | Papers applying similar methods to similar problems | Related applications in the same field |

### Step 2: Identify Gaps Per Section

**Introduction gaps**:
- Every named method or technique should have its canonical citation
- Every factual claim about limitations should cite evidence
- The problem statement should cite foundational works
- The related work survey should cite at least one survey paper
- Recent advances (last 2-3 years) should constitute 30%+ of Introduction citations

**Method section gaps**:
- Every algorithm, loss function, or architectural choice derived from prior work needs a citation
- Optimization techniques (Adam, SGD variants) should cite their original papers
- Evaluation metrics should cite their definitions if non-standard
- Pre-trained models should cite their source papers

**Experiments gaps**:
- Every baseline method should cite its original paper
- Experimental setup details borrowed from other papers need citations
- Dataset sources need citations
- Evaluation protocols from other papers need citations

**Discussion/Related Work gaps**:
- Comparisons to other work should cite the compared papers
- Claims about practical implications should cite application-domain references
- Limitations discussed should cite papers that address those limitations
- Concurrent work should be cited and discussed

### Step 3: Source Quality Ranking

Priority ranking for reference sources:

1. **Peer-reviewed journal papers** -- target journal and related high-impact journals
2. **Top conference papers** -- domain-specific A*/A conferences (NeurIPS, ICML, ICLR, ACL, CVPR, etc.)
3. **Workshop papers and letters** -- short-form venues (IEEE RA-L, EMNLP Findings, etc.)
4. **arXiv preprints** -- only when no published version exists and the work is highly relevant
5. **Technical reports and theses** -- sparingly, for implementation details or datasets
6. **Blog posts and white papers** -- avoid in formal papers; use only as supplementary references

**Avoid**:
- Predatory journals (check against Beall's list)
- Non-peer-reviewed blog posts or white papers as primary evidence
- Papers with incomplete bibliographic metadata
- Self-published work without peer review

### Step 4: BibTeX Quality Standards

Every BibTeX entry must include:

| Field | Required | Notes |
|-------|----------|-------|
| author | Yes | Complete names (not "et al." in the .bib file) |
| title | Yes | Exact title, proper capitalization in braces |
| year | Yes | Publication year |
| journal/booktitle | Yes | Full journal/conference name |
| volume | When available | Journal volume |
| number | When available | Journal issue number |
| pages | When available | Page range with en-dash |
| publisher | When available | Publisher name |
| doi | Highly recommended | Digital Object Identifier |

**Formatting rules**:
```bibtex
% GOOD: Complete entry with proper formatting
@inproceedings{vaswani2017attention,
  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\L}ukasz and Polosukhin, Illia},
  title     = {Attention is All You Need},
  booktitle = {Advances in Neural Information Processing Systems},
  volume    = {30},
  year      = {2017},
  publisher = {Curran Associates, Inc.}
}

% BAD: Incomplete entry
@article{vaswani2017,
  author = {Vaswani et al.},
  title = {Attention is all you need},
  year = {2017}
}
```

**Title capitalization**: Protect proper nouns and acronyms with braces: `{ImageNet}`, `{BERT}`, `{Transformer}`.

### Step 5: Natural Integration

See Part 4 below.

---

## Part 4: Integration Strategies

### Inline Narrative Citation

Weave the reference into the sentence as part of the argument:

```latex
% GOOD: Citation as part of the narrative
Recent work by \citet{ames2022ikflow} demonstrated that normalizing flows can
solve IK problems with multi-modal solution distributions.
```

### Parenthetical Support

Add citation to support a claim already made:

```latex
% GOOD: Citation supports a claim
PSO convergence theory has been extensively studied~\cite{clerc2002particle, poli2007pso_overview}.
```

### Contrastive Citation

Introduce a reference to highlight what this paper does differently:

```latex
% GOOD: Citation sets up contrast
Unlike \citet{jiang2022nn_nr}, which relies on a single-output network,
our approach generates multiple solutions simultaneously.
```

### Grouped Thematic Citation

When citing multiple papers on the same topic, group them logically:

```latex
% GOOD: Thematic grouping with context
Several approaches have applied neural networks to inverse kinematics,
including MLP-based methods~\cite{bócsi2011learning, csiszar2017solving}
and normalizing flows~\cite{ames2022ikflow}.
```

### Anti-Patterns to Avoid

| Anti-Pattern | Description | Fix |
|-------------|-------------|-----|
| **Citation dumping** | `\cite{a,b,c,d,e}` at paragraph end with no context | Distribute citations to specific claims |
| **Orphan citations** | Citing a paper but never discussing its contribution | Add 1+ sentences explaining relevance |
| **Disconnected citations** | Citations in places unrelated to the cited work | Move to the correct claim |
| **Citation-as-evidence** | "This is true [1]" with no explanation of what [1] shows | Explain what the cited paper found |
| **Self-citation padding** | Excessive self-citations not relevant to the current work | Limit to genuinely relevant prior work |

---

## Part 5: Target Metrics

### By Paper Type

| Paper Type | Target Total References | Minimum Recent (last 3 years) | Min % Recent |
|-----------|------------------------|-------------------------------|-------------|
| Letter / Short Paper | 20-30 | 8-10 | 30% |
| Full Research Paper | 35-50 | 12-18 | 30% |
| Survey / Review | 80-150+ | 30+ | 30% |

### By Section (for a typical full paper)

| Section | Expected Citations |
|---------|-------------------|
| Introduction | 15-25 (broad coverage, many recent) |
| Related Work | 20-35 (comprehensive, organized by theme) |
| Methods | 5-15 (specific techniques cited) |
| Experiments | 5-10 (baselines, datasets, metrics) |
| Discussion | 5-10 (connections to other work) |
| Conclusion | 0-3 (only if referencing specific future directions) |

### Journal/Conference-Specific Considerations

When the target venue is known:
- Check the typical reference count by examining 3-5 recent papers from the venue
- Match the citation style (numbered vs. author-year, natbib vs. biblatex)
- Prefer citing papers published in the same venue (demonstrates relevance to the community)
- Check if the venue has specific reference formatting requirements

---

## Part 6: Citation APIs and Tools

### Semantic Scholar API

```python
import requests

def search_semantic_scholar(query: str, limit: int = 5) -> list:
    """Search for papers on Semantic Scholar."""
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,authors,year,venue,externalIds,abstract,citationCount"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    return []

def get_paper_by_id(paper_id: str) -> dict:
    """Get paper details by Semantic Scholar ID, DOI, or arXiv ID."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}"
    params = {"fields": "title,authors,year,venue,externalIds,abstract,references,citations"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {}
```

### CrossRef API

```python
def search_crossref(query: str, rows: int = 5) -> list:
    """Search for papers on CrossRef."""
    url = "https://api.crossref.org/works"
    params = {
        "query": query,
        "rows": rows,
        "sort": "relevance"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["message"]["items"]
    return []
```

### DOI-to-BibTeX

```python
def doi_to_bibtex(doi: str) -> str:
    """Convert DOI to BibTeX via content negotiation."""
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        return response.text
    raise ValueError(f"Could not fetch BibTeX for DOI: {doi}")

# Usage:
# bibtex = doi_to_bibtex("10.5555/3295222.3295349")
```

### arXiv API

```python
import urllib.parse

def search_arxiv(query: str, max_results: int = 5) -> str:
    """Search arXiv for papers."""
    base_url = "http://export.arxiv.org/api/query"
    encoded_query = urllib.parse.quote(query)
    url = f"{base_url}?search_query=all:{encoded_query}&max_results={max_results}&sortBy=relevance"
    response = requests.get(url)
    return response.text  # Returns Atom XML; parse with xml.etree.ElementTree
```

### OpenAlex API

```python
def search_openalex(query: str, per_page: int = 5) -> list:
    """Search OpenAlex for papers."""
    url = "https://api.openalex.org/works"
    params = {
        "search": query,
        "per_page": per_page,
        "sort": "relevance_score:desc"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
```

### Recommended Workflow

```
1. Search Semantic Scholar (fast, good for CS/ML papers)
      |
      v
2. If not found, try CrossRef (broader coverage)
      |
      v
3. If found, get DOI
      |
      v
4. DOI -> BibTeX via content negotiation
      |
      v
5. Validate BibTeX fields are complete
      |
      v
6. Verify paper supports the intended claim
      |
      v
7. Add to .bib file with consistent cite key
```
