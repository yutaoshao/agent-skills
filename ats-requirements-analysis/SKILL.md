---
name: ats-requirements-analysis
description: Turn ATS notes, feedback, and interviews into evidence-backed, decision-ready product requirements and acceptance scope.
---

# ATS Requirements Analysis

Convert messy recruitment-system input into a product artifact that a developer,
HR stakeholder, and tester can use without guessing. This skill is for ATS
requirements, meeting notes, usability feedback, workflow disputes, and scope
questions. It is not a codebase onboarding or visual-only audit skill.

## Operating Contract

- Read the supplied documents, screenshots, transcripts, and existing product
  specs before drawing conclusions. Search the repository when a claim may be
  answered by code or existing documentation.
- Keep four claim states separate: Verified, Inferred, Unknown, and Decision
  Needed. A user preference is not a verified system behavior.
- Separate defects, requirements, UX observations, policy decisions, and
  implementation constraints. Do not turn a visual preference into a P0 defect.
- Preserve contradictions instead of silently merging them. State the competing
  interpretations and ask the smallest question that resolves the behavior.
- Human-readable output defaults to Simplified Chinese. Keep API fields,
  internal status values, and code identifiers in English when quoting them.
- Use synthetic examples only. Never copy candidate names, contact details,
  resumes, email addresses, or other personal data into a skill artifact.

## ATS Baseline

Use these as hypotheses only; project documents and confirmed stakeholder
decisions override them:

- Typical actors are HR/recruiter, business reviewer or interviewer, hiring
  manager, and system administrator.
- Typical objects are job, candidate, resume/artifact, application, interview,
  feedback, offer, task/notification, and talent-pool record.
- A common lifecycle is candidate intake -> HR screening -> resume/business
  review -> interview scheduling -> interview feedback -> offer -> talent pool or
  hire outcome. Do not assume every product uses every stage.
- External systems such as sourcing platforms, email, calendars, chat, and
  meeting tools are integration boundaries. Record manual fallback when an
  integration is unavailable.

## Workflow

1. Define the requested outcome, audience, evidence scope, and out-of-scope
   questions.
2. Extract actors, objects, goals, triggers, decisions, states, side effects,
   permissions, and terminology into an evidence ledger.
3. Normalize feedback into requirements, defects, UX findings, constraints,
   decisions, and open questions.
4. Write the smallest coherent process model implied by the evidence. Mark any
   inferred stage, owner, status, or required field as Inferred.
5. Resolve duplicate terms and conflicting rules. Prefer one canonical term and
   record aliases only when they occur in existing UI or APIs.
6. Define scope using Must, Should, Could, and Deferred. A future capability is
   not part of acceptance merely because it is desirable.
7. Produce the output contract below and list the next handoff to
   ats-workflow-modeling, ats-uat-testing, or ats-product-review.

## Output Contract

Read [references/output-contract.md](references/output-contract.md) when a
structured artifact is requested. At minimum, output:

- goal and user value;
- actors and product objects;
- terminology decisions;
- requirements with evidence and claim state;
- in-scope and out-of-scope behavior;
- unresolved contradictions and decision questions;
- acceptance signals or a clear handoff gap.

Use IDs that remain stable while the document is revised, such as REQ-01,
DEC-01, and Q-01. Keep one requirement per observable behavior.

## Handoffs

- Hand off requirements and unresolved decisions to
  ats-workflow-modeling before prescribing a state machine or permission matrix.
- Hand off approved or explicitly provisional requirements to ats-uat-testing
  for test scenarios and evidence collection.
- Hand off all relevant artifacts to ats-product-review when consistency,
  readiness, or MVP scope needs an independent pass.
- Use adr-management for decisions whose reversal affects persisted data,
  security, integrations, or multiple modules.
