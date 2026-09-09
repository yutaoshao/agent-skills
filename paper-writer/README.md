# Paper Writer

`paper-writer` supports English CS, ML, and AI research papers from research artifacts through LaTeX submission and revision. It keeps the paper's claims, methods, results, citations, figures, tables, and rendered output aligned.

It supports targeted work as well as full manuscripts: extracting an argument from a repository, drafting sections, checking numerical tables, verifying citations, compiling LaTeX, preparing a venue-specific submission, and answering reviewers. It does not require a fixed multi-stage workflow or create project planning files.

For Chinese engineering-paper drafting and rewriting, use [chinese-engineering-paper-writing](../chinese-engineering-paper-writing/).

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

## Structure

```text
paper-writer/
├── SKILL.md
├── modules/
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
└── references/
    ├── citation-guide.md
    ├── evidence-review.md
    ├── latex-checklist.md
    └── writing-philosophy.md
```

## Examples

```text
"Draft an English introduction from these experiment notes."
"Trace every number in the results table to its source CSV."
"Verify the BibTeX entries and citations in this LaTeX project."
"Prepare a point-by-point response to these reviewer comments."
```

## License

MIT
