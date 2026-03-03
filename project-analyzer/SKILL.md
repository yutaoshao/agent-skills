---
name: project-analyzer
description: Analyze and understand unfamiliar codebases when taking over or onboarding to a new project. Use this skill whenever a developer asks to analyze a project, understand a codebase, do a project handover/takeover review, explore an unknown repository, or get up to speed on a new codebase. Also triggers on requests like "what does this project do", "give me an overview of this repo", "help me understand this codebase", or "I just joined this team and need to understand the code".
---

# Project Analyzer

Systematically analyze an unfamiliar codebase and produce a structured report that gets a developer productive fast. Eight modular workflows that can be invoked individually or combined into a full project review.

## Workflow Decision Tree

Determine which workflow(s) to invoke based on the request:

- Request mentions "tech stack", "what technologies", "frameworks used" --> **Module 1: Technology Stack Scan**
- Request mentions "project structure", "directory layout", "how is it organized" --> **Module 2: Project Structure & Entry Points**
- Request mentions "architecture", "design patterns", "how does it work" --> **Module 3: Architecture & Design Patterns**
- Request mentions "dependencies", "packages", "third-party libraries" --> **Module 4: Dependency Analysis**
- Request mentions "code quality", "testing", "linting", "standards" --> **Module 5: Code Quality Assessment**
- Request mentions "CI/CD", "deployment", "workflow", "dev process" --> **Module 6: Development Workflow & Standards**
- Request mentions "risks", "tech debt", "problems", "issues" --> **Module 7: Risk & Technical Debt**
- Request mentions "full analysis", "overview", "onboarding", "understand this project" --> **Module 8: Comprehensive Report** (runs all modules)
- When uncertain, start with Module 8 to provide a complete picture.

---

## Module 1: Technology Stack Scan

Identify every technology, framework, and tool the project relies on. This forms the foundation for all subsequent analysis.

### Procedure

1. Scan the project root for manifest and configuration files to identify the primary stack:
   - **JavaScript/TypeScript**: `package.json`, `tsconfig.json`, `webpack.config.*`, `vite.config.*`, `next.config.*`, `.babelrc`
   - **Python**: `pyproject.toml`, `setup.py`, `setup.cfg`, `requirements*.txt`, `Pipfile`, `poetry.lock`, `tox.ini`
   - **Rust**: `Cargo.toml`, `rust-toolchain.toml`
   - **Go**: `go.mod`, `go.sum`
   - **Java/Kotlin**: `pom.xml`, `build.gradle`, `build.gradle.kts`
   - **Ruby**: `Gemfile`, `Rakefile`
   - **C/C++**: `CMakeLists.txt`, `Makefile`, `meson.build`, `conanfile.txt`
   - **Swift**: `Package.swift`, `*.xcodeproj`
   - **.NET**: `*.csproj`, `*.sln`, `global.json`
   - **PHP**: `composer.json`
   - **Dart/Flutter**: `pubspec.yaml`
2. Identify framework-specific markers:
   - **Frontend**: React (`jsx/tsx` files, `react-dom`), Vue (`.vue` files), Angular (`angular.json`), Svelte (`.svelte` files), Next.js, Nuxt, Remix
   - **Backend**: Express, FastAPI, Django, Flask, Spring Boot, Gin, Actix, Rails, Laravel, NestJS
   - **Mobile**: React Native, Flutter, SwiftUI, Jetpack Compose
   - **Desktop**: Electron, Tauri, Qt, WPF
3. Detect infrastructure and tooling:
   - **Containerization**: `Dockerfile`, `docker-compose.yml`, `.dockerignore`
   - **IaC**: Terraform (`.tf`), Pulumi, CloudFormation, Ansible
   - **CI/CD**: `.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`, `.circleci/`
   - **Database**: Migration files, schema files, ORM configurations
   - **Monorepo tools**: Turborepo (`turbo.json`), Nx (`nx.json`), Lerna, pnpm workspaces
4. Check runtime version constraints: `.node-version`, `.nvmrc`, `.python-version`, `.tool-versions`, `.ruby-version`, `rust-toolchain.toml`.
5. Produce a concise tech stack summary table.

### Output Format

```
| Layer        | Technology        | Version   | Config File          |
|-------------|-------------------|-----------|---------------------|
| Language     | TypeScript        | 5.3       | tsconfig.json       |
| Framework    | Next.js           | 14.x      | next.config.js      |
| Runtime      | Node.js           | >=18      | .nvmrc              |
| Database     | PostgreSQL        | 15        | docker-compose.yml  |
| ORM          | Prisma            | 5.x       | schema.prisma       |
| Styling      | Tailwind CSS      | 3.4       | tailwind.config.js  |
| Testing      | Jest + RTL        | 29.x      | jest.config.js      |
| CI/CD        | GitHub Actions    | -         | .github/workflows/  |
```

---

## Module 2: Project Structure & Entry Points

Map the directory layout, identify architectural boundaries, and locate the key entry points a developer needs to start navigating the code.

### Procedure

1. Generate a high-level directory tree (depth 2-3, excluding `node_modules`, `.git`, `__pycache__`, `dist`, `build`, `vendor`, `.next`, `target` and similar build artifacts).
2. Classify top-level directories by role:
   - **Source code**: `src/`, `lib/`, `app/`, `packages/`, `internal/`, `cmd/`
   - **Tests**: `test/`, `tests/`, `__tests__/`, `spec/`, `e2e/`
   - **Configuration**: Root-level config files, `.env.example`
   - **Documentation**: `docs/`, `doc/`, `wiki/`, `README*`
   - **Build/Output**: `dist/`, `build/`, `out/`, `target/`
   - **Assets/Static**: `public/`, `static/`, `assets/`
   - **Scripts/Tools**: `scripts/`, `tools/`, `bin/`
3. Identify application entry points:
   - **Main entry**: `main.ts`, `index.ts`, `app.py`, `main.go`, `Main.java`, `Program.cs`, `main.rs`
   - **Server bootstrap**: Express `app.listen`, FastAPI `uvicorn.run`, Spring `@SpringBootApplication`
   - **CLI entry**: `bin/` scripts, `__main__.py`, cobra commands
   - **Route definitions**: Router files, controller directories, API route folders
   - **Configuration entry**: Where environment variables are loaded, config initialization
4. Identify module boundaries: Look for clear package/module separations that indicate domain boundaries.
5. Count lines of code by language (use `cloc` or `tokei` if available, otherwise estimate from file counts and average sizes).

### Key Questions to Answer

- Where does execution start?
- Where are routes/endpoints defined?
- Where is configuration loaded?
- What are the domain boundaries?
- Where do I add new features?

---

## Module 3: Architecture & Design Patterns

Understand the high-level architecture and recurring design patterns used throughout the codebase.

### Procedure

1. Load `references/architecture-patterns.md` for the pattern catalog.
2. Determine the overall architectural style:
   - **Monolith**: Single deployable unit, shared database
   - **Microservices**: Multiple services, independent deployments, service discovery
   - **Modular monolith**: Single deployment but strong module boundaries
   - **Serverless**: Lambda/Cloud Functions, event-driven
   - **Monorepo with packages**: Shared repository, independent packages
3. Identify the layering strategy:
   - **MVC/MVP/MVVM**: Model-View-Controller variants
   - **Clean Architecture / Hexagonal**: Domain core with ports and adapters
   - **3-Tier**: Presentation → Business Logic → Data Access
   - **Event-driven**: Event bus, message queues, pub/sub
   - **CQRS**: Separated read/write paths
4. Map the data flow:
   a. Trace a typical request from entry point to response (e.g., HTTP request → middleware → controller → service → repository → database → response).
   b. Identify cross-cutting concerns: authentication, logging, error handling, caching.
   c. Document how state is managed (Redux, Zustand, Context, server state, etc.).
5. Identify recurring code patterns:
   - **Dependency Injection**: Constructor injection, service containers, IoC
   - **Repository pattern**: Data access abstraction
   - **Factory/Builder**: Object creation patterns
   - **Observer/Event**: Event emitters, hooks, listeners
   - **Middleware/Pipeline**: Request processing chains
   - **Strategy**: Pluggable algorithms or behaviors
6. Document API surface:
   - REST endpoints (scan route files)
   - GraphQL schema (if present)
   - gRPC proto files (if present)
   - WebSocket handlers
   - Background job definitions

### Output Format

Produce an architecture diagram description (textual) showing:
- Major components and their responsibilities
- Data flow direction
- External service integrations
- Database connections

---

## Module 4: Dependency Analysis

Evaluate third-party dependencies for health, security, and maintainability.

### Procedure

1. Parse the primary manifest file(s) and separate:
   - **Core dependencies**: Required at runtime
   - **Dev dependencies**: Build tools, test frameworks, linters
   - **Peer dependencies**: Expected to be provided by the consumer
   - **Optional dependencies**: Feature-gated extras
2. Identify high-impact dependencies -- libraries that the project is deeply coupled to:
   - ORM/database drivers
   - Web framework
   - Authentication libraries
   - UI component libraries
   - State management
3. Check for dependency health signals:
   - **Lock file present**: `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `Pipfile.lock`, `poetry.lock`, `Cargo.lock`, `go.sum`
   - **Version pinning strategy**: Exact versions, ranges, or latest
   - **Last update**: Check lock file modification date as a proxy for update frequency
4. Flag potential concerns:
   - Deprecated packages (look for deprecation notices in package metadata)
   - Duplicate functionality (two packages doing the same thing, e.g., `moment` + `dayjs`)
   - Unusually large dependency trees for simple tasks
   - Dependencies with known security implications (check for `audit` scripts or `.nsprc`)
5. Map internal dependencies for monorepos:
   - Which packages depend on which other packages
   - Circular dependency detection
   - Shared vs. isolated dependencies

### Output Format

```
## Core Dependencies (X total)
| Package       | Version | Purpose              | Health  |
|--------------|---------|---------------------|---------|
| next          | 14.1.0  | Web framework       | Active  |
| prisma        | 5.8.0   | ORM                 | Active  |
| lodash        | 4.17.21 | Utility library     | Stable  |

## Concerns
- [WARN] `moment` (2.29.4) -- deprecated, consider migrating to `dayjs` or `date-fns`
- [INFO] No lock file found -- dependency versions may vary across installs
```

---

## Module 5: Code Quality Assessment

Evaluate code quality infrastructure, testing practices, and documentation coverage.

### Procedure

1. Load `references/analysis-checklist.md` for the comprehensive quality checklist.
2. Check formatting and linting setup:
   - **Formatter**: Prettier (`.prettierrc`), Black (`pyproject.toml [tool.black]`), rustfmt, gofmt
   - **Linter**: ESLint (`.eslintrc*`), Pylint/Ruff/Flake8, Clippy, golangci-lint
   - **Type checking**: TypeScript strict mode, mypy, pyright
   - **Pre-commit hooks**: `.husky/`, `.pre-commit-config.yaml`, `lint-staged`
   - **Editor config**: `.editorconfig`, VS Code settings
3. Assess testing practices:
   - **Test framework**: Jest, Vitest, pytest, Go testing, JUnit, RSpec
   - **Test types present**: Unit tests, integration tests, E2E tests (Playwright, Cypress, Selenium)
   - **Test organization**: Co-located vs. separate test directory
   - **Coverage configuration**: Coverage thresholds, reporters
   - **Test helpers/fixtures**: Factories, mocks, test utilities
   - Estimate test-to-source ratio (number of test files vs. source files).
4. Evaluate documentation:
   - **README quality**: Setup instructions, architecture overview, contribution guide
   - **Inline documentation**: JSDoc/docstrings coverage on exported functions
   - **API documentation**: Swagger/OpenAPI, generated docs
   - **ADRs**: Architecture Decision Records in `docs/adr/` or similar
   - **Changelog**: `CHANGELOG.md`, release notes
5. Scan for code complexity indicators:
   - Files exceeding 500 lines (potential god objects)
   - Functions exceeding 50 lines (potential complexity)
   - Deeply nested directory structures (>5 levels)
   - Unusually large files that may need splitting

### Quality Summary Format

```
| Aspect          | Status | Details                          |
|----------------|--------|----------------------------------|
| Formatter       | OK     | Prettier configured              |
| Linter          | OK     | ESLint with strict rules         |
| Type Safety     | WARN   | TypeScript strict mode OFF       |
| Unit Tests      | OK     | Jest, 120 test files             |
| E2E Tests       | MISS   | No E2E test framework found      |
| Pre-commit      | OK     | Husky + lint-staged              |
| Documentation   | WARN   | README exists, no API docs       |
```

---

## Module 6: Development Workflow & Standards

Understand how the team develops, builds, deploys, and collaborates.

### Procedure

1. Analyze CI/CD configuration:
   - Pipeline stages (lint, test, build, deploy)
   - Deployment targets (staging, production)
   - Environment-specific configurations
   - Secret management approach
2. Examine Git workflow:
   - **Branching strategy**: Check branch names in `.git/refs/heads/` and CI config for patterns (GitFlow, trunk-based, feature branches)
   - **Commit conventions**: Check for Conventional Commits patterns in recent history, commitlint config
   - **PR templates**: `.github/PULL_REQUEST_TEMPLATE.md`
   - **Issue templates**: `.github/ISSUE_TEMPLATE/`
   - **Branch protection hints**: Required checks in CI config
3. Identify build and run commands:
   - Parse `scripts` section of `package.json`, `Makefile` targets, `Taskfile.yml`, `justfile`
   - Document: How to install dependencies, run dev server, run tests, build for production
   - Note any required environment variables (from `.env.example` or documentation)
4. Check for development standards documentation:
   - `CONTRIBUTING.md`
   - Code review guidelines
   - Style guide references
   - ADR (Architecture Decision Records)
5. Identify environment setup requirements:
   - Required system dependencies
   - Database setup steps
   - External service dependencies (APIs, message queues, caches)
   - Docker-based development (`docker-compose.yml` for local dev)

### Output: Quick Start Card

```
## Developer Quick Start
1. Prerequisites: Node.js 18+, PostgreSQL 15, Redis
2. Install: `pnpm install`
3. Configure: `cp .env.example .env` then fill in values
4. Database: `pnpm db:migrate && pnpm db:seed`
5. Run: `pnpm dev` (starts at http://localhost:3000)
6. Test: `pnpm test` (unit) / `pnpm test:e2e` (E2E)
7. Build: `pnpm build`
```

---

## Module 7: Risk & Technical Debt

Identify risks, technical debt, and areas that need attention before making changes.

### Procedure

1. Search for debt markers in the codebase:
   - `TODO`, `FIXME`, `HACK`, `XXX`, `WORKAROUND`, `TEMP`, `DEPRECATED`
   - Count occurrences and identify clusters (files/directories with high concentrations signal problematic areas).
2. Identify code smells:
   - **God objects/files**: Files >500 lines that centralize too much logic
   - **Dead code**: Unreachable functions, commented-out blocks, unused exports
   - **Copy-paste duplication**: Similar code blocks across multiple files
   - **Magic numbers/strings**: Hardcoded values without named constants
   - **Inconsistent patterns**: Mixed approaches for the same concern (e.g., some API calls use fetch, others use axios)
3. Assess security posture:
   - **Secret management**: Any hardcoded secrets, API keys, or credentials in source (search for patterns like `password =`, `api_key =`, `secret =`, base64-encoded strings)
   - **Input validation**: Check API endpoints for validation middleware
   - **Authentication/Authorization**: Review auth middleware, role checks
   - **CORS configuration**: Check for overly permissive settings
   - **Dependency vulnerabilities**: Check for `npm audit`, `pip audit`, or similar in CI
4. Evaluate upgrade risks:
   - Framework version vs. latest stable (how far behind?)
   - Language version vs. latest LTS
   - Deprecated API usage within dependencies
5. Identify architectural risks:
   - Tight coupling between modules
   - Missing abstraction layers (direct database queries in route handlers)
   - Single points of failure
   - Missing error handling or catch-all error swallowing

### Output: Risk Matrix

```
| Risk                              | Severity | Category    | Location              |
|----------------------------------|----------|-------------|----------------------|
| Hardcoded DB password            | HIGH     | Security    | src/config/db.ts:15  |
| No input validation on /api/user | HIGH     | Security    | src/routes/user.ts   |
| 47 TODO comments in core module  | MEDIUM   | Tech Debt   | src/core/             |
| React 17 (latest is 19)         | MEDIUM   | Upgrade     | package.json         |
| No E2E tests                    | MEDIUM   | Testing     | -                    |
| God file: utils.ts (1200 lines) | LOW      | Complexity  | src/utils/utils.ts   |
```

---

## Module 8: Comprehensive Report

Full project analysis combining all modules into a single onboarding document. This is the default when a developer says "help me understand this project".

### Procedure

1. Run Modules 1-7 in sequence.
2. Load `references/report-template.md` for the report structure.
3. Synthesize findings into a structured report with these sections:
   - **Executive Summary**: 3-5 sentences covering what the project does, its tech stack, and overall health.
   - **Technology Stack**: Output from Module 1.
   - **Project Map**: Structure and entry points from Module 2.
   - **Architecture Overview**: Patterns and data flow from Module 3.
   - **Dependency Health**: Key findings from Module 4.
   - **Quality Snapshot**: Summary from Module 5.
   - **Developer Onboarding**: Quick start card from Module 6.
   - **Risk Register**: Priority-sorted findings from Module 7.
   - **Recommended First Steps**: 5-10 prioritized actions for the new developer, ordered by impact:
     1. Critical security issues to fix immediately
     2. Development environment setup blockers
     3. Key documentation to read
     4. Areas to avoid modifying until better understood
     5. Quick wins to build familiarity with the codebase

### Quality Criteria

- Report is actionable -- every finding includes a specific location and suggested action
- Risks are sorted by severity, not by discovery order
- The onboarding section alone should let a developer run the project locally within 15 minutes
- No vague statements like "code quality could be improved" -- always specify what and where

---

## Reference Files

- `references/analysis-checklist.md` -- 100+ item checklist organized by analysis phase. Load when executing Module 5 or Module 8 for systematic quality assessment.
- `references/architecture-patterns.md` -- Catalog of common architecture and design patterns with identification heuristics (file structure signatures, naming conventions, code patterns). Load when executing Module 3.
- `references/report-template.md` -- Markdown template for the comprehensive report with section headers, placeholder descriptions, and formatting guidelines. Load when executing Module 8.
