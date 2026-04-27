# Agent Skills

[English](./README.md) | [中文](./README_CN.md)

A repository for storing and managing AI Agent skill modules.

## Overview

This is a modular AI skill collection that provides standardized capability access for intelligent agents. Each skill module contains detailed usage guides, code examples, and best practices, spanning model capabilities, academic workflows, reading and learning methods, developer onboarding, and repo workflow utilities.

## Project Structure

```
agent-skills/
├── glm-skills/              # GLM (Zhipu AI) Skills Library
│   ├── ASR/                 # Speech Recognition
│   ├── TTS/                 # Text to Speech
│   ├── LLM/                 # Large Language Model
│   ├── VLM/                 # Vision Language Model
│   ├── image-generation/    # Image Generation
│   ├── video-generation/    # Video Generation
│   ├── web-search/          # Web Search
│   ├── web-reader/          # Web Content Extraction
│   ├── canvas-design/       # Canvas Design
│   ├── frontend-design/     # Frontend Design System
│   └── document-skills/     # Document Processing (docx/xlsx/pptx/pdf)
├── paper-writer/            # Academic Paper Writing (Full Lifecycle)
│   ├── SKILL.md             # 10-stage workflow (code to submission)
│   ├── modules/             # 10 stage modules
│   ├── references/          # Writing philosophy, checklists & guides
│   ├── plan-template/       # Cross-session context management
│   └── scripts/             # Init and style check scripts
├── paper-polish/            # Academic Paper Polish (LaTeX)
│   ├── SKILL.md             # 6 modular workflows
│   └── references/          # Pattern catalogs & checklists
├── project-analyzer/        # Codebase Analysis & Onboarding
│   ├── SKILL.md             # 8 modular workflows
│   └── references/          # Checklists, pattern catalog & report template
├── sync-context/            # Cross-Agent Context Sync & Handoff
│   ├── SKILL.md             # Session protocol & validation
│   └── scripts/             # Init, check & inject scripts
├── git-commit/              # Git Staging & Detailed Commit Drafting
│   ├── SKILL.md             # Commit workflow and staging rules
│   ├── references/          # Commit type, scope, and body guidelines
│   └── scripts/             # Working tree summary helper
├── how-to-read-a-book/       # Active Reading & Book Analysis
│   └── SKILL.md             # Inspectional, analytical, and syntopical reading workflows
└── [other-skills]/          # Extension Point
```

## Skill Libraries

| Library | Description | SDK | Modules |
|---------|-------------|-----|---------|
| [glm-skills](./glm-skills/) | GLM AI capabilities collection | z-ai-web-dev-sdk | 12 |
| [paper-writer](./paper-writer/) | Full lifecycle academic paper writing (code to submission) | - | 10 |
| [paper-polish](./paper-polish/) | Academic LaTeX paper improvement workflows | - | 6 |
| [project-analyzer](./project-analyzer/) | Codebase analysis & developer onboarding | - | 8 |
| [sync-context](./sync-context/) | Cross-agent context sync & handoff protocol | - | 3 |
| [git-commit](./git-commit/) | Git staging and detailed conventional commit workflow | - | 6 |
| [how-to-read-a-book](./how-to-read-a-book/) | Active reading workflows for books, papers, and long-form texts | - | 4 |

## Skill Categories

### Speech & Conversation
- **ASR**: Speech recognition, supports multiple audio formats
- **TTS**: Speech synthesis, multiple voice options
- **LLM**: Large language model chat

### Vision & Multimodal
- **VLM**: Image understanding and analysis
- **image-generation**: AI image generation
- **video-generation**: AI video generation

### Web Capabilities
- **web-search**: Web search
- **web-reader**: Web content parsing

### Document Processing
- **docx**: Word document operations
- **xlsx**: Excel spreadsheet processing
- **pptx**: PowerPoint presentations
- **pdf**: PDF document processing

### Design System
- **canvas-design**: Visual art creation
- **frontend-design**: Frontend UI design standards

### Academic Writing
- **paper-writer**: Full lifecycle academic paper writing from project source code to submission-ready LaTeX (10 stages: code analysis, literature review, structure, drafting, figures, citations, de-AI polish, LaTeX compilation, submission review, revision)
- **paper-polish**: Automated LaTeX paper improvement (de-AI polishing, citation expansion, figure/table verification, compilation cleanup, full quality review)

### Reading & Learning
- **how-to-read-a-book**: Active reading workflows inspired by *How to Read a Book* / 《如何阅读一本书》 (inspectional reading, analytical reading, syntopical comparison, genre-specific reading artifacts)

### Developer Tools
- **project-analyzer**: Systematic codebase analysis for project takeover and onboarding (tech stack, structure, architecture, dependencies, code quality, dev workflow, risk assessment, comprehensive report)
- **sync-context**: Cross-agent context synchronization via `CONTEXT.md` handoff protocol (session init/end protocol, structure validation, freshness checks, progressive disclosure via `context/` subdirectory)
- **git-commit**: Intentional staging and detailed commit drafting for real repository diffs (scope detection, staged/unstaged inspection, conventional commit formatting, post-commit verification)

## Quick Start

### Install via Claude Code Plugin Marketplace

Install the entire repository (all skills):

```bash
/plugin marketplace add yutaoshao/agent-skills
```

Or install individual skills:

```bash
# GLM AI Skills (ASR, TTS, LLM, VLM, image/video generation, web, design, docs)
/plugin marketplace add yutaoshao/agent-skills/glm-skills

# Academic Paper Writer (Full Lifecycle)
/plugin marketplace add yutaoshao/agent-skills/paper-writer

# Academic Paper Polish
/plugin marketplace add yutaoshao/agent-skills/paper-polish

# Project Analyzer
/plugin marketplace add yutaoshao/agent-skills/project-analyzer

# Cross-Agent Context Sync
/plugin marketplace add yutaoshao/agent-skills/sync-context

# Git staging and commit drafting
/plugin marketplace add yutaoshao/agent-skills/git-commit

# Active reading and book analysis
/plugin marketplace add yutaoshao/agent-skills/how-to-read-a-book
```

### Manual Installation

Clone the repository and copy the desired skill to your Claude skills directory:

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/paper-polish ~/.claude/skills/
cp -r agent-skills/project-analyzer ~/.claude/skills/
cp -r agent-skills/git-commit ~/.claude/skills/
cp -r agent-skills/how-to-read-a-book ~/.claude/skills/
```

Each skill module's `SKILL.md` contains complete usage guides and code examples.

## Contributing

When adding new skill modules, follow this structure:

```
skill-name/
├── SKILL.md         # Core documentation (required)
├── LICENSE.txt      # License (required)
├── scripts/         # Example code (recommended)
└── README.md        # Quick start (optional)
```

If a new top-level skill changes repository discovery or installation paths, update `README.md` and `README_CN.md` in the same change.

## License

Each skill module is licensed independently. See `LICENSE.txt` in each module directory.
