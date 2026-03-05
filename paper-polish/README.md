# paper-polish-skill

A Claude Code Skill for automated academic LaTeX paper improvement before journal submission.

## Features

Six modular workflows that can be invoked individually or combined:

| Module | Function | Trigger Keywords |
|--------|----------|-----------------|
| Module 1 | De-AI text polishing | polish, de-AI, natural writing |
| Module 2 | Citation expansion | citations, references, bibliography |
| Module 3 | Figure/diagram quality check | figures, TikZ, diagrams |
| Module 4 | Table data cross-verification | tables, data, numbers |
| Module 5 | LaTeX compilation cleanup | compile, warnings, errors |
| Module 6 | Full quality review | review, full check, submission |

## Installation

### Option A: Claude Code Plugin Marketplace

```bash
/plugin marketplace add yutaoshao/agent-skills/paper-polish
```

### Option B: Manual installation

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/paper-polish ~/.claude/skills/
```

## Skill Structure

```
paper-polish/
├── SKILL.md              # Main skill definition (6 modules)
└── references/
    ├── de-ai-patterns.md  # 50+ AI writing antipatterns catalog
    ├── citation-guide.md  # Citation gap analysis & integration guide
    └── latex-checklist.md # 80+ item LaTeX quality checklist
```

## Reference Files

- **de-ai-patterns.md**: Comprehensive catalog of 8 categories of AI writing patterns with detection heuristics and replacement strategies. Covers bold-label openers, overused transitions, filler phrases, AI vocabulary, mechanical sentence structures, conclusion patterns, discussion patterns, and superlative claims.

- **citation-guide.md**: Methodology for analyzing citation gaps (temporal, methodological, foundational, claim support), sourcing high-quality references, BibTeX quality standards, and natural integration strategies with anti-patterns to avoid.

- **latex-checklist.md**: 80+ item quality checklist covering compilation, references, typography, figures, tables, equations, content quality, and pre-submission final checks.

## Usage

The skill auto-activates when Claude detects LaTeX paper improvement tasks. Example prompts:

- "Polish my paper to remove AI-flavored writing"
- "Expand citations to reach 40+ references"
- "Check my TikZ diagrams for errors"
- "Verify table data matches experimental results"
- "Run a full quality review before submission"
- "Help me prepare this paper for ISA Transactions submission"

## Related

For full lifecycle paper writing from project source code to submission, see [paper-writer](../paper-writer/).

## License

MIT
