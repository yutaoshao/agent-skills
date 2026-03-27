---
name: sync-context
description: Use this skill to maintain a persistent project context file (CONTEXT.md) that survives AI model switches. It defines a handoff protocol, validates context freshness, and supports progressive disclosure via a context/ subdirectory for large projects.
---

# Sync Context

Maintain an external project memory so switching between AI models never loses development progress.

## Goals

1. Use `CONTEXT.md` as the **single source of truth** for project state and handoff.
2. Define a clear **session protocol**: what to read on start, what to write on end.
3. Validate context **structure and freshness** via a shared shell script.
4. Support **progressive disclosure**: keep `CONTEXT.md` lean; offload detailed reference docs to `context/`.

## When to Use

- Switching between AI coding assistants (Claude Code, Codex, Gemini, etc.)
- Cross-agent context synchronization or handoff
- Setting up `CONTEXT.md` project memory
- Any request involving project state persistence across sessions

## CONTEXT.md Structure

`CONTEXT.md` must contain these sections, designed for efficient handoff:

### Handoff sections (update every session)

These sections describe the **current state** and must always live in `CONTEXT.md`. Keep each section under 15 lines.

- `## In Progress` — what is currently being worked on, with enough detail for a new agent to continue
- `## Recent Changes` — what changed in the last 1–2 sessions (files modified, decisions made)
- `## Next Steps` — prioritized list of what to do next
- `## Blockers & Open Questions` — anything unresolved that the next agent should know

### Reference sections (update when needed)

These sections provide background knowledge. They can live **inline** (for small projects) or be **offloaded to `context/`** (for large projects).

- `## Project Overview` — one-paragraph project description
- `## Architecture` — high-level structure, key patterns, tech stack
- `## Conventions` — coding style, naming, commit conventions
- `## Key Files` — paths to the most important files for current work

### Metadata

The first line of `CONTEXT.md` after the title should be:

```markdown
> Last Updated: YYYY-MM-DD HH:MM (timezone)
```

This is updated automatically by `sync.sh` or manually by the agent.

## Progressive Disclosure: `context/` Subdirectory

When `CONTEXT.md` grows beyond ~200 lines, move detailed reference content into a `context/` directory at the project root:

```text
CONTEXT.md                ← lean: handoff sections + one-line summaries for references
context/
  architecture.md         ← detailed architecture documentation
  conventions.md          ← detailed coding conventions
  key-files.md            ← full file index with descriptions
```

In `CONTEXT.md`, replace verbose reference sections with a **one-line summary + link**:

```markdown
## Architecture

Next.js + Prisma + PostgreSQL monorepo (apps/ and packages/).
→ Details: [context/architecture.md](context/architecture.md)
```

**Rules:**
- Handoff sections (In Progress, Recent Changes, Next Steps, Blockers) **never** go into `context/` — they must always be in the main file.
- The AI should read detail files from `context/` only when it needs deeper understanding for its current task.
- `sync.sh check` will warn when `CONTEXT.md` exceeds 200 lines and suggest using `context/`.
- `sync.sh inject` will list available detail files from `context/` so the AI knows what's available without loading it all.

## Session Protocol

### On Session Start (new model comes in)

1. Read `CONTEXT.md` thoroughly
2. Review files listed in `## Key Files`
3. Check `## In Progress` and `## Blockers & Open Questions` before starting work
4. If `context/` exists, note the available detail files — read them only when needed

### On Session End (before switching away)

1. Update `## In Progress` with current state
2. Update `## Recent Changes` with what was done this session
3. Update `## Next Steps` if priorities changed
4. Update `## Blockers & Open Questions` if applicable
5. If reference knowledge changed significantly, update the relevant `context/*.md` file
6. Run `sync.sh check` to validate

## Agent Instructions (Add to your AI's custom instructions)

To enforce this protocol, copy and paste the following into your AI's global `.cursorrules`, `cline_instructions.md`, or Custom Instructions box:

```markdown
# Critical Project Context Protocol

1. ALWAYS begin every session by running `bash sync-context/scripts/sync.sh inject` and thoroughly internalizing the output. Do not start coding before reading this.
2. If `CONTEXT.md` does not exist, run `bash sync-context/scripts/sync.sh init` to create it.
3. NEVER finish a session or switch tasks without updating `CONTEXT.md`.
4. Before you finish, you MUST run `bash sync-context/scripts/sync.sh check` and fix any errors it reports.
5. If inject output lists files in `context/`, read the relevant ones BEFORE doing deep work on those areas.
```

## Procedure

### 1. Initialize (first time)

Run `sync.sh init` at the project root to generate a template `CONTEXT.md`.

### 2. Validate

Run `sync.sh check` to verify:
- `CONTEXT.md` exists and has all required sections
- Content is not stale (warns if last update > 24 hours)
- File is not too large (warns if > 200 lines, suggests using `context/`)

### 3. Inject Context

Run `sync.sh inject` at the start of a session to output the context in an AI-optimized format. If a `context/` directory exists, inject will also list the available detail files.

### 4. Git guard (optional)

Install a `pre-commit` hook:

```bash
SCRIPT="$(git rev-parse --show-toplevel)/sync-context/scripts/sync.sh"
if [[ -x "$SCRIPT" ]]; then
  "$SCRIPT" check
fi
```

This blocks commits when `CONTEXT.md` is missing or invalid.

## Validation Rules

`check` fails when:
- `CONTEXT.md` is missing
- Any required section heading is missing

`check` warns when:
- `Last Updated` timestamp is older than 24 hours
- `CONTEXT.md` exceeds 200 lines

## Design Principles

- **Context-first**: `CONTEXT.md` is the only required file
- **Protocol over tooling**: the handoff protocol matters more than the script
- **Keep it fresh**: stale context is worse than no context
- **Keep it lean**: large context wastes the AI's context window — offload to `context/`
- **Model-agnostic**: nothing in `CONTEXT.md` should be specific to any AI runtime

## Deliverables

- `CONTEXT.md`
- `sync-context/scripts/sync.sh`
- `context/` (optional, for large projects)
