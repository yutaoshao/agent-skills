# Architecture Pattern Vocabulary

Use this catalog only after mapping concrete responsibilities and one real
journey. Pattern names summarize observed relationships; they do not prove them.

## Contents

- [Evidence Guardrails](#evidence-guardrails)
- [Describe Independent Dimensions](#describe-independent-dimensions)
- [Delivery Topologies](#delivery-topologies)
- [Runtime Interaction Styles](#runtime-interaction-styles)
- [Code Organization Patterns](#code-organization-patterns)
- [Recurring Design Patterns](#recurring-design-patterns)
- [Interface Patterns](#interface-patterns)
- [Reporting Language](#reporting-language)

## Evidence Guardrails

Directory names, manifests, Dockerfiles, decorators, and naming conventions are
candidate signals. Before assigning a pattern label, corroborate it with evidence
appropriate to the claim:

- composition or bootstrap wiring;
- actual dependency direction;
- runtime calls, events, jobs, or library consumers;
- deployment units and release configuration;
- data and state ownership;
- both sides of a public boundary when both are in scope; otherwise separate the
  verified local contract from unknown remote consumption or behavior;
- the representative journey traced in the onboarding report.

Allow multiple patterns by component. A monorepo can contain a modular monolith,
several services, shared libraries, and scheduled jobs at the same time.

Use this component map before applying labels:

| Component | Responsibility | Public boundary | Collaborators | Owned state | State | Evidence |
|---|---|---|---|---|---|---|
| [Observed component] | [What it contributes] | [API/event/export/etc.] | [Concrete relationships] | [DB/cache/file/artifact/etc.] | Verified / Inferred / Unknown | [Locations] |

## Describe Independent Dimensions

Do not collapse these dimensions into one architecture label:

| Dimension | Examples | Evidence to inspect |
|---|---|---|
| Repository topology | Single package, workspace, nested projects | Manifests, workspace config, package boundaries |
| Delivery topology | Library, one deployable, several deployables, functions, jobs, static site | Build and deployment configuration, artifacts, release workflow |
| Runtime interaction | Request-response, command, library call, event, stream, batch DAG | Entry registrations, call sites, schemas, consumers, orchestrators |
| Code organization | Layered, feature-oriented, ports and adapters, component tree, pipeline | Imports, interfaces, composition, representative flow |
| State ownership | Process, browser, database, cache, filesystem, remote service, artifact or IaC state | Read/write sites, schemas, clients, transaction or ownership boundaries |

## Delivery Topologies

### Single Deployable

Candidate signals include one build artifact or one deployed process. A single
manifest or `src/` directory is not enough.

Required corroboration:

- build or packaging output;
- deployment or startup configuration;
- runtime composition showing the relevant components in one unit.

Counterevidence includes independently released packages, separately deployed
workers, functions, or services.

### Modular Monolith

Candidate signals include one deployable with domain responsibilities exposed
through explicit internal contracts.

Required corroboration:

- one delivery unit;
- demonstrated module boundaries and dependency direction;
- controlled cross-module access or public internal interfaces.

Do not conclude this from a `modules/` directory or barrel exports alone.

### Multiple Services Or Deployables

Candidate signals include independently built or released processes, services,
workers, or applications.

Required corroboration:

- independent startup or deployment units;
- network, event, or artifact contracts between units;
- data ownership or operational independence where claimed.

Several Dockerfiles or package directories can also be build tooling, examples,
or one coordinated deployment, so they are not sufficient proof of microservices.

### Functions, Jobs, Or Serverless Units

Candidate signals include registered event sources, scheduled jobs, handlers, or
function deployment definitions.

Required corroboration:

- trigger-to-handler mapping;
- deployed or packaged unit boundaries;
- state, retry, and downstream integration behavior.

## Runtime Interaction Styles

| Style | Candidate signals | Required corroboration |
|---|---|---|
| Request-response | Routes, controllers, RPC handlers | Registered entry, handler path, returned response |
| Command | Executables, subcommands, handlers | Executable declaration, dispatch, exit or artifact behavior |
| Library call | Public exports, client methods, interfaces | Canonical export and implementation verify the local static contract; a consumer, public API test, or execution is needed for usage or runtime claims |
| Event-driven | Publishers, brokers, handlers, event schemas | Publisher-to-topic and topic-to-consumer wiring; delivery semantics when claimed |
| Stream processing | Sources, operators, sinks, checkpoints | Connected topology, state/checkpoint ownership, sink behavior |
| Batch or DAG | Schedules, tasks, dependencies, artifacts | Orchestrator wiring, task inputs/outputs, retry or checkpoint behavior |

## Code Organization Patterns

### Layered Or MVC-Like

Candidate signals include presentation, controller, service, domain, and data
access responsibilities with directional calls.

Corroborate the actual dependency direction and journey. Similar directory names
do not establish a layered architecture, and direct calls are not automatically a
defect.

### Feature Or Domain-Oriented

Candidate signals include code grouped around business capabilities with local
handlers, logic, data, and tests.

Corroborate public boundaries, consumers, state ownership, and how cross-feature
collaboration occurs.

### Ports And Adapters

Candidate signals include domain-facing interfaces implemented by infrastructure
adapters and composed at an outer boundary.

Corroborate that dependency direction points toward the domain and that concrete
framework or transport code stays outside the claimed core. Names such as
`domain/`, `ports/`, or `adapters/` are not sufficient.

### Pipeline

Candidate signals include ordered transformations, middleware, compiler passes,
data stages, or processing chains.

Corroborate ordering, intermediate representation or data contracts, termination,
and error propagation.

### Component And State Architecture

Candidate signals include UI components, stores, providers, hooks, view models,
or reactive state primitives.

Corroborate where state is owned, how updates flow, which components consume it,
and how server or persistent state differs from local presentation state.

## Recurring Design Patterns

| Pattern | Candidate signals | Required corroboration |
|---|---|---|
| Dependency injection | Constructor parameters, providers, containers, wiring functions | Composition chooses concrete implementations and consumers receive them through the claimed boundary |
| Repository or DAO | `Repository`, `Store`, or DAO interfaces | Consumer uses the abstraction and implementation owns data access |
| Middleware or pipeline | Registered ordered handlers, filters, interceptors | Runtime registration and next-step/error semantics |
| Strategy | Shared behavior contract with selectable implementations | Selection point and at least two meaningful implementations |
| Observer or pub-sub | Subscribe/publish APIs, listeners, hooks | Publisher, registration, consumer, and delivery boundary |
| Factory or builder | Centralized object construction | Real call sites use it to vary or constrain construction |
| Facade | Small public surface over several collaborators | Consumers rely on the facade and it coordinates the underlying subsystem |

Do not list every pattern-shaped class. Include only patterns that clarify the
selected journey or an important change boundary.

## Interface Patterns

| Interface | Candidate signals | Verify |
|---|---|---|
| REST-like HTTP | Resource routes and HTTP methods | Route registration, handler, status and payload behavior |
| GraphQL | Schema, resolvers, operations | Schema-to-resolver wiring and selected operation path |
| gRPC | Service definitions and generated stubs | Registered implementation and caller or contract test |
| Message contract | Topic/queue names and schemas | Verify each local publisher or consumer separately; remote delivery, compatibility, and handling remain `Unknown` without external evidence |
| Plugin contract | Manifest, hook, command, or extension interface | Discovery, registration, invocation, and host interaction |
| Package API | Export map, public header, module interface | Canonical export plus implementation verify the local static API; consumer use and compatibility require separate evidence |

## Reporting Language

Prefer bounded statements:

- "The selected journey is implemented as request-response across these three
  observed components."
- "The billing package appears domain-oriented (`Inferred`) because these public
  interfaces have two consumers; deployment independence was not checked."
- "The repository is a workspace; delivery topology remains `Unknown` because
  deployment configuration was outside scope."

Avoid statements such as "this is microservices" or "this follows Clean
Architecture" unless the exact scope and corroborating dimensions are stated.
