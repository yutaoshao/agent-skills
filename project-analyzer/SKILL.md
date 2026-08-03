---
name: project-analyzer
description: Analyze unfamiliar repositories for project takeover and developer onboarding by building an evidence-backed mental model of the product context, core module collaboration, and one representative end-to-end user journey. Use when asked to understand a codebase, explain what a project does, map architecture or entry points, trace a business flow, prepare a handover, or perform focused dependency, quality, workflow, security, or technical-debt analysis.
---

# Project Analyzer

Help a newcomer explain what a project is for, how its core modules collaborate,
and how one real user journey moves through entry points, key code, data or side
effects, and tests. Prefer a coherent, evidence-backed mental model over a broad
inventory.

## Operating Contract

- Default to read-only inspection. Preserve the worktree and unrelated user
  changes.
- Read applicable repository instructions before analyzing code, including
  `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and nested equivalents.
- Inspect a command and its repository-defined behavior before running it.
  Treat dependency installation, code generation, migrations, seeds, service
  startup, container orchestration, and external calls as state-changing.
  Request authorization unless the user already authorized that action.
- Run tests or builds only when their scope and side effects are understood.
  Report commands that were not run instead of implying they passed.
- Never expose a discovered secret value. Report only its location, suspected
  class, and a redacted description.
- Use current authoritative sources for time-sensitive dependency or platform
  claims. If current data cannot be checked, mark the claim `Unknown`.
- Ask a question only when ambiguity materially changes the repository scope or
  the journey to trace. Otherwise state the assumption and continue.

## Evidence Rules

Read [references/evidence-policy.md](references/evidence-policy.md) before making
material architecture, behavior, absence, health, or risk claims.

Use these states throughout the analysis:

- `Verified`: supported by direct, claim-appropriate evidence and no unresolved
  contradiction.
- `Inferred`: supported by indirect or incomplete evidence and a stated reasoning
  chain, but missing the corroboration required for that claim type.
- `Unknown`: evidence is missing, conflicting, inaccessible, or outside the
  inspected scope.
- `N/A`: demonstrably irrelevant to this project type or analysis scope.

Use exactly one of these four values in each claim-state field. Split a compound
claim when its parts have different evidence. Put scope qualifiers such as
"declared intent," "static implementation," or "runtime behavior" in the claim
wording, not in the state value. `Observed` and `Blocked` are verification-result
descriptions, not additional claim states.

Attach an exact file, symbol, line, command result, or authoritative source to
every material claim. Directory names, file size, and single keyword matches are
investigation leads, never sufficient evidence of core value, architecture,
quality, or risk. For negative findings, record the search scope and exclusions;
"not found" does not mean "does not exist."

## Choose The Analysis Mode

- **Onboarding (default):** Use for takeover, overview, handover, or "help me
  understand this project" requests. Run the core workflow below.
- **Focused analysis:** Use when the user asks about one stack, module, entry
  point, journey, dependency, workflow, or risk. Run Preflight and only the
  relevant workflow portions.
- **Deep audit:** Use only when the user explicitly asks for a comprehensive
  quality, dependency, security, workflow, or technical-debt assessment. Load
  [references/analysis-checklist.md](references/analysis-checklist.md).

Do not turn an ambiguous onboarding request into a deep audit.

## Investigate Progressively

- Start with the minimum evidence needed to choose a representative journey; do
  not inventory the whole repository first.
- Make each search or file read answer a completion-gate question, close a known
  evidence gap, or verify the next hop in the selected journey.
- Stop expanding into unrelated modules once the selected journey is supported
  and remaining gaps are documented.
- For monorepos, inspect only the workspaces and contracts crossed by the journey
  unless the user requests a broader map.

## Core Onboarding Workflow

### 1. Establish Scope And Provenance

1. Resolve the repository and workspace roots, current branch and commit, dirty
   state, submodules, and nested projects.
2. Read repository instructions and primary human documentation first.
3. Identify generated, vendored, build-output, fixture, archived, and private
   areas. Exclude them unless they are part of the selected journey.
4. Record the inspected scope and any access, tooling, network, or runtime
   limitations.

### 2. Build The Product And Domain Model

1. Determine the project's declared purpose, primary users or actors, and the
   value it delivers.
2. Extract domain terms, important entities, state transitions, invariants, and
   external systems from claim-appropriate sources such as product docs, user
   interfaces, CLI help, public APIs, schemas, fixtures, and tests.
3. Separate declared intent from implemented behavior. Surface stale or
   conflicting documentation.
4. List a small set of concrete, regular user journeys that could represent the
   project's core value.

### 3. Classify The Project And Map Responsibilities

Read [references/journey-playbooks.md](references/journey-playbooks.md) and choose
the applicable project-type guidance. Allow hybrid and monorepo classifications.

Map modules by runtime responsibility and contract, not by directory shape.
For each core module, identify:

- responsibility and user-facing contribution;
- inbound entry points or callers;
- outbound calls, events, or data contracts;
- state owned or transformed;
- external side effects;
- tests or other verification surfaces.

Use [references/architecture-patterns.md](references/architecture-patterns.md)
only when architecture terminology materially improves the explanation. Treat
every catalog match as a hypothesis until corroborated by runtime composition,
dependency direction, deployment boundaries, state ownership, or the selected
journey.

### 4. Select One Representative Journey

Choose the normal success path that best satisfies these criteria, in order:

1. It directly demonstrates the project's core user value.
2. It crosses important module or system boundaries.
3. Its important steps can be checked against code, tests, or documentation.
4. It represents regular use rather than setup, health checks, administration,
   or an unusual error path.

State why the journey was selected and why plausible alternatives were not. If
the core journey cannot be established, select the best-supported provisional
journey, mark it `Inferred`, and list the evidence needed to confirm it.

### 5. Trace The Journey End To End

Follow concrete symbols rather than describing a generic layered architecture.
Trace, where applicable:

1. actor, trigger, input, and preconditions;
2. user-facing, API, CLI, event, job, or library entry point;
3. validation, authentication, authorization, and configuration;
4. orchestration and core domain decisions;
5. state reads, writes, transactions, or artifacts;
6. messages, jobs, filesystem, network, or other external side effects;
7. returned result or user-visible outcome;
8. tests, fixtures, or smoke checks that exercise the path.

For every hop, capture the symbol and location, responsibility, input/output,
state change or side effect, evidence, and evidence state. Verify both sides of
important boundaries when possible. Include one material guard or failure path
only when it clarifies the normal journey.

### 6. Verify What Can Be Verified Safely

1. Discover setup, run, test, and build commands from canonical repository
   sources.
2. Distinguish documented commands from commands actually executed.
3. Prefer the smallest targeted check that validates the selected journey.
4. Record the exact command, exit status, relevant result, and blocker.
5. Do not claim that the project runs, builds, or passes tests unless observed.

### 7. Synthesize The Onboarding Report

Load [references/report-template.md](references/report-template.md). Lead with the
project's purpose and selected journey, then explain module collaboration and the
evidence-backed trace. Keep technology inventory and general audit findings
secondary unless they block understanding the journey. Include every applicable
core section from the template. A concrete reading order and one explicit final
outcome are required even when the user requests a concise report.

## Optional Deep Dives

Run only the requested or materially relevant sections of
[references/analysis-checklist.md](references/analysis-checklist.md):

- technology and dependency health;
- test and code-quality infrastructure;
- development, CI/CD, and release workflow;
- security and trust boundaries;
- reliability, performance, and observability;
- technical debt and change risk.

Do not assign risk from arbitrary size thresholds, missing tools, or pattern
preferences alone. Base severity on demonstrated impact, likelihood, reachability,
and evidence quality. Do not label dependencies current, deprecated, vulnerable,
or unmaintained without fresh authoritative data and a retrieval date.

## Completion Gate

Assess whether the report lets a newcomer answer:

- Who uses this project, in what scenario, and for what value?
- Which modules are core, what does each own, and how do they collaborate?
- Where does the selected journey enter the system?
- Which concrete symbols implement its important decisions?
- Where does it read or change state, and what side effects occur?
- Which tests or observations verify the journey?
- Which parts remain inferred or unknown, and why?

End with one explicit outcome:

- **Onboarding complete:** every question above is answered with sufficient
  evidence for the stated claim status.
- **Analysis complete; onboarding incomplete:** one or more questions remain
  unanswered because of named evidence, access, runtime, or scope gaps. List the
  exact gaps and the next evidence needed; do not continue searching without a
  new lead or expanded authority.

Completeness does not require line counts, a full dependency list, an overall
health grade, or running every optional audit.
