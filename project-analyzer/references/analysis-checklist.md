# Optional Deep-Dive Analysis Checklist

Load only the sections requested by the user or required to investigate a
material onboarding blocker. This is not the default onboarding workflow.

For each question, record:

| Question | Applicable? | State | Evidence | Consequence or next check |
|---|---|---|---|---|
| [Context-specific question] | Yes / No / Unknown | Verified / Inferred / Unknown / N/A | [Location or command] | [Why it matters] |

A missing practice becomes a finding only when project requirements, repository
rules, or a demonstrated user journey make it consequential.

## Contents

- [Technology And Dependencies](#technology-and-dependencies)
- [Testing And Code Quality](#testing-and-code-quality)
- [Development And Delivery Workflow](#development-and-delivery-workflow)
- [Security And Trust Boundaries](#security-and-trust-boundaries)
- [Error Handling And Reliability](#error-handling-and-reliability)
- [Performance And Scalability](#performance-and-scalability)
- [Observability](#observability)
- [Technical Debt And Change Risk](#technical-debt-and-change-risk)
- [Risk Reporting](#risk-reporting)

## Technology And Dependencies

Investigate only the manifests, lockfiles, packages, and runtime units in scope.

- Which languages, runtimes, frameworks, package managers, databases, brokers,
  and platform services participate in the selected scope?
- Which version source is authoritative: runtime file, manifest, lockfile,
  resolved environment, container image, or CI configuration?
- Which third-party dependencies sit on the representative journey or another
  critical boundary?
- Are versions reproducible from committed manifests and locks?
- Which internal packages depend on each other through verified exports,
  contracts, or runtime calls?
- Are there demonstrated duplicate, unused, circular, deprecated, vulnerable, or
  unmaintained dependencies?
- What fresh authoritative source and retrieval date support any maintenance,
  deprecation, latest-version, or vulnerability claim?

Do not use lockfile filesystem modification time as maintenance evidence. Use Git
history for repository change timing and current authoritative package sources
for ecosystem health. If those sources are unavailable, mark health `Unknown`.

## Testing And Code Quality

- Which test types exist for the selected behavior and important boundaries?
- Which assertions prove user-visible outcomes, state changes, and side effects?
- Were relevant tests executed in the current environment? Record command and
  result separately from test discovery.
- Are fixtures, fakes, mocks, and generated data representative of the boundary
  under test?
- Which formatter, linter, type checker, static analyzer, or coverage tool is
  required by repository policy or CI?
- Do suppressions, weak types, duplication, or complex control flow create a
  demonstrated maintenance or correctness problem?
- Does the public API or critical business logic lack a relevant verification
  surface?

File length, function length, nesting, and test-to-source ratios are investigation
leads only. Do not assign severity without showing responsibility concentration,
change coupling, defect risk, or another concrete consequence. Do not require E2E
tests when the project has no relevant end-to-end user boundary.

## Development And Delivery Workflow

- What are the canonical install, configure, run, targeted-test, full-test, build,
  package, and release commands?
- Which commands were only documented, which were inspected, and which were run?
- Which environment variables and external services are required, and how are
  safe local values supplied?
- What CI stages and release artifacts are verified by repository configuration?
- Which deployment units and environments exist in the inspected scope?
- What do repository instructions require for branches, commits, reviews, and
  releases?
- Which claims require hosting-provider data that was not inspected?

Do not infer team workflow from local branch names or `.git/refs/heads`. Local Git
state can verify the inspected checkout, not remote policy or team practice.

## Security And Trust Boundaries

- Where does untrusted input enter the selected journey?
- Which validation, authentication, authorization, and policy checks apply?
- Where are trust boundaries crossed through HTTP, RPC, messages, files,
  subprocesses, plugins, templates, or deserialization?
- Are database queries, shell commands, paths, and templates constructed through
  safe APIs at those boundaries?
- How are credentials referenced, loaded, rotated, and prevented from appearing
  in logs or artifacts?
- Are CORS, CSRF, XSS, rate limiting, sandboxing, or permission checks applicable
  to this project and boundary?
- Are dependency advisories checked by a current authoritative tool or source?

Treat secret-pattern matches as potential findings. Never print or decode values;
report only the location, suspected class, and redacted description. Record
tracked-source scope and exclusions. A generic search cannot verify that the
repository contains no secrets.

## Error Handling And Reliability

- How do failures propagate across each boundary in the selected journey?
- Are errors classified, preserved, logged, translated, retried, or swallowed?
- What transaction, idempotency, timeout, retry, dead-letter, cleanup, and
  graceful-shutdown behavior is applicable?
- Can partial state or duplicate side effects occur?
- Which tests exercise material failure and recovery behavior?

Do not require a global error handler, graceful shutdown, retries, or a dead-letter
queue when the runtime model does not call for them.

## Performance And Scalability

- Which latency, throughput, memory, storage, cost, or concurrency constraints are
  documented or visible in the selected journey?
- Are queries, pagination, caching, batching, streaming, indexes, asset sizes, or
  blocking operations relevant to the observed bottleneck?
- Is there profiling, benchmark, load-test, query-plan, or production evidence?
- Which conclusion is only a hypothesis pending measurement?

Do not present a theoretical optimization opportunity as a current performance
defect without impact evidence.

## Observability

- Which logs, metrics, traces, events, health signals, or audit records make the
  selected journey observable?
- Do correlation identifiers cross process or asynchronous boundaries where
  applicable?
- Can an operator distinguish input failure, dependency failure, internal failure,
  and partial success?
- Are alerting and dashboards in repository scope or hosted elsewhere?

Do not require distributed tracing, health endpoints, or request logging for a
library, static artifact, or other project without those operational boundaries.

## Technical Debt And Change Risk

- Which TODO, FIXME, workaround, duplication, legacy path, or inconsistent pattern
  intersects core value or a high-change boundary?
- Does Git history show repeated fixes, coupled changes, ownership concentration,
  or churn in the relevant area?
- Which generated, vendored, migration, compatibility, or public-contract files
  constrain changes?
- What tests, rollout mechanism, feature flag, migration plan, or rollback path
  reduce the change risk?
- Is the proposed concern reachable through a normal or security-relevant path?

Marker counts and repository size do not establish debt. Explain the consequence
of each reported item.

## Risk Reporting

Report only risks with a concrete consequence and evidence:

| Risk | Impact | Likelihood or reachability | Evidence state | Evidence | Suggested next check or action |
|---|---|---|---|---|---|
| [Specific failure or maintenance risk] | [User/system consequence] | [Why it can occur] | Verified / Inferred / Unknown | [Locations/results] | [Proportionate response] |

Order risks by demonstrated impact and likelihood, not discovery order or category.
Do not produce an overall health grade unless the user supplies a scoring rubric.
