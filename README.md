# Agent Skills

[English](./README.md) | [中文](./README_CN.md)

Central catalog for the skills stored in this repository. The root README files are the only overview docs; individual skill directories intentionally keep `SKILL.md` as the authoritative source and do not need their own `README.md`.

## Repository Layout

```text
agent-skills/
├── README.md
├── README_CN.md
├── glm-skills/
│   ├── ASR/
│   ├── TTS/
│   ├── LLM/
│   ├── VLM/
│   ├── image-generation/
│   ├── video-generation/
│   ├── web-search/
│   ├── web-reader/
│   ├── canvas-design/
│   ├── frontend-design/
│   └── document-skills/
│       ├── docx/
│       ├── xlsx/
│       ├── pptx/
│       └── pdf/
├── paper-writer/
├── paper-polish/
└── project-analyzer/
```

## Conventions

- Every installable skill must include a `SKILL.md`.
- Use `SKILL.md` as the canonical instructions for triggers, workflow, references, and scripts.
- Put cross-skill discovery, installation notes, and maintenance conventions in this root README pair.
- Optional folders such as `references/`, `scripts/`, `assets/`, `modules/`, or `plan-template/` should be documented from `SKILL.md` when they matter to execution.

## Skill Index

### Research and Developer Skills

| Skill | Focus |
|------|-------|
| `paper-writer` | Full paper-writing lifecycle for CS/ML/AI projects, from repo analysis to submission and rebuttal |
| `paper-polish` | LaTeX paper improvement, de-AI polishing, citation expansion, figure/table review, and submission checks |
| `project-analyzer` | Codebase onboarding, architecture review, dependency analysis, risk discovery, and project reporting |
| `sync-context` | Cross-agent handoff workflow using `CONTEXT.md`, mirrored instructions, and git/hook validation |

### GLM Skills

| Skill | Focus |
|------|-------|
| `ASR` | Speech-to-text workflows with `z-ai-web-dev-sdk` |
| `TTS` | Text-to-speech generation with multiple voices and controls |
| `LLM` | Chat completions and conversational AI workflows |
| `VLM` | Image understanding and multimodal chat |
| `image-generation` | Text-to-image generation |
| `video-generation` | Async video generation from text or image inputs |
| `web-search` | Web search and retrieval |
| `web-reader` | Web page content extraction |
| `canvas-design` | Static visual design and poster-style creative output |
| `frontend-design` | Design-token-driven frontend implementation and UI quality guidance |
| `docx` | Word document creation, editing, and review |
| `xlsx` | Spreadsheet creation, analysis, and formula-safe editing |
| `pptx` | Presentation creation and editing |
| `pdf` | PDF extraction, generation, form filling, and document manipulation |

## Installation

### Claude Code

For a personal install, copy any skill directory into `~/.claude/skills/<skill-name>`:

```bash
cp -R /path/to/agent-skills/paper-writer ~/.claude/skills/paper-writer
```

For a project-scoped install, copy the skill into `.claude/skills/<skill-name>` inside the target repository.

After installation, restart Claude Code or reload skills so the new skill is picked up.

### Codex

Copy any skill directory into `~/.codex/skills/<skill-name>`:

```bash
cp -R /path/to/agent-skills/paper-writer ~/.codex/skills/paper-writer
```

After installation, restart Codex so the new skill is picked up.

### Other Agent Runtimes

If you use another agent runtime, copy the target skill folder into that runtime's skills directory. The transferable unit is the skill folder itself, centered on `SKILL.md`.

## Maintenance

When adding or updating a skill:

1. Add or update `SKILL.md`.
2. Keep detailed operational guidance inside `SKILL.md` and referenced files.
3. Update this root README pair if the skill list, installation guidance, or repository conventions change.
4. Avoid adding per-skill `README.md` files unless a platform strictly requires them.
5. For cross-agent collaboration in this repository, use `sync-context/` together with `CONTEXT.md`, `CLAUDE.md`, and the generated `AGENTS.md`.

## License

Each skill directory carries its own license information. Check the local `LICENSE.txt` when present.
