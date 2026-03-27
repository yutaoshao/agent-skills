---
name: sync-context
description: Use this skill when a repository needs reliable cross-agent handoff across Claude Code, Codex, or similar runtimes. It standardizes `CONTEXT.md` as the project state source of truth, keeps `AGENTS.md` mirrored from `CLAUDE.md`, and adds lightweight validation through a shared shell script and git hook.
---

# Sync Context

Make cross-agent collaboration explicit, deterministic, and low-maintenance.

This skill is for repositories where multiple AI runtimes may work on the same codebase and you want handoff state to survive runtime switches.

## Goals

1. Use `CONTEXT.md` as the single source of truth for project state.
2. Keep `CLAUDE.md` as the canonical agent-instruction file.
3. Regenerate `AGENTS.md` from `CLAUDE.md` instead of maintaining two divergent instruction files.
4. Enforce the workflow with a shared shell script and an optional git `pre-commit` hook.

## When to Use

Use this skill when the user asks for any of the following:

- cross-agent context synchronization
- Claude Code and Codex handoff workflow
- `CONTEXT.md` / `CLAUDE.md` / `AGENTS.md` setup
- project memory or handoff files
- git hook validation for agent collaboration

## Recommended File Roles

```text
CONTEXT.md   -> project state source of truth
CLAUDE.md    -> canonical agent instructions
AGENTS.md    -> generated mirror of CLAUDE.md
```

Keep project status, decisions, conventions, and handoff notes in `CONTEXT.md`.
Do not duplicate large amounts of project-state content into both `CLAUDE.md` and `AGENTS.md`.

## Procedure

### 1. Establish the files

At the target project root:

- create `CONTEXT.md` if missing
- create or normalize `CLAUDE.md`
- generate `AGENTS.md` from `CLAUDE.md`

`CONTEXT.md` should contain these sections:

- `Project Overview`
- `Architecture Decisions`
- `Current Status`
- `Known Issues`
- `Conventions`
- `Important Files`
- `Open Questions`

### 2. Install the shared script

Use `scripts/sync.sh` as the single entrypoint.

Supported commands:

- `sync.sh sync` : regenerate `AGENTS.md` from `CLAUDE.md`
- `sync.sh check`: validate required files and fail when they are missing or out of sync

Keep the script deterministic. Let agents update content; let the script only sync and validate.

### 3. Add a local git guard

Install a `pre-commit` hook that runs:

```bash
"$REPO_ROOT/sync-context/scripts/sync.sh" sync
git add "$REPO_ROOT/AGENTS.md"
"$REPO_ROOT/sync-context/scripts/sync.sh" check
```

This keeps the mirrored file fresh in the staged commit and blocks the commit if required files are missing or invalid.

### 4. Optional runtime hooks

If the local runtime supports task-completion hooks, wire those hooks to run the sync script or remind the agent to update `CONTEXT.md`.

Important: runtime hooks are helpful but not sufficient on their own. Keep the git hook as the last line of defense.

## Minimal Hook Example

Example idea for a runtime that supports task-completion hooks:

```json
{
  "hooks": {
    "TaskCompleted": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "zsh -lc 'script=\"$PWD/sync-context/scripts/sync.sh\"; if [[ -x \"$script\" ]]; then \"$script\" check; fi'"
          }
        ]
      }
    ]
  }
}
```

Adapt the exact hook syntax to the runtime. Do not assume every runtime uses the same settings format.

## Validation Rules

`check` should fail when any of the following is true:

- `CONTEXT.md` is missing
- `CLAUDE.md` is missing
- `AGENTS.md` is missing
- `CONTEXT.md` lacks any required section
- `AGENTS.md` does not exactly mirror `CLAUDE.md`

## Design Principles

- KISS: keep the workflow small and predictable
- DRY: maintain sync logic in one script only
- YAGNI: avoid building semantic summarizers into shell scripts
- Protect the call chain: never make downstream runtimes guess the latest project state from chat history

## Deliverables

A complete minimal setup should include:

- `CONTEXT.md`
- `CLAUDE.md`
- `AGENTS.md`
- `sync-context/SKILL.md`
- `sync-context/scripts/sync.sh`
- `.git/hooks/pre-commit`
