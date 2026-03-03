# Project Analysis Checklist

A systematic checklist for evaluating an unfamiliar codebase. Work through each section in order; check items that are present and note items that are missing.

---

## 1. Repository Basics

- [ ] README.md exists and is up to date
- [ ] LICENSE file present
- [ ] .gitignore configured properly
- [ ] No sensitive files committed (.env, credentials, private keys)
- [ ] Repository size is reasonable (no large binaries in git history)
- [ ] Branch naming convention is consistent
- [ ] Recent commit activity (not abandoned)

## 2. Technology Stack

- [ ] Primary language(s) identified
- [ ] Framework(s) identified with version
- [ ] Runtime version specified (.nvmrc, .python-version, etc.)
- [ ] Package manager identified (npm/yarn/pnpm/pip/cargo/go mod)
- [ ] Build tool identified (webpack/vite/esbuild/rollup/etc.)
- [ ] Database technology identified
- [ ] Caching layer identified (if applicable)
- [ ] Message queue/event system identified (if applicable)

## 3. Project Structure

- [ ] Clear separation of concerns in directory layout
- [ ] Source code directory identified
- [ ] Test directory identified
- [ ] Configuration directory identified
- [ ] Static assets directory identified
- [ ] Entry point(s) located
- [ ] Route/endpoint definitions located
- [ ] Database schema/migrations located
- [ ] No deeply nested directories (>5 levels)

## 4. Dependency Management

- [ ] Lock file present and committed
- [ ] Dependencies are version-pinned or range-locked
- [ ] No deprecated packages in use
- [ ] No duplicate-purpose packages
- [ ] Dev dependencies separated from production dependencies
- [ ] No unused dependencies
- [ ] Security audit passes (npm audit / pip audit)

## 5. Code Quality - Formatting & Linting

- [ ] Code formatter configured (Prettier, Black, gofmt, rustfmt)
- [ ] Linter configured (ESLint, Pylint/Ruff, Clippy, golangci-lint)
- [ ] Editor config present (.editorconfig)
- [ ] Pre-commit hooks configured (Husky, pre-commit)
- [ ] Consistent code style across the codebase
- [ ] No linter disable comments without justification

## 6. Code Quality - Type Safety

- [ ] Type system in use (TypeScript, mypy, type hints)
- [ ] Strict mode enabled (if applicable)
- [ ] No excessive use of `any` / `object` / `type: ignore`
- [ ] API boundaries have explicit type definitions
- [ ] Shared types/interfaces are centralized

## 7. Testing

- [ ] Test framework configured
- [ ] Unit tests present
- [ ] Integration tests present
- [ ] E2E tests present (if applicable)
- [ ] Test coverage configured and measured
- [ ] Test coverage threshold set (if applicable)
- [ ] Tests pass on current main branch
- [ ] Test fixtures/factories/helpers organized
- [ ] No flaky tests (check CI history if available)
- [ ] Critical business logic has test coverage

## 8. Documentation

- [ ] README contains project description
- [ ] README contains setup/installation instructions
- [ ] README contains development workflow
- [ ] Architecture documentation exists (ADRs, diagrams)
- [ ] API documentation exists (Swagger/OpenAPI, generated docs)
- [ ] Inline documentation on complex functions
- [ ] CONTRIBUTING.md exists
- [ ] CHANGELOG.md exists
- [ ] Environment variables documented (.env.example)

## 9. CI/CD

- [ ] CI pipeline configured
- [ ] CI runs linting
- [ ] CI runs tests
- [ ] CI runs type checking
- [ ] CI runs security audit
- [ ] Build step configured
- [ ] Deployment pipeline configured
- [ ] Environment-specific configurations exist
- [ ] Secrets managed properly (not in repo)

## 10. Git Workflow

- [ ] Branching strategy identifiable
- [ ] Commit message convention followed
- [ ] PR/MR template exists
- [ ] Issue template exists
- [ ] Code review process evident (PR comments, approvals)
- [ ] Release process documented or evident

## 11. Security

- [ ] No hardcoded secrets in source code
- [ ] Environment variables used for sensitive configuration
- [ ] Input validation on API endpoints
- [ ] Authentication mechanism in place
- [ ] Authorization/role-based access control present
- [ ] CORS configured appropriately
- [ ] Rate limiting configured (if public API)
- [ ] SQL injection prevention (parameterized queries, ORM)
- [ ] XSS prevention measures (if web frontend)
- [ ] CSRF protection (if applicable)
- [ ] Dependencies scanned for vulnerabilities

## 12. Error Handling

- [ ] Global error handler configured
- [ ] API endpoints return consistent error format
- [ ] Errors are logged (not swallowed silently)
- [ ] User-facing error messages are informative
- [ ] No catch-all empty catch blocks
- [ ] Async errors handled properly (no unhandled promise rejections)
- [ ] Graceful shutdown implemented

## 13. Performance & Scalability

- [ ] Database queries are indexed (check migration files)
- [ ] N+1 query prevention (eager loading, data loaders)
- [ ] Pagination implemented for list endpoints
- [ ] Caching strategy in place (if applicable)
- [ ] Static assets optimized (compression, CDN)
- [ ] Bundle size considered (if frontend)
- [ ] No synchronous blocking operations in async contexts

## 14. Observability

- [ ] Logging framework configured
- [ ] Log levels used appropriately
- [ ] Request/response logging for APIs
- [ ] Error tracking service integrated (Sentry, Datadog, etc.)
- [ ] Health check endpoint exists
- [ ] Metrics collection configured (if applicable)
- [ ] Distributed tracing (if microservices)
