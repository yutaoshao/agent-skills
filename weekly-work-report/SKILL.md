---
name: weekly-work-report
description: Generate concise Chinese weekly work reports from a week of daily reports. Use when asked to summarize 日报 into a 周报 or 工作周报, consolidate weekly accomplishments and material problems, plan next week's work, continue an existing weekly-report style, or save or update a dated weekly report. Merge daily entries by workstream, preserve the true completion state, and base next-week plans on explicit commitments, unfinished work, and supported next steps.
---

# Weekly Work Report

Turn daily reports into a compact weekly summary and a realistic next-week
plan. Report the week's outcomes, not a day-by-day transcript.

## Determine the Reporting Week

1. Resolve the target week in the user's local timezone. Follow an explicit
   date range or named week. Otherwise use the most recently completed
   workweek, normally Monday through Friday; use the current week to date only
   when the user asks for it.
2. When a weekly-report path or directory is supplied, inspect adjacent weekly
   filenames before choosing the output date. Do not assume that the filename
   date is the week-ending date; it may be the submission date or next Monday.
3. Collect the daily reports whose filename dates fall inside the target range.
   Exclude files containing `周报`, the target weekly draft, and unrelated
   notes. Follow the date range across sibling month directories when needed.
4. Read the latest one to three complete weekly reports for style. Use the most
   recent complete example as the primary template and repeated patterns as
   stronger evidence than one-off formatting.

Treat daily-report content as the source of truth. Do not inspect Codex tasks
or reconstruct missing days unless the user explicitly asks. If reports are
missing, summarize only the available coverage and never invent work.

## Extract Weekly Evidence

For each daily report, privately record:

- completed work or meaningful progress;
- the actual end-of-week state;
- explicit tomorrow or next-week plans;
- unresolved work that naturally carries over;
- material problems, their impact, and whether they were resolved.

Recognize that daily formats may vary. Text under `明日计划`, `明日工作计划`,
`下周`, or similar headings is a plan, not a completed result. Long technical
notes, screenshots, reading notes, and investigation logs support a concise
outcome but should not be copied into the weekly report.

Use status-accurate verbs. Preserve `调研`, `梳理`, `设计`, `实现`, `验证`, and
`完成` according to the evidence; do not upgrade partial progress or a plan
into a finished result.

## Consolidate by Workstream

1. Group related daily entries by project, objective, or deliverable.
2. Express each workstream at its final weekly state. Merge setup, learning,
   troubleshooting, and exercises when they contributed to one outcome.
3. Remove repeated daily status updates and intermediate steps. Do not count
   the same work once per day.
4. Prefer a small set of concrete outcomes over exhaustive coverage. Include
   business or learning value when it fits in the same short sentence.
5. Put a problem in `遇到的问题` only when it materially delayed or constrained
   the work. State the problem, response, and current result in one short
   paragraph; omit routine debugging.

Build `下周待完成` from explicit next-week instructions, unfinished substantive
work, and direct next milestones. Merge overlapping plans, order dependent
steps sensibly, and do not introduce a new initiative unsupported by the daily
reports or user request. Planning a direct next step is allowed when the user
asks for next-week planning, but keep it within the current workstream.

## Write in the Established Format

Use the compact heading structure from the user's weekly examples:

```text
# 内容:

# 本周已完成

1 <主题化成果>；
2 <主题化成果>；
3 <主题化成果>。

# 下周待完成

<一条计划，或多条简短编号计划。>

# 遇到的问题

<问题、处理和当前结果。>
```

Omit `遇到的问题` when no material problem is supported. Use one sentence for
a single next-week plan and numbered lines for multiple independent plans.
Preserve the user's terminology and heading style, while fixing obvious typos
and normalizing accidental spacing or inconsistent punctuation.

Output only the weekly-report body. Do not add a preface, date-range narrative,
daily subsections, detailed reading summaries, citations, source paths, a code
fence, methodology, or a closing offer.

## Save Only When Requested

Draft in the response by default. When the user explicitly asks to save or
update the report, infer the filename convention from adjacent files, such as
`M.D 周报.md`. Read an existing target before editing and preserve unrelated
content; do not silently overwrite a competing draft.

## Final Check

Before returning the report, verify that:

- every accomplishment is supported by an in-range daily report;
- daily progress is merged by workstream rather than repeated chronologically;
- completion wording matches the actual end-of-week state;
- next-week plans are supported, non-duplicative, and realistically scoped;
- the problems section includes impact and outcome rather than a debug log;
- the result matches the recent weekly format and stays concise.
