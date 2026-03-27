# Agent Collaboration Rules

## Purpose
This workspace may be worked on by multiple agents such as Claude Code and CodeX.
All agents must use explicit context files instead of relying on session memory.

## Canonical Instruction File
- `CLAUDE.md` is the canonical source of workspace agent instructions.
- `AGENTS.md` mirrors `CLAUDE.md` and should not be edited manually.

## Before Starting Work
1. Identify the target project root.
2. Read that project's `CONTEXT.md` first if it exists.
3. Read workspace `CLAUDE.md` or `AGENTS.md`.
4. Do not assume any prior chat history is available.

## After Finishing Work
Update the target project's `CONTEXT.md` when any of the following changed:
- architecture decisions
- current implementation progress
- known issues
- important file ownership or responsibilities
- conventions relevant to future work

## Context Update Rules
- Keep entries concise and factual.
- Do not record speculation.
- Do not duplicate large code blocks.
- Prefer bullets over paragraphs.
- Update only sections impacted by the completed work.

## Required Sections in Project CONTEXT.md
- Project Overview
- Architecture Decisions
- Current Status
- Known Issues
- Conventions
- Important Files
- Open Questions

## Recommended Project CONTEXT.md Template
```md
# Project Context

## Project Overview
One sentence describing what this project does.

## Architecture Decisions
- Decision:
  - Background:
  - Conclusion:
  - Impact:

## Current Status
- In Progress:
- Completed:
- Next Steps:

## Known Issues
- Issue:
  - Symptom:
  - Cause:
  - Workaround:
  - Follow-up:

## Conventions
- Code:
- Directory:
- API:
- Testing:

## Important Files
- `path/to/file`: what it is responsible for

## Open Questions
- Pending decisions and unresolved questions
```

## Synchronization Workflow
- Treat `CONTEXT.md` as the source of truth for project state.
- Keep `CLAUDE.md` focused on stable workspace instructions.
- Regenerate `AGENTS.md` from `CLAUDE.md` via `sync-context/scripts/sync.sh` instead of editing it directly.
- Before commit, run the sync script or rely on the local `pre-commit` hook to validate required files.

## Handoff Principle
The next agent should be able to continue from `CONTEXT.md` without reading prior chat history.
