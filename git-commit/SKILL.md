---
name: git-commit
description: Stage cohesive repository changes, create detailed Git commits, and automatically merge safe local feature-branch commits back to main/master. Use when inspecting current git modifications, deciding what to stage, writing a conventional-commit style subject, running non-interactive `git add` plus `git commit`, or finishing a local feature branch. Trigger on requests like "commit my changes", "stage and commit this work", "make a conventional commit", "commit and merge back", or "finish this branch locally".
---

# Git Commit

Stage the right files, create a commit message grounded in the real diff, and automatically merge the committed feature branch back into the local base branch when it is safe.

## Quick Start

1. Run `git rev-parse --show-toplevel` to confirm the target repository root.
2. Run `python3 /absolute/path/to/git-commit/scripts/collect_commit_context.py`.
3. Inspect the full diff for files that drive behavior, APIs, migrations, tests, or CI.
4. Review commit boundaries and split obvious independent units before staging.
5. Read [`references/commit-guidelines.md`](references/commit-guidelines.md) before finalizing each message.
6. Stage and commit each intended unit non-interactively, then verify the result.
7. Unless the user explicitly asked for commit-only/no-merge, run the automatic local merge-back workflow after the final intended commit.

## Workflow

### 1. Determine Commit Scope

- Treat already staged files as the current commit scope unless the user explicitly asks to restage.
- If nothing is staged, stage only the files that belong to the requested change.
- Pause and ask the user before committing when the working tree mixes changes whose boundaries are unclear.
- Leave unrelated user edits untouched; never clean the working tree or unstage files you did not touch.
- Surface the real git error when there is nothing to commit; do not fabricate a fallback success path.

### 2. Review Commit Boundaries

- Before staging, classify the diff into independently reviewable and revertible units.
- Split into multiple commits by default when the diff contains different change types, unrelated subsystems, opportunistic fixes, or tests that clearly belong to different production changes.
- Keep docs and tests with the production change they describe or verify.
- Keep one commit only when the staged or unstaged diff represents a single coherent behavior change.
- Do not ask before splitting when boundaries are obvious and the user asked generally to commit changes.
- Ask only when splitting would be ambiguous, require risky partial-hunk staging, or conflict with already staged user intent.

### 3. Inspect Changes Deeply Enough

- Use `scripts/collect_commit_context.py` for the high-level inventory of staged, unstaged, and untracked files.
- Inspect full diffs for files that change runtime behavior, public APIs, migrations, tests, release metadata, or CI.
- Prefer `git diff --cached -- <file>` when files are already staged.
- Use `git diff -- <file>` for unstaged files that may need to be added.
- Check renames, deletions, and generated files explicitly before staging them.
- Confirm whether tests were only modified or also executed; never claim a test run that did not happen.

### 4. Choose Staging Strategy

- Prefer explicit path-based `git add <path>...` over `git add -A`.
- Use `git add -A` only when the user explicitly wants every current change and the diff is cohesive.
- Do not stage editor junk, secrets, local env files, or incidental OS files unless the user clearly intends to commit them.
- Preserve partial staging boundaries unless the user asks to restage the whole file.
- If the repo has staged files plus additional unstaged work, commit the staged set by default and mention the remaining local changes afterward.
- When splitting commits, stage one boundary at a time, commit it, then stage the next boundary.

### 5. Write the Commit Message

- Read [`references/commit-guidelines.md`](references/commit-guidelines.md) before choosing the final subject and body.
- Use a conventional commit subject when the change type is inferable.
- Keep the subject specific, imperative, and under roughly 72 characters when practical.
- Add a blank line followed by 2 to 6 bullets describing the most important technical changes.
- Mention tests only when they were actually added, updated, or run.
- Add migration or compatibility notes when the diff changes interfaces, contracts, or behavior in a breaking way.

### 6. Commit Non-Interactively

Use repeated `-m` flags so the commit can be reproduced from the terminal without opening an editor.

```bash
git commit \
  -m "feat(scope): concise summary" \
  -m "- First concrete change
- Second concrete change
- Tests or validation that actually happened"
```

If the body needs a `BREAKING CHANGE:` paragraph, add one more `-m` block for it.

### 7. Verify

- Run `git show --stat --oneline HEAD -1` after each commit.
- If you create multiple commits, verify the final range with `git log --oneline` or `git show --stat --oneline HEAD -N`.
- Report each commit hash and subject back to the user.
- Mention any remaining unstaged or untracked files that were intentionally left out.
- If `git commit` fails, surface the real error and do not invent a fallback success path.

### 8. Automatic Local Merge-Back Workflow

Run this section after the final intended commit unless the user explicitly asks for commit-only/no-merge. This workflow merges only when the current branch looks like a local feature branch and the working tree is clean after all selected commits.

1. Record the feature branch and detect the base branch:
   ```bash
   FEATURE_BRANCH=$(git branch --show-current)
   BASE_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's#^refs/remotes/origin/##')
   if [ -z "$BASE_BRANCH" ]; then
     git show-ref --verify --quiet refs/heads/main && BASE_BRANCH=main || BASE_BRANCH=master
   fi
   ```
2. If `FEATURE_BRANCH` is empty because HEAD is detached, do not merge; report the commit and the detached HEAD state.
3. If already on `main`, `master`, or the detected `BASE_BRANCH`, do not merge; report the commit on the current branch.
4. If any staged, unstaged, or untracked changes remain after the commit, do not switch branches. Report the commit and ask the user to clean, stash, or explicitly include those changes.
5. Run the relevant verification command before merging when one is known or was run during the task. Do not claim tests passed unless the command was actually run.
6. Merge locally:
   ```bash
   git switch "$BASE_BRANCH"
   git merge "$FEATURE_BRANCH"
   ```
7. If the user explicitly asked to sync with GitHub, push only the merged base branch:
   ```bash
   git push origin "$BASE_BRANCH"
   ```

Do not create a PR, push the feature branch, delete the feature branch, stash changes, or discard work unless the user explicitly asks.

## Decision Rules

- Choose `feat` for new user-visible capability or new workflow support.
- Choose `fix` for bug corrections or regression repairs.
- Choose `refactor` for internal restructuring without intended behavior change.
- Choose `docs`, `test`, `ci`, `build`, `perf`, `style`, `chore`, or `revert` when those are the dominant change types.
- Use a scope only when one subsystem, package, feature, or directory clearly dominates the diff.
- Omit the scope when the change spans several areas equally.
- Prefer multiple focused commits over one omnibus commit when the diff has independent review or rollback boundaries.

## Output Expectations

Produce a commit that matches the actual diff and tell the user:

- what was staged,
- the final commit subject(s),
- the main bullet-point body themes for each commit,
- the resulting commit hash(es),
- any remaining local changes not included in the commit,
- and whether automatic merge-back ran, skipped, or stopped for safety.

## Example Requests

- `Commit my current changes with a detailed message.`
- `Stage the files for this auth fix and create a conventional commit.`
- `Write a thorough git commit for the staged diff only.`
- `Inspect the repo changes and make one cohesive commit if appropriate.`
- `Commit this branch and merge it back to main locally.`
- `Commit only; do not merge.`
