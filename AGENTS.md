# Agent Rules

## Context

- Run `bash sync-context/scripts/sync.sh inject` before deep work that changes repository-level skills, docs, or workflow conventions.
- Update `CONTEXT.md` and run `bash sync-context/scripts/sync.sh check` before finishing work that changes repo-level behavior or expectations.

## Skill Changes

- Treat each skill directory's `SKILL.md` as the canonical operational guide.
- Treat `README.md` and `README_CN.md` as repository discovery docs for humans.
- When adding, removing, renaming, or materially changing a top-level skill, update `README.md` and `README_CN.md` in the same change when the user-facing overview, install commands, project structure, or capability summaries become stale.
- Update README files selectively rather than mechanically. Typical sections to review are `Project Structure`, `Skill Libraries`, category summaries, and installation examples.
- Skip README edits only when the change is purely internal and does not affect discoverability or user-facing capability descriptions.

## Safety

- Do not bundle unrelated local changes into the same commit.
- Leave incidental local metadata such as `.DS_Store` or `.claude/` untouched unless the user explicitly asks to include them.
