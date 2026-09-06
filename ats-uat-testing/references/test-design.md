# ATS Test Design

## Risk Register

| ID | Risk | Likelihood | Impact | Evidence | Owner | Mitigation or acceptance decision |
|---|---|---:|---:|---|---|---|

Use qualitative Low/Medium/High values unless the team has a numeric scale.
High-impact risks include unauthorized candidate data access, wrong-stage
progression, duplicated external actions, lost candidate/job association, and
irreversible deletion.

## Acceptance Case

```text
ID: AT-01
Area: <stage or capability>
Preconditions: <role, records, integration state>
Given: <initial observable state>
When: <one user action or bounded action sequence>
Then: <visible result, persisted state, and side effects>
Evidence: <screenshot, response, record, log, or not available>
Claim state: Verified | Inferred | Unknown | Decision Needed
```

One case should prove one behavior. Add a separate case for each role, state,
or failure outcome that changes the expected result.

## Exploratory Charter

```text
Charter: <risk and target flow>
Mission: <what to learn>
Heuristics/tours: state transitions, permissions, boundaries, recovery, or data integrity
Timebox: <bounded duration or step count>
Oracles: <observable signals that indicate a problem>
Debrief: findings, questions, and follow-up regression cases
```

## Regression Selection

Select tests affected by changed stages, shared components, API contracts,
permission rules, persisted associations, integrations, and prior defects. Do
not call a full regression complete when a dependency or environment was not
available; list the untested slice.
