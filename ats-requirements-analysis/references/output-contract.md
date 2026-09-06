# ATS Requirements Output Contract

Use this structure for a reusable requirements artifact. Omit sections that are
truly out of scope, but state that they are out of scope.

```markdown
# <requirement title>

## Goal and User Value
- Goal:
- Primary users:
- Observable value:

## Evidence and Claim States
| ID | Claim | State | Evidence or reasoning |
|---|---|---|---|

## Actors and Objects
| Actor/object | Responsibility or meaning | Source |
|---|---|---|

## Terminology
| Canonical term | Avoided alias | Meaning and reason |
|---|---|---|

## Requirements
| ID | Requirement | Type | Priority | State | Evidence |
|---|---|---|---|---|---|

## Scope
- Must:
- Should:
- Could:
- Deferred/out of scope:

## Decisions and Open Questions
| ID | Decision/question | Options | Recommended default | Trade-off |
|---|---|---|---|---|

## Acceptance Signals
- <observable outcome>

## Handoff
- Next skill:
- Inputs it should receive:
```

Requirement types may be `business`, `workflow`, `permission`, `data`,
`integration`, `UX`, `operational`, or `constraint`. Keep one observable
behavior per requirement.
