---
name: adr-management
description: Manage durable Architecture Decision Records in software repositories. Use when choosing or reviewing a module's architecture, framework, storage, integration, security, or operational approach; when creating, validating, accepting, rejecting, deprecating, or superseding an ADR; or when linking an ADR with Trellis task design.md, research, and spec files. Prefer this skill whenever a decision has meaningful future cost, multiple viable options, or a non-obvious constraint that should outlive the current conversation.
---

# ADR Management

Record the reason behind consequential technical choices so future agents and
engineers can recover both the decision and its boundaries. Keep the historical
record separate from task plans and current coding rules, then link the three
layers explicitly.

## Document Layers

Use the repository's existing convention when one is present. Otherwise use
`docs/adr/` with four-digit filenames such as
`0001-local-sqlite.md`.

| Layer | Purpose | Expected contents |
| --- | --- | --- |
| ADR | Durable decision history | Context, drivers, alternatives, decision, consequences, status, and revisit triggers |
| Trellis `design.md` | Task-level design | How this task applies the ADR: boundaries, data model, interfaces, rollout, and open questions |
| Trellis `.trellis/spec/` | Current executable rules | Stable constraints that implementation and review must continue to enforce |

Do not turn `.trellis/spec/` into an ADR archive. A spec states what
is true now; an ADR explains why the project chose it and when it should be
revisited. If a repository deliberately uses `.trellis/adr/`, pass that
directory to the CLI and preserve the same filename and metadata conventions.

## Decision Threshold

Create an ADR when at least one condition holds:

- the choice affects more than one module, a public contract, persisted data,
  deployment, security, reliability, or operating cost;
- there are two or more credible options and the trade-off is not obvious from
  local code;
- reversing the choice later would be expensive, disruptive, or require data
  migration;
- a constraint is likely to be mistaken for a historical accident;
- an AI agent or new contributor would reasonably ask "why this option?".

Do not create an ADR for routine implementation details that are already fully
specified by an existing ADR or spec. Mention the existing ADR instead.

## Workflow

### 1. Discover and read

1. Determine the ADR directory: inspect `docs/adr/`,
   `.trellis/adr/`, and repository documentation before creating a new
   location. Use `docs/adr/` only when no convention exists.
2. Read the ADR index, then the relevant accepted, proposed, superseded, or
   deprecated records. Search by module, technology, constraint, and status.
3. For a Trellis project, identify the active task directory and read its
   `design.md`, relevant `research/`, and applicable
   `.trellis/spec/` files.
4. Check whether the requested choice is already decided. If so, explain the
   existing decision and record only a new exception or replacement when needed.

Use the bundled CLI for deterministic inventory and checks:

```bash
python3 /absolute/path/to/adr-management/scripts/adr.py next --dir docs/adr
python3 /absolute/path/to/adr-management/scripts/adr.py list --dir docs/adr
python3 /absolute/path/to/adr-management/scripts/adr.py validate --dir docs/adr
```

### 2. Capture the proposal in the task design

Before acceptance, put the candidate decision and its alternatives in the
active Trellis task's `design.md`. Include an explicit `Related ADRs`
section, using `proposed` ADR IDs when the record has been created. Keep
implementation details in `design.md`; keep the durable "why" in the ADR.

For a new decision, create a proposed record:

```bash
python3 /absolute/path/to/adr-management/scripts/adr.py create \
  --dir docs/adr \
  --title "Choose local SQLite for the desktop demo" \
  --slug local-sqlite \
  --owner "team-or-owner" \
  --related-design .trellis/tasks/<task>/design.md \
  --related-task .trellis/tasks/<task> \
  --related-spec .trellis/spec/<relevant-rule>.md
```

The command refuses to overwrite an existing path. Replace every placeholder
and complete all required sections using the template in
`references/adr-template.md`. That file is directly copyable: front matter
starts on its first line. Keep one-line scalars and one-level block or inline
lists; IDs must match the four-digit filename prefix, empty relationships use
`[]`, and artifact paths should be repository-relative.

### 3. Review before acceptance

Review the record as a decision, not as an implementation diary. Confirm:

- the context names the problem and the forces that make it non-trivial;
- alternatives are concrete and evaluated against the stated drivers;
- the decision is specific enough to constrain implementation without dictating
  incidental code;
- consequences include costs, risks, migration or rollback implications, and
  non-functional effects;
- assumptions and evidence are distinguishable from facts;
- related task/design/spec paths exist, and the design explains how the choice
  will be applied;
- revisit triggers are observable, and the status accurately reflects review.

Run the read-only review and validation commands:

```bash
python3 /absolute/path/to/adr-management/scripts/adr.py review docs/adr/0001-local-sqlite.md
python3 /absolute/path/to/adr-management/scripts/adr.py validate --dir docs/adr
```

Do not mark a record `accepted` merely because code was written. Acceptance
is the team's agreement that the decision and its consequences are understood.
The CLI refuses `proposed -> accepted` while required sections are placeholders
or otherwise empty, or while `Review Notes` lacks a recorded outcome; complete
the record and review it first.
When review rejects the proposal, preserve the record as `rejected` and
explain the reason in the review notes or a follow-up ADR; do not delete it.

### 4. Change status deliberately

Use the CLI so status changes are visible in the diff and invalid transitions
are rejected:

```bash
python3 /absolute/path/to/adr-management/scripts/adr.py status \
  docs/adr/0001-local-sqlite.md --to accepted
```

Supported statuses are `proposed`, `accepted`, `rejected`,
`superseded`, and `deprecated`. The normal transitions are:

```text
proposed  -> accepted | rejected | deprecated
rejected  -> proposed
accepted  -> superseded | deprecated
superseded -> (terminal)
deprecated -> (terminal)
```

Treat `superseded` as terminal. To reconsider a rejected decision, create
a new proposal or explicitly move it back to `proposed`; never rewrite the
historical decision text to make the old choice appear different.

### 5. Supersede instead of rewriting history

When a later decision replaces an accepted ADR, create and review the new ADR
first. Then update both records with the coordinated command:

```bash
python3 /absolute/path/to/adr-management/scripts/adr.py supersede \
  --dir docs/adr --old ADR-0001 --new ADR-0007
```

The command requires the new ADR to be `accepted`, marks the old ADR
`superseded`, keeps the front matter and body relationship lines synchronized,
refuses inconsistent or non-reciprocal links,
and attempts to restore both original files if either replacement fails. Any
write or rollback failure is surfaced as an error. If the
replacement is still only a proposal, record
`Supersedes: ADR-0001` in the new ADR's prose or metadata and wait until
acceptance before running the transition command.

### 6. Synchronize with Trellis

For each accepted decision:

1. In the task `design.md`, keep a reciprocal link to the ADR and state
   which design choices implement it.
2. In `.trellis/spec/`, capture only stable, testable constraints
   derived from the ADR. Add a `Related ADRs` link so the rationale
   remains discoverable.
3. Keep detailed investigation in the task's `research/` and link it
   from the ADR's `Evidence` or `Related Artifacts` section.
4. During `trellis-check` or review, verify that implementation, design,
   and spec do not contradict an accepted ADR. If they do, pause and decide
   whether to update the implementation or create a superseding ADR.
5. At task close, run ADR validation and update the Trellis task notes/journal;
   do not silently promote an unreviewed proposal into a permanent spec.

The CLI validates relative artifact paths against the repository root when it
can infer one. It reports missing paths; it does not create placeholder specs,
modify design files, or conceal a broken link.

New records use the simple front matter defined in
`references/adr-template.md`: one-line scalars plus one-level block or inline
lists. For compatibility, `list`, `validate`, and `review` can also read the
common legacy Markdown form with `Status`, `Date`, `Owners`, `Related task`,
and `Supersedes` bullets. Only files matching `NNNN-lowercase-slug.md` are
treated as records, so `index.md` and `template.md` are ignored. Migrate a
legacy record to front matter before using mutating `status` or `supersede`
commands; the CLI refuses to guess how to rewrite legacy metadata.

## Commands

All commands are read-only unless noted. Run `python3 scripts/adr.py --help`
for complete options.

```text
next       Print the next available ADR ID
create     Create a non-overwriting proposed ADR from the template (mutates)
list       List records, optionally filtered by status or as JSON
validate   Check filenames, metadata, sections, IDs, statuses, and references
review     Report review gaps for one or more records (read-only)
status     Apply a validated status transition (mutates)
supersede  Link two accepted ADRs with coordinated writes and rollback (mutates)
```

Use explicit absolute paths when the current working directory is not the
repository root. The script uses only the Python standard library and exits
non-zero on invalid input or failed validation. Missing related paths are
warnings by default; pass `validate --strict` to make warnings fail the check.

## Safety Rules

- Never overwrite, delete, or renumber an existing ADR to "clean up" history.
- Never invent a rationale, owner, date, evidence, or status to fill a blank.
- Keep secrets and credentials out of ADRs; reference a secure system by name.
- Treat public API, schema, migration, security, and operational claims as
  reviewable facts and cite code, tests, issue IDs, or research where available.
- If a decision is uncertain, keep it `proposed` and state the open question.
- Prefer a new ADR for a materially different choice; edit an accepted ADR only
  for clear factual corrections that do not alter its decision.
