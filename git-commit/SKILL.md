---
name: git-commit
description: Stage cohesive repository changes and create detailed Git commits grounded in the real diff. Use when Codex needs to inspect current git modifications, decide what to stage, write a conventional-commit style subject, and run non-interactive `git add` plus `git commit` with a precise multi-bullet body. Trigger on requests like "commit my changes", "write a detailed commit message", "stage and commit this work", or "make a conventional commit for the current diff".
---

# Git Commit

Stage the right files and create a commit message that explains the real work without inventing behavior, validation, or scope.

## Quick Start

1. Run `git rev-parse --show-toplevel` to confirm the target repository root.
2. Run `python3 /absolute/path/to/git-commit/scripts/collect_commit_context.py`.
3. Inspect the full diff for files that drive behavior, APIs, migrations, tests, or CI.
4. Read [`references/commit-guidelines.md`](references/commit-guidelines.md) before finalizing the message.
5. Stage the intended files, commit non-interactively, and verify the result with `git show --stat --oneline HEAD -1`.

## Workflow

### 1. Determine Commit Scope

- Treat already staged files as the current commit scope unless the user explicitly asks to restage.
- If nothing is staged, stage only the files that belong to the requested change.
- Pause and ask the user before committing when the working tree mixes clearly unrelated changes.
- Leave unrelated user edits untouched; never clean the working tree or unstage files you did not touch.
- Surface the real git error when there is nothing to commit; do not fabricate a fallback success path.

### 2. Inspect Changes Deeply Enough

- Use `scripts/collect_commit_context.py` for the high-level inventory of staged, unstaged, and untracked files.
- Inspect full diffs for files that change runtime behavior, public APIs, migrations, tests, release metadata, or CI.
- Prefer `git diff --cached -- <file>` when files are already staged.
- Use `git diff -- <file>` for unstaged files that may need to be added.
- Check renames, deletions, and generated files explicitly before staging them.
- Confirm whether tests were only modified or also executed; never claim a test run that did not happen.

### 3. Choose Staging Strategy

- Prefer explicit path-based `git add <path>...` over `git add -A`.
- Use `git add -A` only when the user explicitly wants every current change and the diff is cohesive.
- Do not stage editor junk, secrets, local env files, or incidental OS files unless the user clearly intends to commit them.
- Preserve partial staging boundaries unless the user asks to restage the whole file.
- If the repo has staged files plus additional unstaged work, commit the staged set by default and mention the remaining local changes afterward.

### 4. Write the Commit Message

- Read [`references/commit-guidelines.md`](references/commit-guidelines.md) before choosing the final subject and body.
- Use a conventional commit subject when the change type is inferable.
- Keep the subject specific, imperative, and under roughly 72 characters when practical.
- Add a blank line followed by 2 to 6 bullets describing the most important technical changes.
- Mention tests only when they were actually added, updated, or run.
- Add migration or compatibility notes when the diff changes interfaces, contracts, or behavior in a breaking way.

### 5. Commit Non-Interactively

Use repeated `-m` flags so the commit can be reproduced from the terminal without opening an editor.

```bash
git commit \
  -m "feat(scope): concise summary" \
  -m "- First concrete change
- Second concrete change
- Tests or validation that actually happened"
```

If the body needs a `BREAKING CHANGE:` paragraph, add one more `-m` block for it.

### 6. Verify

- Run `git show --stat --oneline HEAD -1` after committing.
- Report the commit hash and subject back to the user.
- Mention any remaining unstaged or untracked files that were intentionally left out.
- If `git commit` fails, surface the real error and do not invent a fallback success path.

## Decision Rules

- Choose `feat` for new user-visible capability or new workflow support.
- Choose `fix` for bug corrections or regression repairs.
- Choose `refactor` for internal restructuring without intended behavior change.
- Choose `docs`, `test`, `ci`, `build`, `perf`, `style`, `chore`, or `revert` when those are the dominant change types.
- Use a scope only when one subsystem, package, feature, or directory clearly dominates the diff.
- Omit the scope when the change spans several areas equally.
- Prefer one well-scoped commit over one omnibus commit when the diff mixes unrelated work.

## Output Expectations

Produce a commit that matches the actual diff and tell the user:

- what was staged,
- the final commit subject,
- the main bullet-point body themes,
- the resulting commit hash,
- and any remaining local changes not included in the commit.

## Example Requests

- `Commit my current changes with a detailed message.`
- `Stage the files for this auth fix and create a conventional commit.`
- `Write a thorough git commit for the staged diff only.`
- `Inspect the repo changes and make one cohesive commit if appropriate.`
