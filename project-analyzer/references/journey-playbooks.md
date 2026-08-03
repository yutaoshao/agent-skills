# Journey Playbooks

Use this guide to adapt onboarding analysis to the repository in front of you.
Classify by delivered behavior and runtime boundaries, not by directory names.
Combine playbooks for hybrid systems and monorepos.

## Contents

- [Universal Journey Selection](#universal-journey-selection)
- [Responsibility Map](#responsibility-map)
- [User-Facing Application Or Service](#user-facing-application-or-service)
- [CLI Or Developer Tool](#cli-or-developer-tool)
- [Library Or SDK](#library-or-sdk)
- [Data Or ML Pipeline](#data-or-ml-pipeline)
- [Infrastructure Or Automation](#infrastructure-or-automation)
- [Plugin, Skill, Or Extension Collection](#plugin-skill-or-extension-collection)
- [Documentation Or Configuration Repository](#documentation-or-configuration-repository)
- [Monorepo And Hybrid Systems](#monorepo-and-hybrid-systems)

## Universal Journey Selection

Derive candidate journeys from multiple surfaces where available:

- product or user documentation;
- visible application navigation, public APIs, CLI help, or exported APIs;
- executable entry-point registration;
- schemas, migrations, fixtures, examples, and sample data;
- test names and test setup;
- release notes and integration documentation.

Select a normal success path that directly delivers core user value, crosses key
responsibility boundaries, and has enough evidence to trace. Do not default to
login, health checks, installation, configuration, administration, or error
handling merely because those paths are easy to locate.

Record candidates without numeric scoring:

| Candidate journey | User value | Key boundaries | Available evidence | Decision |
|---|---|---|---|---|
| [Concrete journey] | [Outcome] | [Responsibilities crossed] | [Code/test/docs] | Selected / deferred and why |

If no journey clearly dominates, choose the best-supported provisional path,
mark the selection `Inferred`, and list what evidence would change the choice.

## Responsibility Map

Treat a module as a coherent runtime or domain responsibility with an observable
contract. A directory is only a navigation aid.

For every core responsibility, collect:

| Responsibility | Inbound contract | Outbound contract | State owned or transformed | Side effects | State | Evidence |
|---|---|---|---|---|---|---|
| [What it contributes] | [Caller/input/event] | [Call/output/event] | [Data/artifact] | [Network/job/file/etc.] | Verified / Inferred / Unknown / N/A | [Locations/results] |

Corroborate important boundaries from both sides when both are in scope. If a
consumer, provider, or remote service is outside the repository, verify the local
contract and implementation separately, then mark remote use or behavior
`Unknown`. A caller import alone does not prove the callee's runtime behavior, and
a registered handler alone does not prove that a user-facing entry reaches it.

## User-Facing Application Or Service

Possible entry surfaces include UI actions, HTTP or RPC routes, WebSocket events,
mobile intents, background triggers, and scheduled jobs.

Trace:

1. actor action or external trigger;
2. frontend or transport entry;
3. validation, identity, and authorization;
4. orchestration and domain decision;
5. state reads and writes, including transaction boundaries;
6. synchronous and asynchronous integrations;
7. response, rendered state, or notification;
8. focused unit, integration, contract, or end-to-end test.

Do not impose a controller-service-repository sequence when the implementation
uses another shape.

## CLI Or Developer Tool

Possible entry surfaces include executable declarations, command registries,
subcommands, flags, stdin, config files, and environment variables.

Trace:

1. invocation and argument parsing;
2. configuration resolution and validation;
3. command dispatch;
4. core operation;
5. filesystem, process, network, or repository side effects;
6. stdout, stderr, artifacts, and exit status;
7. command-level tests or a side-effect-safe smoke invocation.

Separate a help-path smoke check from evidence that the core command succeeds.

## Library Or SDK

Possible entry surfaces include public exports, constructors, client methods,
protocol implementations, callbacks, and extension interfaces.

Trace:

1. consumer-visible API and inputs;
2. type, schema, or argument validation;
3. internal orchestration;
4. serialization, transport, storage, or platform adapter;
5. returned value, error contract, callbacks, or events;
6. public API tests, compatibility tests, examples, or consumer fixtures.

Treat examples as declared usage until corroborated by implementation or tests.

## Data Or ML Pipeline

Possible entry surfaces include jobs, notebooks promoted to pipelines, schedulers,
dataset registrations, training commands, batch APIs, and stream consumers.

Trace:

1. source dataset or event and trigger;
2. schema validation and preprocessing;
3. transformations, feature computation, training, or inference;
4. orchestration and retry/checkpoint boundaries;
5. intermediate and final artifacts, models, tables, or topics;
6. metrics, lineage, quality gates, and publication;
7. fixture, data-contract, reproducibility, or evaluation tests.

Record data versions and environment assumptions when they affect reproducibility.

## Infrastructure Or Automation

Possible entry surfaces include desired-state configuration, modules, deployment
commands, CI events, policy checks, and operator actions.

Trace:

1. requested configuration change or event;
2. variable and policy validation;
3. module composition or workflow dispatch;
4. plan, diff, or generated artifact;
5. provider or platform operation;
6. state backend, created resources, and rollback boundary;
7. static validation, plan tests, policy tests, or sandbox deployment evidence.

Static infrastructure configuration verifies declared desired state only.
Deployed resources and current drift remain `Unknown` without environment
evidence. Inspect plans before execution: they may access remote state, credentials,
or provider APIs and therefore require authorization under the command-safety
policy. Never run apply, deploy, or destroy operations merely to complete
onboarding.

## Plugin, Skill, Or Extension Collection

Possible entry surfaces include manifests, discovery metadata, trigger descriptions,
commands, hooks, tool registrations, and loader APIs.

Trace:

1. installation or discovery contract;
2. invocation or trigger matching;
3. instruction or handler routing;
4. referenced resources, tools, or adapters loaded;
5. generated artifact, external action, or user-facing result;
6. validation, fixture, or forward-test surface.

For a collection, distinguish repository-level publishing and discovery from one
representative extension's runtime path.

## Documentation Or Configuration Repository

Possible value paths include authoring to rendered documentation, configuration
to generated output, schema changes to consumers, and examples to user adoption.

Trace:

1. author or maintainer input;
2. canonical source and validation rules;
3. transformation, generation, or publishing pipeline;
4. links, artifacts, registries, or downstream consumers;
5. lint, render, schema, or integration verification.

Do not invent an application runtime when the repository delivers reference or
configuration artifacts.

## Monorepo And Hybrid Systems

First map independent deployables, packages, applications, shared libraries, and
their build or workspace relationships. Then choose one user journey and trace
only the packages and services it actually crosses.

Record:

- the selected workspace and why it represents core value;
- package or service boundaries crossed by the journey;
- shared contracts and generated code;
- independent state or deployment ownership;
- excluded workspaces and the consequence of excluding them.

Do not describe a monorepo as one monolith solely because it has one root manifest,
or as microservices solely because it contains several directories or Dockerfiles.
