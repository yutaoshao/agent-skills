---
name: ats-workflow-modeling
description: Model ATS stages, state transitions, roles, permissions, integrations, and recovery paths from product requirements.
---

# ATS Workflow Modeling

Turn ATS requirements into a reviewable behavior model before implementation.
Use this skill when stages, owners, permissions, external notifications, or
resume/interview/offer lifecycle rules are unclear. Do not use it as a visual
UI critique or as a substitute for a database migration design.

## Operating Contract

- Inspect the source requirements and existing implementation evidence first.
- Never invent a transition, permission, notification, or required field to make
  the diagram look complete. Mark it Decision Needed or Inferred.
- Every state must have an owner, entry condition, allowed actions, exit
  condition, visible result, and retained history where applicable.
- Model permissions at three levels: navigation visibility, data visibility,
  and mutation/action authority. Do not treat a hidden menu as authorization.
- Treat BOSS/source platforms, email, calendar/chat, and meeting tools as
  failure-prone boundaries. Include retries, idempotency, manual fallback, and
  user-visible failure states when relevant.
- Human-readable output defaults to Simplified Chinese. Keep internal state
  codes and API identifiers in English alongside their Chinese labels.
- Use synthetic candidates and job examples only.

## ATS Modeling Vocabulary

Typical actors include HR/recruiter, business reviewer or hiring manager,
interviewer, candidate, and system administrator. Typical objects include job,
candidate, application, resume/artifact, interview, feedback, offer, task,
notification, and talent-pool record. A project may rename or remove any of
these after evidence review.

## Workflow

1. Establish the boundary: the product, external systems, actors, and objects
   included in this model.
2. Build an actor/action inventory and identify the authoritative source of
   truth for each important field and status.
3. Build a state table. For each transition record trigger, actor, precondition,
   side effects, next state, failure behavior, and audit/history requirement.
4. Build the role matrix separately from the state table. Include view, create,
   edit, decide, schedule, export, archive, and admin actions as applicable.
5. Draw the main happy path and only the exception paths that change product
   behavior: rejection, hold, missing artifact, conflicting association,
   integration failure, retry, timeout, and manual completion.
6. Check that list views, detail views, tasks, notifications, APIs, and persisted
   state use the same owner and status vocabulary.
7. Produce the output contract and list unresolved decisions for
   ats-requirements-analysis or ats-product-review.

## Output Contract

Read [references/modeling-checklist.md](references/modeling-checklist.md) when
the model is non-trivial or a state/permission review is requested. Output, as
applicable:

- scope and actors;
- object/source-of-truth table;
- stage and state transition table;
- role-data-action permission matrix;
- main and exception flows;
- integration side-effect and recovery table;
- audit/history expectations;
- open decisions and evidence gaps.

Use stable IDs such as ST-01, TR-01, PERM-01, and INT-01. Keep a decision
condition observable; avoid vague labels such as "审核完成" without defining
who acts and what result is recorded.

## Handoffs

- Start from ats-requirements-analysis output when available.
- Send the state table and permission matrix to ats-uat-testing so tests cover
  every meaningful transition and role boundary.
- Send the complete model to ats-product-review for cross-document consistency.
- Use adr-management when the selected model affects security, persisted state,
  public contracts, integrations, or costly future migration.
