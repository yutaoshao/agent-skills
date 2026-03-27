# project-analyzer

A skill for systematically analyzing unfamiliar codebases when taking over or onboarding to a new project.

## Features

Eight modular workflows that can be invoked individually or combined:

| Module | Function | Trigger Keywords |
|--------|----------|-----------------|
| Module 1 | Technology stack identification | tech stack, frameworks, technologies |
| Module 2 | Project structure & entry points | structure, layout, entry points |
| Module 3 | Architecture & design patterns | architecture, patterns, data flow |
| Module 4 | Dependency analysis | dependencies, packages, libraries |
| Module 5 | Code quality assessment | quality, testing, linting, standards |
| Module 6 | Development workflow & standards | CI/CD, deployment, dev process |
| Module 7 | Risk & technical debt | risks, tech debt, security, TODOs |
| Module 8 | Comprehensive report | full analysis, overview, onboarding |

## Installation

### Option A: Claude Code Plugin Marketplace

```bash
/plugin marketplace add yutaoshao/agent-skills/project-analyzer
```

### Option B: Manual installation

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/project-analyzer ~/.claude/skills/
```

## Skill Structure

```
project-analyzer/
├── SKILL.md                            # Main skill definition (8 modules)
└── references/
    ├── analysis-checklist.md           # 100+ item quality checklist
    ├── architecture-patterns.md        # Architecture & design pattern catalog
    └── report-template.md             # Comprehensive report template
```

## Reference Files

- **analysis-checklist.md**: 100+ item checklist covering repository basics, technology stack, project structure, dependencies, code quality, testing, documentation, CI/CD, git workflow, security, error handling, performance, and observability.

- **architecture-patterns.md**: Catalog of architectural styles (monolith, modular monolith, microservices, serverless, monorepo) and design patterns (MVC, Clean Architecture, CQRS, repository, DI, middleware, strategy) with file structure signatures and code-level identification heuristics.

- **report-template.md**: Markdown template for the comprehensive analysis report including executive summary, tech stack table, project map, architecture overview, dependency health, quality snapshot, developer onboarding quick start, risk register, and prioritized recommended first steps.

## Usage

The skill activates when Claude detects project analysis or onboarding tasks. Example prompts:

- "Analyze this project for me"
- "Help me understand this codebase"
- "I just took over this project, give me an overview"
- "What tech stack does this project use?"
- "What are the main risks in this codebase?"
- "Generate a full project report"
- "Where are the entry points in this project?"
- "How is this project structured?"

## License

MIT
