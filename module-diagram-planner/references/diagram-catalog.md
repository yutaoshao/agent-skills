# Diagram Catalog

Use this catalog to choose diagrams by the question they answer.

| Diagram Type | Use When | Answers | Good Signals | Avoid When |
|--------------|----------|---------|--------------|------------|
| Boundary diagram | Ownership or dependencies are unclear | What is inside the module, what is outside, and who talks to whom? | Interfaces, adapters, external services, excluded responsibilities | The module is a single pure function |
| Container/component diagram | A subsystem has multiple deployable or logical parts | What are the major parts and responsibilities? | Processes, services, packages, layers | A boundary diagram already covers the same facts |
| Sequence diagram | Order, async behavior, streaming, retries, or callbacks matter | What happens over time in the main flow? | Request/response, event publish, retry, fallback, stream chunks | The flow is static configuration only |
| Decision tree | Rules, thresholds, policies, classifiers, permissions, or routing matter | How is behavior selected? | Conditions, defaults, precedence, fail-fast checks | Decisions are not explicit or testable |
| Data flow diagram | Transformations, persistence, or handoffs matter | How does data move and change shape? | Input/output schemas, stores, queues, derived records | No meaningful transformation happens |
| Config map | Behavior depends on config, env, templates, or overrides | Which settings control behavior, and where do they come from? | Defaults, required fields, validation, local overrides | Config is trivial or unrelated |
| State machine | Entities move through named states | What states exist and what transitions are allowed? | Job status, connection lifecycle, task lifecycle | The module is stateless |
| Error path diagram | Failures, retries, fallback, recovery, or fail-fast behavior matters | What fails where, how does it surface, and what recovers? | Exceptions, fallback rules, retry policy, user-visible errors | Errors are simple pass-through |
| Metrics/observability map | Logs, traces, metrics, cost, or audit events matter | What is emitted, where, and with which dimensions? | Event names, fields, aggregation dimensions | Observability is not implemented |
| Test coverage map | Reviewers need confidence in behavior | Which behavior is covered by which tests? | Test files, cases, happy/failure paths, uncovered risks | No tests exist and the user wants architecture only |
| Deployment/runtime diagram | Runtime hosting or process topology matters | Where does it run and how is it supervised? | Processes, ports, workers, launchers, external services | The user only needs code-level behavior |
| UI interaction map | A frontend feature has screens or user actions | What can the user do, and how does UI state move? | Screens, controls, routes, local/server state | There is no UI surface |

## Selection Heuristics

- Start with a boundary diagram when the reader does not know where the module begins.
- Add a sequence diagram when order or timing is part of correctness.
- Add a decision tree when behavior branches by rules or policy.
- Add a data flow diagram when data shape changes are central.
- Add an error path diagram when fallback, retries, or fail-fast behavior are important to review.
- Add a metrics map when the module affects cost, monitoring, auditing, or operations.
- Add a test coverage map before review or merge when risk is high.

## Common Bundles

**Routing/policy module**

Boundary diagram, decision tree, sequence diagram, config map, metrics map.

**Gateway/integration module**

Boundary diagram, sequence diagram, error path diagram, config map, metrics map.

**Storage/pipeline module**

Data flow diagram, schema or record lifecycle, error path diagram, test coverage map.

**Scheduler/workflow module**

State machine, sequence diagram, runtime diagram, error/recovery path, metrics map.

**Frontend feature**

Screen/interaction map, state/data flow diagram, API sequence diagram, error states.
