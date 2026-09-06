---
name: ats-uat-testing
description: Design and run evidence-based ATS acceptance, exploratory, regression, and role-permission tests.
---

# ATS UAT Testing

Design tests that answer whether an ATS workflow is usable and correct for HR,
interviewers, business reviewers, and administrators. Use this skill for a test
plan, acceptance cases, exploratory sessions, defect triage, regression scope,
or an evidence-backed release verdict. It does not implement product code or
replace the browser automation tool.

## Operating Contract

- Read the requirements and workflow model before choosing tests. If they are
  missing or contradictory, state the gap and test only what is justified.
- Prefer risk-based coverage over a large undifferentiated checklist. Prioritize
  irreversible, privacy-sensitive, cross-role, state-changing, and external-
  integration behavior.
- Test observable outcomes: visible state, persisted association, allowed or
  denied action, notification status, audit record, and recoverable failure.
- For every defect, preserve exact reproduction steps, preconditions, actual
  result, expected result, environment, evidence, and impact. Do not infer a
  root cause from a screenshot alone.
- Distinguish a product defect, requirement ambiguity, environment blocker,
  test-data problem, and UX opportunity.
- Use Verified, Inferred, Unknown, and Decision Needed for claims about behavior.
- Human-readable output defaults to Simplified Chinese. Keep HTTP status codes,
  API fields, internal state codes, and test IDs in English where useful.
- Use synthetic candidate records, resumes, emails, and calendars. Do not send
  real personal data to a cloud browser or external testing service.

## Coverage Model

Cover the applicable dimensions:

- main recruitment path from intake through screening, interview, offer, and
  talent-pool outcome;
- state transitions, duplicate actions, reopen/edit behavior, and terminal
  states;
- role and field visibility, deep links, direct API access, and mutation
  authority;
- form validation, empty/loading/error states, long text, missing resume,
  conflicting candidate association, and boundary values;
- external calendar, chat, email, sourcing-platform, and meeting failures,
  retries, idempotency, delivery status, and manual fallback;
- visual consistency and interaction only when it changes task completion or
  comprehension.

## Workflow

1. Establish target build, environment, roles, test data, and the flow under
   test. Record anything unavailable before testing.
2. Translate each acceptance criterion into one or more observable checks using
   Given/When/Then or explicit steps.
3. Add exploratory charters for risky unknowns and state/permission boundaries.
4. Run the smallest useful test set. Use Playwright or another available browser
   tool for interaction; re-snapshot after navigation or major UI changes.
5. Capture evidence for failures and classify severity by user/business impact,
   reachability, data/privacy risk, and recoverability.
6. Build a regression set from changed states, shared components, APIs,
   integrations, and previously fixed defects.
7. Report a verdict: Ready, Ready with known issues, Blocked, or Not Ready. A
   blocked environment is not a passing result.

## Output Contract

Read [references/test-design.md](references/test-design.md) for the test-plan
and acceptance-case structure. Read
[references/defect-template.md](references/defect-template.md) when reporting
failures. The result should contain:

- scope, evidence, environment, roles, and test data;
- risk register and prioritized test coverage;
- acceptance cases and exploratory charters;
- defects with reproducible evidence and severity;
- regression impact and untested areas;
- a release verdict with explicit blockers and assumptions.

## Handoffs

- Consume requirements from ats-requirements-analysis and state/permission
  models from ats-workflow-modeling.
- Send failed behavior and unresolved acceptance questions to
  ats-product-review.
- Use impeccable for a separate visual/UX audit and trellis-check after code
  changes. Do not use a UI screenshot as a substitute for state or API evidence.
