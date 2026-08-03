# Evidence Policy

Use this policy for every onboarding report and deep audit. Match the strength of
the conclusion to the evidence actually inspected.

## Contents

- [Claim States](#claim-states)
- [Evidence By Claim Type](#evidence-by-claim-type)
- [Claim Records](#claim-records)
- [Negative And Conflicting Evidence](#negative-and-conflicting-evidence)
- [Heuristics And Metrics](#heuristics-and-metrics)
- [Command Safety And Verification](#command-safety-and-verification)
- [Dependency And Security Claims](#dependency-and-security-claims)

## Claim States

| State | Use when | Do not use when |
|---|---|---|
| `Verified` | Claim-appropriate direct evidence supports the conclusion and no material contradiction remains | A filename, directory name, comment, keyword, or unchecked document is the only support |
| `Inferred` | Several observations support an explicit reasoning chain, but runtime or independent corroboration is missing | The evidence is too sparse or contradictory to choose a conclusion |
| `Unknown` | Evidence is absent, inaccessible, outside scope, or contradictory | A scoped search merely returned no match |
| `N/A` | The check is demonstrably irrelevant to the repository type or selected journey | The analyst did not inspect it |

Use `Blocked` only for an attempted verification command that could not complete.
It describes the check result, not the truth of the underlying claim.

Use exactly one state per atomic claim. Split clauses with different evidence.
Keep qualifiers such as "documented," "static implementation," or "runtime" in
the claim text; never extend or combine state values with slashes, conjunctions,
or new labels such as `Observed`.

## Evidence By Claim Type

Evidence authority depends on the claim:

| Claim | Strong evidence | Important limitation |
|---|---|---|
| Declared product intent | Product docs, user docs, public UI, CLI help, API description | Verifies what the project claims, not current implementation |
| Current static implementation | Concrete symbols, call sites, manifests, schemas, generated contracts, configuration | Does not prove the path succeeds at runtime |
| Runtime behavior | Passing targeted test, observed local execution, trace/log from the inspected revision | Record environment, command, revision, and result |
| Module collaboration | Both sides of a call/event/data contract plus composition or wiring | Similar names or neighboring directories are insufficient |
| Dependency version | Manifest and lockfile or resolved package metadata | A version range is not the installed version |
| Dependency health | Current authoritative registry, maintainer, advisory, or release source | Record retrieval date; do not infer from lockfile filesystem mtime |
| Team process | Applicable repository instructions, CI config, contribution docs, verified hosting policy | Local branch names do not prove the team's workflow |
| Historical change | Git history for the relevant path and revision | Filesystem timestamps are not repository history |

A document-only behavior claim remains `Inferred` unless the report explicitly
states only that the behavior is documented. A static fact may be `Verified`
without execution when its canonical artifact directly establishes that fact.

## Claim Records

Record every material claim with a state and evidence. For every `Inferred` or
`Unknown` claim, also record the reasoning or gap inline or link it through a
stable claim ID to the report's conflicts and unknowns section:

| Claim | State | Evidence | Reasoning or gap |
|---|---|---|---|
| [Specific claim] | Verified / Inferred / Unknown / N/A | `path:symbol`, `path:line`, command result, or authoritative source | [Why the evidence is sufficient, or what is missing] |

For a straightforward `Verified` static fact, exact canonical evidence can make
the reasoning self-evident. Prefer symbol references when line numbers are
unstable. Include both when useful. For executed checks, record the exact command,
exit status, relevant output, and environment limitations. Do not say a command
passed when only its definition was read.

## Negative And Conflicting Evidence

For absence claims, report:

- the repository and revision searched;
- included and excluded paths;
- search patterns or structured fields inspected;
- generated, vendored, ignored, private, or inaccessible areas;
- whether history, submodules, and external services were in scope.

Translate "no match in the inspected scope" to `Unknown` unless the inspected
canonical artifact is exhaustive for that claim. For example, a parsed manifest
can verify that a dependency is not declared there, but a filename search cannot
verify that the behavior does not exist.

When sources disagree:

1. Preserve both observations.
2. Prefer the source authoritative for that claim type.
3. Explain the conflict and its practical consequence.
4. Use `Inferred` or `Unknown` until the conflict is resolved.

## Heuristics And Metrics

Use filenames, directory layouts, file size, function length, nesting depth,
TODO counts, and keyword clusters only to choose what to inspect next. Before
turning a lead into a finding, establish behavioral or maintenance impact.

Do not:

- equate top-level directories with runtime modules;
- force a repository into one architecture label;
- call a large file a god object without responsibility and change-coupling evidence;
- treat missing E2E tests as a defect without a relevant user boundary;
- estimate line counts or coverage when exact tools or data are unavailable;
- use checkout-dependent modification times as maintenance evidence.

## Command Safety And Verification

Classify commands before execution:

| Class | Examples | Default action |
|---|---|---|
| Read-only inspection | `rg`, manifest parsing, `git status`, `git log`, listing files | Run within repository instructions |
| Local validation | Targeted tests, type checks, builds, linters | Inspect scripts and side effects first; run only when clearly local and reversible |
| State-changing | Install, generate, format, migrate, seed, start services, containers, external API calls | Require existing user authorization or ask before running |
| Destructive or production-facing | Deletes, resets, deploys, production database or infrastructure operations | Do not run without explicit, target-specific authorization |

Record the worktree state before and after validation when commands may generate
files. Do not remove or revert user changes to restore cleanliness.

## Dependency And Security Claims

- Use structured manifest and lockfile parsers where available.
- Use current authoritative sources for latest-version, maintenance, deprecation,
  or vulnerability claims and record the retrieval date.
- If network access or an audit tool is unavailable, mark health `Unknown` rather
  than guessing from age or popularity.
- Treat secret-pattern matches as potential findings until validated. Never print,
  decode, or reproduce candidate values. Report only path, line, suspected class,
  and a redacted fingerprint if one is needed for deduplication.
- Inspect tracked or distributed content in the authorized scope, including
  examples and shipped generated artifacts. Classify each match as confirmed
  synthetic, confirmed live, or unresolved without exposing its value. Exclude a
  match from conclusions only after confirming it is synthetic or outside scope,
  and record that decision. Treat third-party vendor content separately while
  still reporting any distribution risk that remains in scope.
