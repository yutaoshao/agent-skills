# project-analyzer

An evidence-led onboarding skill for developers taking over unfamiliar
repositories.

## Outcome

The default workflow helps a newcomer:

- explain who the project serves and what recurring value it delivers;
- map core modules by responsibility, contract, and state ownership;
- select one representative, routine user or consumer journey;
- trace that journey through entry points, key symbols, data changes, side
  effects, observable results, and tests;
- distinguish verified facts from inferences, unknowns, and non-applicable checks.

## Default Workflow

1. Establish repository scope, instructions, revision, and exclusions.
2. Build the product and domain model.
3. Classify the project type and map module responsibilities.
4. Select a journey that demonstrates core value and crosses key boundaries.
5. Trace concrete symbols from trigger to observable result.
6. Run only safe, targeted verification.
7. Produce an evidence-backed onboarding map and reading order.

The skill does not run a comprehensive audit merely because the user asks for an
overview.

## Optional Deep Dives

Focused workflows are available for technology and dependencies, testing and
quality, development and delivery, security, reliability, performance,
observability, technical debt, and change risk.

## Skill Structure

```text
project-analyzer/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- evidence-policy.md
    |-- journey-playbooks.md
    |-- architecture-patterns.md
    |-- analysis-checklist.md
    `-- report-template.md
```

## Installation

### Codex

Use the built-in `$skill-installer`:

```text
$skill-installer https://github.com/yutaoshao/agent-skills/tree/main/project-analyzer
```

### Claude Code Plugin Marketplace

```bash
/plugin marketplace add yutaoshao/agent-skills/project-analyzer
```

### Manual Claude Code Installation

```bash
git clone https://github.com/yutaoshao/agent-skills.git
cp -r agent-skills/project-analyzer ~/.claude/skills/
```

## Usage

Example requests:

- "I just joined this team. Help me understand this repository."
- "Explain what this project is for and how its core modules collaborate."
- "Trace one representative user journey from entry point to tests."
- "Map the architecture of this CLI without assuming it is a web service."
- "Perform a focused dependency or security deep dive."

## License

MIT
