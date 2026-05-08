---
name: module-diagram-planner
description: Use when analyzing a feature, subsystem, or code module and deciding which architecture, runtime, data flow, decision, state, error, metrics, or test diagrams would best explain it before drawing diagrams.
---

# Module Diagram Planner

Plan high-signal diagrams for a feature or module. The goal is to choose the smallest useful set of diagrams that helps a reader understand boundaries, behavior, decisions, data, failures, and validation without producing decorative or redundant diagrams.

## When to Use

Use this skill when the user asks:

- What diagrams would explain a module, feature, subsystem, service, flow, or architecture.
- To prepare Mermaid diagrams, design docs, module docs, onboarding docs, or review aids.
- To understand routing, gateways, schedulers, APIs, storage, integrations, stateful flows, observability, or tests.

Do not use it for whole-repository onboarding unless the task is specifically about diagram planning; use a project-analysis skill first.

## Core Rules

- Inspect evidence before choosing diagrams: entry points, call sites, interfaces, config, data models, tests, logs, metrics, and failure handling.
- Each diagram must answer one explicit question. If no clear question exists, do not include that diagram.
- Prefer 3-5 diagrams for a normal feature. Use 1-2 for small modules and more only for large subsystems.
- Separate planning from drawing. First propose the diagram set, order, and contents; draw only after the user asks or approves.
- Be honest about uncertainty. Mark inferred links as inferred and list missing evidence.
- Prefer Mermaid for portable text diagrams unless the user requests another format.

## Workflow

1. **Define scope**
   - Name the module and the reader's goal: onboarding, review, debugging, design, operations, or testing.
   - Identify what is inside and outside the module boundary.

2. **Gather evidence**
   - Read the module entry point, public interfaces, configuration, key collaborators, tests, and recent docs.
   - Trace at least one representative happy path and one failure or edge path when available.

3. **Classify the module**
   - Routing or policy: decision tree, sequence, config, metrics.
   - API or integration: boundary, sequence, data flow, error paths.
   - Storage or pipeline: data flow, lifecycle, schema, failure paths.
   - Scheduler or workflow: state machine, timeline, sequence, recovery.
   - UI flow: screen map, state/data flow, interaction sequence.

4. **Choose diagrams**
   - Load `references/diagram-catalog.md` when the module is non-trivial or the best diagram types are not obvious.
   - Select diagrams by question, not by habit.
   - Avoid overlapping diagrams unless they serve different readers.

5. **Produce a diagram plan**
   - Recommended order.
   - Diagram type and title.
   - Question answered.
   - Nodes/entities to include.
   - Edges/events/labels to include.
   - Evidence sources and any uncertainty.

6. **Draw only when requested**
   - Use one diagram per distinct question.
   - Keep labels short and implementation-grounded.
   - After drawing, briefly explain how to read each diagram and what it intentionally omits.

## Output Template

```markdown
## Diagram Plan: <module>

Reader goal: <goal>
Scope: <inside boundary>; out of scope: <outside boundary>

| Order | Diagram | Question Answered | Include | Evidence |
|-------|---------|-------------------|---------|----------|
| 1 | Boundary diagram | Who owns what, and who talks to whom? | ... | ... |
| 2 | Sequence diagram | What happens during the main runtime flow? | ... | ... |
| 3 | Decision tree | How does the module choose behavior? | ... | ... |

Recommended first diagram to draw: <diagram>, because <reason>.
Open questions: <missing evidence or assumptions>
```

## Example: Model Routing

For a model-routing module, a good first plan is usually:

1. Boundary diagram: agent runtime, router, model gateway, providers, metrics.
2. Decision tree: input length, keywords, tools, purpose, default tier.
3. Sequence diagram: first user turn computes a route decision, later turns reuse it, gateway records actual provider/model.
4. Config map: routing enabled flag, default tier, tier provider configs, rule thresholds.
5. Metrics map: route tier/reason, provider/model, usage, cost, aggregation.

Skip a state machine unless the routing decision itself has persistent states.
