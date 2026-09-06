---
name: codex-daily-report
description: Generate concise Chinese work daily reports from Codex tasks and the user's recent report examples. Use when asked to review today's Codex conversations, tasks, or threads; summarize them into a 日报 or 工作日报; continue an existing daily-report style; or save or update a dated report. Distinguish completed work from research, discussion, and plans, deduplicate related tasks by outcome, and follow the user's compact report conventions.
---

# Codex Daily Report

Turn same-day Codex task evidence into a short work report. Report outcomes,
not the conversation or tool-use process.

## Collect the Day's Evidence

1. Resolve the target date in the user's local timezone. Treat “today” as the
   current local calendar day unless the user names another date.
2. Use the host's Codex task-list tool to request enough recent tasks to cross
   the start-of-day boundary. Consider tasks created earlier if they contain
   turns from the target date.
3. Select Codex tasks with activity on the target date. Exclude ChatGPT chats,
   the current report-generation task, and unrelated personal conversations.
4. Read the relevant turns in each selected task. Follow older-page cursors
   until all target-date turns are covered; do not pull earlier work into the
   report merely because it shares a task.
5. Parse `codex://threads/<id>` links directly when the user supplies them.
   Treat supplied tasks as evidence, but still inspect the rest of the day's
   Codex tasks when the request covers the whole day.

Use task metadata only for discovery. Base report claims on the task content,
final outputs, changed artifacts, or executed checks. Do not browse the web or
cite Codex product documentation just to generate the report. If task-reading
tools are unavailable, use only transcripts or exports the user supplied and
state the evidence gap outside the report.

## Learn the User's Format

When the user gives a report file or directory:

1. Read the three to five most recent daily reports before the target date.
2. Exclude weekly reports and unrelated notes.
3. Use the latest complete report as the primary template. Use repeated
   patterns across the other reports to distinguish conventions from one-off
   formatting or unfinished drafts.
4. Preserve the user's headings, numbering, terminology, density, and treatment
   of learning notes. Keep the source reports read-only unless the user asks to
   save or update a file.

For the established compact Chinese format, prefer `今日完成：`, bare numbered
lines such as `1 ...`, an optional `读书摘要：`, and `明日计划：`. Do not add a
document title, date line, or project tag unless recent complete reports use
them consistently.

## Synthesize Before Writing

Build a private evidence ledger with the work theme, accurate action verb,
outcome, completion state, and supported next step. Do not expose the ledger.

- Merge tasks that contribute to the same outcome. Collapse retries,
  debugging turns, prompt iterations, and follow-up clarifications.
- Prefer work-relevant outcomes over file names, commands, commits, test logs,
  or internal implementation details.
- Use status-accurate verbs: `梳理` or `调研` for analysis, `设计` for a
  proposed solution, `实现` for a material implementation, `验证` only for an
  executed check, and `完成` only when the intended result is actually done.
- Never upgrade a request, discussion, plan, or partial attempt into a completed
  result. Omit abandoned or trivial tasks unless they produced a reportable
  outcome.
- Mention blockers only when they materially affect delivery. State them
  plainly rather than turning the report into a troubleshooting log.
- Derive tomorrow's plan only from explicit plans, unfinished substantive work,
  or direct next steps in the day's tasks. Do not invent work to fill a section.

## Write the Report

Use the smallest set of numbered items that covers the day's substantive work,
normally one line per outcome. Keep each item concrete: action, object, and the
useful result when it fits naturally.

Include `读书摘要：` only when learning or reading was part of the day. Use one
short bullet per chapter or topic and summarize its central idea in one
sentence. Do not expand it into general study notes.

Use this default shape when it matches the examples:

```text
今日完成：

1 <事项>
2 <事项>
3 学习《<资料>》第 <章节>：

读书摘要：
- 第 <章节>：<一句话核心内容>。

明日计划：

1 <有依据的下一步>
2 <有依据的下一步>
```

Omit the reading block when it does not apply. Omit `明日计划` rather than
inventing unsupported plans. Output only the report body: no preface, method
explanation, citations, source list, code fence, or closing offer.

## Save Only When Requested

Draft in the response by default. When the user explicitly asks to save or
update the report, infer the filename convention from adjacent reports, read an
existing target file before editing, and preserve unrelated content. Do not
silently overwrite competing material.

## Final Check

Before returning the report, verify that:

- every work item is supported by a target-date Codex turn or artifact;
- research, discussion, implementation, and completion are not conflated;
- related tasks are deduplicated by outcome;
- the latest complete report's structure and terminology are preserved;
- reading summaries and tomorrow plans are concise and evidence-backed;
- the response contains the report only and does not become a long explanation.
