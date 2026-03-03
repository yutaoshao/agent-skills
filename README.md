# Agent Skills

[English](./README.md) | [中文](./README_CN.md)

A repository for storing and managing AI Agent skill modules.

## Overview

This is a modular AI skill collection that provides standardized capability access for intelligent agents. Each skill module contains detailed usage guides, code examples, and best practices.

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
├── paper-polish/            # Academic Paper Polish (LaTeX)
│   ├── SKILL.md             # 6 modular workflows
│   └── references/          # Pattern catalogs & checklists
├── project-analyzer/        # Codebase Analysis & Onboarding
│   ├── SKILL.md             # 8 modular workflows
│   └── references/          # Checklists, pattern catalog & report template
└── [other-skills]/          # Extension Point
```

## Skill Libraries

| Library | Description | SDK | Modules |
|---------|-------------|-----|---------|
| [glm-skills](./glm-skills/) | GLM AI capabilities collection | z-ai-web-dev-sdk | 12 |
| [paper-polish](./paper-polish/) | Academic LaTeX paper improvement workflows | - | 6 |
| [project-analyzer](./project-analyzer/) | Codebase analysis & developer onboarding | - | 8 |

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
- **paper-polish**: Automated LaTeX paper improvement (de-AI polishing, citation expansion, figure/table verification, compilation cleanup, full quality review)

### Developer Tools
- **project-analyzer**: Systematic codebase analysis for project takeover and onboarding (tech stack, structure, architecture, dependencies, code quality, dev workflow, risk assessment, comprehensive report)

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

# Academic Paper Polish
/plugin marketplace add yutaoshao/agent-skills/paper-polish

# Project Analyzer
/plugin marketplace add yutaoshao/agent-skills/project-analyzer
```

### Manual Installation

Clone the repository and copy the desired skill to your Claude skills directory:

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/paper-polish ~/.claude/skills/
cp -r agent-skills/project-analyzer ~/.claude/skills/
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

## License

Each skill module is licensed independently. See `LICENSE.txt` in each module directory.
