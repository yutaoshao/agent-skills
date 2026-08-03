# Project Onboarding Report Template

Load this template only after collecting evidence. Remove empty examples and
optional sections rather than filling them with generic content.

Give material claims stable IDs such as `C1`. Every `Inferred` or `Unknown` claim
must explain its reasoning or gap inline or link by ID to section 7.

# Project Onboarding Map: [Project Name]

| Field | Value |
|---|---|
| Scope | [Repository or subtree analyzed, plus exclusions] |
| Revision | [Branch and commit, or Unknown] |
| Worktree | [State observed at analysis start] |
| Verification boundary | [Static inspection and commands actually run] |
| Delivered behavior | [Examples: application, service, CLI, library or package, SDK, pipeline, infrastructure, plugin, documentation, or hybrid; include evidence state] |
| Repository topology | [Examples: single package, workspace/monorepo, or nested projects; include evidence state] |

## Evidence Legend

- `Verified`: Claim-appropriate direct evidence supports the exact statement.
- `Inferred`: Evidence supports the reasoning, but a named link or corroboration
  is missing.
- `Unknown`: The claim was not established within the inspected scope.
- `N/A`: The item is demonstrably irrelevant to this project or journey.

Documentation verifies documented intent, not implemented runtime behavior.
Each claim-state cell must contain exactly one listed state. Split compound claims
instead of combining states or adding qualifiers to state values.

## 1. 60-Second Orientation

| ID | Question | Finding | State | Evidence |
|---|---|---|---|---|
| C1 | Who consumes, uses, or operates this project? | | | |
| C2 | In what regular situation is it used? | | | |
| C3 | What observable outcome delivers its core value? | | | |
| C4 | What kind of project or delivery unit is it? | | | |
| C5 | What must a newcomer understand first? | | | |

### Domain Vocabulary And Invariants

Include only terms and rules needed to follow the selected journey.

| Term or invariant | Meaning in this project | State | Evidence |
|---|---|---|---|
| | | | |

## 2. Representative Journey

**Selected journey:** [Actor or consumer performs a concrete action to obtain an
observable result]

**Selection state:** [Verified / Inferred / Unknown]

**Selection evidence:** [Exact code, test, documentation, or observed result]

**Selection rationale:** [How it demonstrates core value, crosses important
boundaries, represents normal use, and can be verified]

### Candidates Considered

| Candidate journey | User value | Key boundaries | Available evidence | Decision |
|---|---|---|---|---|
| | | | | Selected or deferred, with reason |

### Scenario Contract

| Actor or consumer | Preconditions | Trigger or input | Observable success | Out of scope | State | Evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

If the selection is `Inferred`, state what evidence would confirm or replace it.

## 3. Core Responsibilities And Collaboration

Define modules by responsibility, contract, and state ownership rather than by
directory names.

| ID | Module or subsystem | Responsibility | Public boundary or key symbols | Owns or changes | Collaborates with | State | Evidence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Add a compact collaboration diagram only when it materially clarifies three or
more observed boundaries. Use repository-specific component names and label every
edge with its call, command, data, artifact, or event. Do not emit a generic
controller-service-repository diagram.

## 4. End-To-End Journey Trace

| ID | # | Journey stage | Concrete file and symbol | Input to output | Handoff or next boundary | State change or side effect | State | Evidence |
|---|---|---|---|---|---|---|---|---|
| | 1 | Trigger or entry | | | | | | |
| | 2 | Parsing or boundary checks | | | | | | |
| | 3 | Orchestration or core decision | | | | | | |
| | 4 | State or output production | | | | | | |
| | 5 | Observable result | | | | | | |

Adapt stages to the project type. Use `N/A` with evidence when a stage does not
apply. Never invent HTTP, UI, database, worker, or external-service layers to fill
the table.

### Material Guard Or Failure Path

Include one guard or failure path only when it explains an important invariant,
boundary, or side-effect constraint in the normal journey.

| Trigger | Handling path | User or system effect | State | Evidence |
|---|---|---|---|---|
| | | | | |

## 5. Tests And Runtime Verification

| Behavior or claim | Exact test or command | Exit status | Relevant result, blocker, or environment limitation | What it establishes | Claim state | Evidence |
|---|---|---|---|---|---|---|
| | | [Code or N/A] | Passed / Failed / Blocked / Not run: reason | | | |

Distinguish "test exists" from "test passed." A documented command or blocked
check does not verify runtime behavior.

## 6. Recommended Reading Order

Prefer the shortest path that reconstructs the selected journey.

| Order | File or symbol | Read it to answer | Depends on |
|---|---|---|---|
| 1 | | | |

## 7. Conflicts, Inferences, And Unknowns

| Claim ID | Question or claim | Evidence checked | Gap or conflict | Why it matters | Next evidence to obtain | State |
|---|---|---|---|---|---|---|
| | | | | | | |

For a negative search result, include the search scope and exclusions. Do not
translate a scoped miss into a repository-wide absence claim.

**Outcome:** [Onboarding complete / Analysis complete; onboarding incomplete]

For an incomplete outcome, name the unmet completion gates and the next evidence
needed. Do not present the gap as a generic recommendation.

## Optional Appendices

Add only when requested or necessary to understand the selected journey:

- technology stack and runtime constraints;
- verified setup, run, build, or test commands;
- dependency health;
- quality and testing infrastructure;
- CI, release, and deployment workflow;
- security, reliability, performance, or observability;
- technical debt and change risk;
- broader repository inventory.
