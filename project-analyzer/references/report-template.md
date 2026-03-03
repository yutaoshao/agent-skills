# Project Analysis Report Template

Use this template when generating a comprehensive report (Module 8). Fill in each section with findings from the corresponding module. Remove sections that are not applicable.

---

# Project Analysis Report: [Project Name]

**Analyzed by:** Claude Project Analyzer
**Date:** [YYYY-MM-DD]
**Repository:** [path or URL]
**Branch:** [branch name]

---

## Executive Summary

[3-5 sentences: What does the project do? What is the tech stack? What is the overall health assessment? What are the top priorities for the new developer?]

**Overall Health: [GOOD / FAIR / NEEDS ATTENTION]**

---

## 1. Technology Stack

| Layer | Technology | Version | Config File |
|-------|-----------|---------|-------------|
| Language | | | |
| Framework | | | |
| Runtime | | | |
| Database | | | |
| ORM | | | |
| Styling | | | |
| Testing | | | |
| CI/CD | | | |
| Containerization | | | |

**Key observations:**
- [Notable technology choices or version concerns]

---

## 2. Project Map

### Directory Structure

```
[High-level tree output, depth 2-3]
```

### Entry Points

| Entry Point | File | Purpose |
|------------|------|---------|
| Main | | |
| API Routes | | |
| Config | | |

### Code Statistics

| Language | Files | Lines of Code |
|----------|-------|--------------|
| | | |
| **Total** | | |

---

## 3. Architecture Overview

**Style:** [Monolith / Modular Monolith / Microservices / Serverless / Monorepo]

**Layering:** [MVC / Clean Architecture / 3-Tier / Event-Driven / CQRS]

### Component Diagram (Textual)

```
[Request Flow]
Client -> [API Gateway/Router] -> [Middleware] -> [Controller] -> [Service] -> [Repository] -> [Database]
                                       |
                                  [Auth / Logging / Error Handling]
```

### Key Design Patterns

| Pattern | Where Used | Example |
|---------|-----------|---------|
| | | |

### Data Flow

[Describe how data flows through the system for a typical request]

### External Integrations

| Service | Purpose | Config Location |
|---------|---------|----------------|
| | | |

---

## 4. Dependency Health

### Core Dependencies ([N] total)

| Package | Version | Purpose | Health |
|---------|---------|---------|--------|
| | | | Active / Stable / Deprecated / Unmaintained |

### Concerns

- [CRITICAL] ...
- [WARN] ...
- [INFO] ...

### Lock File Status

- Lock file: [Present / Missing]
- Last updated: [Date]
- Pinning strategy: [Exact / Range / Loose]

---

## 5. Quality Snapshot

| Aspect | Status | Details |
|--------|--------|---------|
| Formatter | [OK / WARN / MISS] | |
| Linter | [OK / WARN / MISS] | |
| Type Safety | [OK / WARN / MISS] | |
| Unit Tests | [OK / WARN / MISS] | |
| Integration Tests | [OK / WARN / MISS] | |
| E2E Tests | [OK / WARN / MISS] | |
| Pre-commit Hooks | [OK / WARN / MISS] | |
| Documentation | [OK / WARN / MISS] | |
| API Docs | [OK / WARN / MISS] | |

### Complexity Hotspots

| File | Lines | Concern |
|------|-------|---------|
| | | God object / High complexity / Deep nesting |

---

## 6. Developer Onboarding

### Prerequisites

- [Runtime and version]
- [Database]
- [Other system dependencies]

### Quick Start

```bash
# 1. Install dependencies
[command]

# 2. Configure environment
[command]

# 3. Setup database
[command]

# 4. Run development server
[command]

# 5. Run tests
[command]

# 6. Build for production
[command]
```

### Key Scripts

| Command | Purpose |
|---------|---------|
| | |

### Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| | | | |

---

## 7. Risk Register

### Critical (Fix Immediately)

| # | Risk | Location | Suggested Action |
|---|------|----------|-----------------|
| 1 | | | |

### High (Fix Soon)

| # | Risk | Location | Suggested Action |
|---|------|----------|-----------------|
| 1 | | | |

### Medium (Plan to Address)

| # | Risk | Location | Suggested Action |
|---|------|----------|-----------------|
| 1 | | | |

### Low (Note for Future)

| # | Risk | Location | Suggested Action |
|---|------|----------|-----------------|
| 1 | | | |

### Technical Debt Summary

- **TODO/FIXME count:** [N] across [M] files
- **Top debt clusters:** [directories with highest concentration]
- **Estimated effort:** [rough sizing of remediation work]

---

## 8. Recommended First Steps

Priority-ordered actions for the new developer:

1. **[CRITICAL]** [Action] -- [Why] -- [Location]
2. **[HIGH]** [Action] -- [Why] -- [Location]
3. **[HIGH]** [Action] -- [Why] -- [Location]
4. **[MEDIUM]** [Action] -- [Why] -- [Location]
5. **[MEDIUM]** [Action] -- [Why] -- [Location]

### Areas to Understand Before Modifying

| Area | Why | Key Files to Read |
|------|-----|-------------------|
| | | |

### Safe Starting Points (Quick Wins)

| Task | Difficulty | Files Involved |
|------|-----------|----------------|
| | Easy / Medium | |

---

## Appendix

### A. Full Dependency List

[Complete dependency list if needed]

### B. File Count by Directory

[Breakdown of file counts per top-level directory]

### C. Glossary

| Term | Definition |
|------|-----------|
| [Project-specific terms] | |
