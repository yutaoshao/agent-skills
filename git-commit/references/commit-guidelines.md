# Commit Guidelines

Use this reference after inspecting the real diff and before running `git commit`.

## Message Shape

Prefer this structure:

```text
type(scope): concise summary

- First concrete change
- Second concrete change
- Third concrete change or validation that actually happened
```

Keep the subject imperative and specific. Avoid trailing periods. Keep it under roughly 72 characters when practical.

## Type Selection

- `feat`: add user-visible functionality, new flows, or new supported behavior
- `fix`: correct a bug, regression, edge case, or broken integration
- `refactor`: restructure internals without intended behavior change
- `perf`: improve speed, memory use, or query efficiency
- `docs`: change documentation only
- `test`: add or update automated tests without meaningful product changes
- `build`: change dependency management, packaging, or build tooling
- `ci`: change CI workflows, release automation, or pipeline configuration
- `style`: change formatting only, with no logic impact
- `chore`: routine maintenance that does not fit a more specific type
- `revert`: revert a previous commit

Choose the dominant type. If the diff includes a little documentation or test maintenance alongside a feature or fix, keep the feature or fix type.

## Scope Selection

- Use a scope only when one package, directory, feature area, or subsystem clearly dominates the diff.
- Prefer product or module names over generic filenames.
- Omit the scope when the change spans multiple areas equally.

Good scope examples:

- `agent`
- `auth`
- `api`
- `search`
- `cli`

## Body Rules

- Write 2 to 6 bullets.
- Ground every bullet in the actual diff.
- Mention migrations, schema changes, compatibility implications, or cleanup of obsolete paths when relevant.
- Mention tests only when they were added, changed, or run.
- Do not claim validation, bug fixes, or behavior changes that the diff does not support.

Useful bullet patterns:

- `- Add ...`
- `- Wire ... into ...`
- `- Refactor ... to ...`
- `- Remove obsolete ...`
- `- Add tests for ...`
- `- Update docs for ...`

## Staging Rules

- Default to committing the already staged set when staged and unstaged changes coexist.
- Prefer explicit `git add <path>...` commands over `git add -A`.
- Ask before bundling unrelated changes into one commit.
- Avoid staging local environment files, secrets, transient editor files, or OS metadata unless the user clearly wants them committed.

## Example

```text
feat(agent): add deep research engine with multi-round search

- Add DeepResearch orchestration with multi-round planning and synthesis
- Introduce a pluggable ResearchProvider interface for search backends
- Wire the default Tavily provider into the application lifecycle
- Add unit tests for parsing, deduplication, and saturation handling
```
