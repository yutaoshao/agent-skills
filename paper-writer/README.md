# Paper Writer

From project source code to submission-ready LaTeX paper. A 10-stage lifecycle skill for CS/ML/AI researchers, covering code analysis, literature review, paper structure, section drafting, figure/table generation, citation management, de-AI polishing, LaTeX compilation, submission preparation, and revision handling.

## Features

| Stage | Module | Description |
|-------|--------|-------------|
| S1 | Project Analysis | Extract contributions and results from source code |
| S2 | Literature Review | Search, organize, and synthesize related work |
| S3 | Paper Structure | Define contribution, apply Narrative Principle, generate outline |
| S4 | Writing Core | Section-by-section drafting with writing philosophy |
| S5 | Figures & Tables | Publication-quality figures (450 DPI) and data verification |
| S6 | Citation Management | Anti-hallucination citation workflow with API verification |
| S7 | Polish | De-AI text polishing (English + Chinese patterns) |
| S8 | LaTeX Compilation | Template setup, compilation, 80+ item checklist |
| S9 | Review & Submission | Conference checklists, self-review, submission package |
| S10 | Revision & Resubmission | Reviewer response, rebuttal, camera-ready |

## Conference Support

Templates guide included for: **NeurIPS**, **ICML**, **ICLR**, **ACL**, **AAAI**, **COLM**.

Custom templates also supported -- provide your `.tex` template and the skill adapts.

## Installation

### Claude Code Plugin Marketplace

```bash
/plugin marketplace add yutaoshao/agent-skills/paper-writer
```

### Manual

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/paper-writer ~/.claude/skills/paper-writer
```

## Skill Structure

```
paper-writer/
├── SKILL.md                     # Core skill definition
├── LICENSE.txt                  # MIT License
├── README.md                    # This file
├── modules/                     # 10 stage modules (loaded on demand)
│   ├── m01-project-analysis.md
│   ├── m02-literature-review.md
│   ├── m03-paper-structure.md
│   ├── m04-writing-core.md
│   ├── m05-figures-tables.md
│   ├── m06-citation-management.md
│   ├── m07-polish.md
│   ├── m08-latex-compilation.md
│   ├── m09-review-submission.md
│   └── m10-revision-resubmission.md
├── references/                  # Deep-dive reference documents
│   ├── de-ai-patterns.md
│   ├── citation-guide.md
│   ├── latex-checklist.md
│   ├── writing-philosophy.md
│   ├── conference-checklists.md
│   ├── reviewer-guidelines.md
│   ├── prompts-collection.md
│   ├── color-palettes.md
│   └── templates-guide.md
├── plan-template/               # Cross-session context management
│   ├── project-overview.md
│   ├── stage-gates.md
│   ├── progress.md
│   ├── outline.md
│   └── notes.md
└── scripts/
    ├── init_plan.sh / .ps1      # Initialize plan/ directory
    └── style_check.sh / .ps1   # De-AI style checker
```

## Usage Examples

```
# Full paper from a research project
"Write a paper based on my project code in ./src"

# Single stage
"Analyze my repository and identify the main contributions"
"Write the introduction section"
"Polish my paper to remove AI writing patterns"
"Check if my paper is ready for NeurIPS submission"

# Citation management
"Verify all citations in my paper"
"Expand the bibliography to meet journal requirements"

# Revision
"Help me respond to reviewer comments"
```

## Related

For post-writing polishing only (without the full lifecycle), see [paper-polish](../paper-polish/).

## License

MIT
