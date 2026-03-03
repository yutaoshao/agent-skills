# Architecture Patterns Catalog

A reference for identifying common architecture and design patterns in unfamiliar codebases. Each pattern includes file structure signatures, naming conventions, and code-level indicators.

---

## 1. Architectural Styles

### 1.1 Monolith

**Signatures:**
- Single `package.json` / `pom.xml` / `go.mod` at root
- One `Dockerfile` producing one deployable artifact
- Shared database configuration (single connection string)
- All features in one `src/` directory

**Directory pattern:**
```
src/
├── controllers/    (or routes/, handlers/)
├── services/       (or business/, domain/)
├── models/         (or entities/, schemas/)
├── middleware/
├── utils/          (or helpers/, lib/)
└── config/
```

### 1.2 Modular Monolith

**Signatures:**
- Single deployment, but code organized by business domain
- Each module has its own models, services, controllers
- Module-level `index.ts` or `__init__.py` that exports a public API
- Inter-module communication via explicit interfaces, not direct imports

**Directory pattern:**
```
src/
├── modules/
│   ├── auth/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── models/
│   │   └── index.ts        # Public API
│   ├── billing/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── models/
│   │   └── index.ts
│   └── notifications/
└── shared/                  # Cross-cutting concerns
```

### 1.3 Microservices

**Signatures:**
- Multiple `Dockerfile` files or `docker-compose.yml` with many services
- Separate package manifests per service
- API gateway or service mesh configuration
- Message broker config (RabbitMQ, Kafka, NATS)
- Service discovery configuration
- Each service has its own database connection

**Directory pattern:**
```
services/
├── user-service/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── order-service/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── api-gateway/
└── docker-compose.yml
```

### 1.4 Monorepo (Multi-package)

**Signatures:**
- `packages/` or `apps/` directory with multiple sub-projects
- Workspace configuration (`pnpm-workspace.yaml`, `lerna.json`, `turbo.json`, `nx.json`)
- Shared packages referenced as workspace dependencies
- Root-level tooling config with per-package overrides

**Directory pattern:**
```
packages/
├── web/              # Frontend app
├── api/              # Backend API
├── shared/           # Shared utilities
├── ui/               # Component library
└── config/           # Shared configurations
turbo.json            # or nx.json
pnpm-workspace.yaml
```

### 1.5 Serverless

**Signatures:**
- `serverless.yml`, `template.yaml` (SAM), or `cdk.ts` / `cdk.py`
- Function-per-file organization
- Event source mappings (API Gateway, S3, SQS triggers)
- No long-running server process
- Cold start optimization patterns

**Directory pattern:**
```
functions/
├── createUser/
│   ├── handler.ts
│   └── event.json
├── processOrder/
│   ├── handler.ts
│   └── event.json
serverless.yml
```

---

## 2. Layering Patterns

### 2.1 MVC (Model-View-Controller)

**Identification:**
- Directories named `models/`, `views/`, `controllers/` (or `templates/`, `handlers/`)
- Controller files import from model files
- View templates reference model data
- Common in: Rails, Django, Spring MVC, Laravel, Express

**Code indicators:**
```
// Controller imports model
import { User } from '../models/User';
// Controller renders view
res.render('users/index', { users });
```

### 2.2 Clean Architecture / Hexagonal (Ports & Adapters)

**Identification:**
- Directories named `domain/`, `application/`, `infrastructure/`, `adapters/`, `ports/`
- Domain layer has zero external imports (no framework, no ORM)
- Repository interfaces defined in domain, implemented in infrastructure
- Use case classes with single `execute()` method

**Directory pattern:**
```
src/
├── domain/
│   ├── entities/
│   ├── repositories/    # Interfaces only
│   └── value-objects/
├── application/
│   ├── use-cases/
│   └── services/
├── infrastructure/
│   ├── database/        # Repository implementations
│   ├── http/
│   └── messaging/
└── adapters/
    ├── controllers/
    └── presenters/
```

### 2.3 CQRS (Command Query Responsibility Segregation)

**Identification:**
- Separate `commands/` and `queries/` directories
- Different models for read and write operations
- Command handlers and query handlers as distinct classes
- Often paired with Event Sourcing

**Code indicators:**
- Classes named `*Command`, `*Query`, `*CommandHandler`, `*QueryHandler`
- Separate read models / projections

### 2.4 Event-Driven Architecture

**Identification:**
- Event emitters, event bus, or message broker integration
- Files named `*Event`, `*Listener`, `*Subscriber`, `*Handler`
- Event schema definitions (Avro, Protobuf, JSON Schema)
- Dead letter queue configuration

**Code indicators:**
```
// Event definition
class OrderCreatedEvent { ... }
// Event handler
@EventHandler(OrderCreatedEvent)
class SendConfirmationEmail { ... }
```

---

## 3. Common Design Patterns

### 3.1 Repository Pattern

**Identification:**
- Files named `*Repository`, `*Repo`, `*Store`, `*DAO`
- Interface defining CRUD operations
- Implementation wrapping ORM or database client
- Services import repositories, not ORM directly

### 3.2 Dependency Injection

**Identification:**
- Constructor parameters for dependencies (not direct imports)
- IoC container configuration (`inversify`, `tsyringe`, Spring `@Autowired`, Nest `@Injectable()`)
- Module files that wire dependencies together
- Factory functions that accept dependencies as parameters

### 3.3 Middleware / Pipeline Pattern

**Identification:**
- Chained function calls (`app.use(...)`)
- Files in `middleware/` directory
- Decorator patterns (`@UseGuard()`, `@Middleware()`)
- Pipe-like composition of request handlers

### 3.4 Strategy Pattern

**Identification:**
- Interface with multiple implementations selected at runtime
- Configuration-driven behavior switching
- Factory that returns different implementations based on input
- Example: payment processors, notification channels, export formats

### 3.5 Observer / Pub-Sub

**Identification:**
- EventEmitter usage
- `on()` / `emit()` patterns
- Webhook registrations
- React-like hooks system

### 3.6 Facade Pattern

**Identification:**
- Single class/module that simplifies a complex subsystem
- `index.ts` / `__init__.py` that re-exports a clean API
- Service classes that orchestrate multiple lower-level operations
- SDK or client libraries wrapping complex APIs

---

## 4. Frontend-Specific Patterns

### 4.1 Component Architecture (React/Vue/Svelte)

**Identification:**
- Components organized by feature or by type
- Shared UI components in `components/ui/` or `components/common/`
- Page components in `pages/` or `views/`
- Layout components wrapping page content

### 4.2 State Management Patterns

| Pattern | Signatures |
|---------|-----------|
| Redux / Zustand | `store/`, `slices/`, `reducers/`, `actions/` |
| Context + Hooks | `contexts/`, `providers/`, `useX` custom hooks |
| Server State | React Query / SWR / TanStack Query usage |
| Atomic State | Jotai (`atoms/`), Recoil (`selectors/`) |

### 4.3 API Layer Patterns

| Pattern | Signatures |
|---------|-----------|
| Service Layer | `services/api.ts`, `services/userService.ts` |
| API Client | `lib/api-client.ts` with axios/fetch wrapper |
| Generated Client | OpenAPI codegen, tRPC, GraphQL codegen |
| Hook-based | `hooks/useUsers.ts` wrapping data fetching |

---

## 5. API Design Patterns

### 5.1 RESTful API

**Identification:**
- Resource-based URL patterns (`/users`, `/users/:id`, `/users/:id/orders`)
- HTTP method semantics (GET, POST, PUT, PATCH, DELETE)
- Status code conventions
- HATEOAS links (rare but distinctive)

### 5.2 GraphQL

**Identification:**
- `.graphql` or `.gql` schema files
- Resolver directories
- Single `/graphql` endpoint
- Type definitions with Query/Mutation/Subscription

### 5.3 gRPC

**Identification:**
- `.proto` files with service and message definitions
- Generated client/server stubs
- Binary protocol configuration

### 5.4 tRPC

**Identification:**
- Router definitions with `publicProcedure` / `protectedProcedure`
- End-to-end type safety without schema files
- Shared types between client and server
