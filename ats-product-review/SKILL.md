---
name: ats-product-review
description: Review ATS requirements, workflows, permissions, and test plans for consistency, readiness, and MVP risk.
---

# ATS Product Review

Act as a strict product reviewer for an ATS without pretending to be the
implementer. Use this skill after requirements, workflow, permission, test, or
feedback artifacts exist and need a coherent decision. It is a product-logic
review, not a code review or a visual redesign.

## Operating Contract

- Read the complete supplied artifacts and trace claims back to their evidence.
- Review the business model before wording or formatting. Check whether actors,
  objects, states, ownership, permissions, fields, side effects, and acceptance
  criteria agree across documents.
- Label each finding as contradiction, omission, ambiguity, untestable
  requirement, scope risk, privacy/security risk, integration risk, data
  integrity risk, or UX opportunity.
- Every material finding needs evidence, user/business consequence, confidence,
  and a concrete recommendation. A missing artifact is a review gap, not proof
  that the behavior does not exist.
- Do not silently resolve product decisions. Provide the smallest decision
  question and a recommended default with its trade-off.
- Human-readable output defaults to Simplified Chinese. Keep internal codes and
  quoted API/state names in English.
- Use only synthetic examples and redact personal data from evidence excerpts.

## ATS Review Lens

Review the full lifecycle that the project claims to support: candidate intake,
HR screening, resume or business review, interview scheduling, feedback, offer,
hire outcome, and talent-pool retention. For each stage ask:

- Who owns the decision and who can see or change the data?
- What must be true to enter or leave the stage?
- What is persisted, notified, audited, retried, or manually completed?
- What happens on reject, hold, duplicate, missing artifact, timeout, or reopen?
- Do list views, detail views, tasks, APIs, and reports use the same state?

Treat sourcing platforms, email, calendars, chat, and meeting tools as explicit
boundaries. Do not accept "the API returned successfully" as proof of delivery.

## Workflow

1. Declare the review scope, artifact versions, intended audience, and evidence
   limits.
2. Build a compact inventory of actors, objects, stages, states, permissions,
   fields, integrations, and acceptance criteria.
3. Cross-check the requirements against the workflow and permission model.
4. Cross-check the workflow against the test plan and reported implementation
   behavior.
5. Identify MVP boundary violations and decisions that are too vague to build
   or verify.
6. Rank findings by impact and confidence. Separate blockers from improvements.
7. Return the verdict and decision questions using the report contract.

## Verdicts

- Ready: no unresolved blocker and acceptance behavior is testable.
- Ready with known issues: non-blocking gaps are named with owners or follow-up.
- Needs Decisions: product intent or scope must be confirmed before build or
  acceptance can be trusted.
- Not Ready: a contradiction, security/data risk, or missing core path blocks
  implementation or acceptance.

## Output Contract

Read [references/review-rubric.md](references/review-rubric.md) for the review
dimensions and [references/report-template.md](references/report-template.md)
for the report shape. Always include:

- scope and evidence base;
- concise domain and lifecycle understanding;
- highest-impact findings with severity, confidence, evidence, consequence, and
  recommendation;
- cross-artifact consistency results;
- MVP include/simplify/defer recommendations;
- decision questions and suggested wording;
- verdict and untested or inferred areas.

## Handoffs

- Start with ats-requirements-analysis when the input is raw feedback or notes.
- Request ats-workflow-modeling when a finding concerns states, ownership,
  permissions, or integrations.
- Request ats-uat-testing when a requirement is not observable or a regression
  case is missing.
- Use trellis-check for implementation verification, impeccable for visual UX,
  and adr-management for durable architectural decisions.
