# Review Checklist

Use this checklist for standard, deep, and submission-oriented polishing. Report failures and unknowns; do not convert them into silent edits.

## Severity Model

| Severity | Meaning | Required handling |
|---|---|---|
| `blocker` | Possible fabrication, contradictory evidence, broken file, or requirement preventing reliable delivery | Stop the affected edit and request resolution |
| `major` | Meaning drift, unsupported claim, missing evidence, or verified journal-rule violation | Correct from evidence or raise an author query |
| `minor` | Local clarity, consistency, grammar, or formatting problem | Correct while preserving meaning |
| `suggestion` | Optional improvement with a real tradeoff | Explain; do not present as mandatory |

## Pre-Edit Check

- [ ] Identify input format and editable source.
- [ ] Identify discipline and article type.
- [ ] Record target journal or label the task general-only.
- [ ] Select light, standard, or deep editing.
- [ ] Record requested output and revision visibility.
- [ ] Inventory integrity anchors.
- [ ] Inventory protected propositions that may be rewritten, merged, or relocated.
- [ ] For equation-bearing DOCX, inventory OMML, embedded objects, drawings, numbers, fields, bookmarks, references, and equation paragraph styles.
- [ ] Identify missing context that makes a requested rewrite unsafe.

## Structure and Argument

- [ ] Title, abstract, body, and conclusion describe the same research scope.
- [ ] The research problem and gap are distinguishable.
- [ ] Each contribution maps to supplied evidence.
- [ ] Each section and paragraph has an identifiable rhetorical job.
- [ ] Every sentence or proposition-bearing unit has an identifiable necessary function.
- [ ] Every sentence passes the deletion test, or is merged, deleted, or queried.
- [ ] Repeated propositions serve distinct reader needs rather than duplicating wording.
- [ ] Necessary information appears in the section where readers need it.
- [ ] Wording and high-emphasis positions give each proposition proportionate weight.
- [ ] Paragraph order reflects the actual reasoning or procedure.
- [ ] Results are distinguishable from interpretation.
- [ ] Limitations remain visible and proportionate.
- [ ] The conclusion does not exceed tested conditions.

## Language

- [ ] Subjects and pronoun antecedents are clear.
- [ ] Terms, abbreviations, symbols, and names are consistent.
- [ ] Long modifiers and nested clauses remain interpretable.
- [ ] Transitions state real logical relations.
- [ ] Empty emphasis and redundant framing are removed where safe.
- [ ] Necessary hedging and scope qualifiers remain.
- [ ] Lists and prose are chosen by rhetorical function, not a blanket rule.
- [ ] Revised paragraphs read naturally in their surrounding context.

## Evidence and Integrity

- [ ] Original and revised numbers, units, signs, ranges, and precision are compared.
- [ ] Comparisons retain their baseline, metric, dataset, and condition.
- [ ] Statistical terms are supported by the manuscript.
- [ ] Causal and novelty claims are not strengthened.
- [ ] Citation identifiers and claim attachment are preserved.
- [ ] New references, if any, are verified from authoritative metadata.
- [ ] Equations, figures, tables, captions, and cross-references remain aligned.
- [ ] Every protected proposition remains traceable, correctly scoped, and sufficiently visible after moves, merges, or deletions.
- [ ] Funding, ethics, conflicts, data, authorship, and affiliations remain factual.
- [ ] Every unresolved integrity issue appears in the author-query list.

## Word Equations

- [ ] Every displayed equation and material inline formula has a necessary technical function, appropriate placement, and a prose introduction or definition where needed.
- [ ] Operators, signs, term order, scripts, limits, conditions, dimensions, and symbol meanings match the protected source.
- [ ] Native OMML remains native and editable; OLE or MathType candidates and their embedded parts remain intact unless conversion was explicitly authorized.
- [ ] No equation was silently flattened to plain text or replaced with a drawing or image.
- [ ] Equation-bearing paragraphs were edited at node or run level rather than rebuilt from whole-paragraph text.
- [ ] Inline or displayed treatment, numbering scope, parentheses, typography, punctuation, and symbol definitions follow a verified rule or the manuscript's consistent convention.
- [ ] Displayed formulas use a verified equation style or real tab stops; repeated spaces are not used for centering or number alignment.
- [ ] Long formulas break at logical points and remain legible at the actual column width; stacked content is not clipped by fixed line spacing.
- [ ] Visible numbers are unique and follow the verified sequence; `SEQ`, bookmarks, `REF`, and visible references are synchronized.
- [ ] Before-and-after structural audits account for native math, embedded objects, numbers, fields, bookmarks, and intentional formula changes.
- [ ] Every formula page was inspected after rendering, and the final repaginated document was inspected page by page.
- [ ] The renderer had the required fonts and compatible equation support; alternate-renderer missing glyphs or layout changes were not mistaken for source defects.
- [ ] Desktop Word fields were updated before final rendering, or the unavailable step is reported explicitly.

## Journal Compliance

- [ ] The journal profile cites current official sources and access dates.
- [ ] Hard requirements and observed conventions are separated.
- [ ] Article type matches the profile.
- [ ] Title, abstracts, and keywords meet verified requirements.
- [ ] Length and heading requirements are checked.
- [ ] Figure, table, equation, unit, and nomenclature rules are checked.
- [ ] Reference and citation style is checked without inventing metadata.
- [ ] Author, funding, ethics, conflict, data, anonymization, and file requirements are checked.
- [ ] Unknown and conflicting requirements remain explicit.

## File Validation

- [ ] `.docx` styles, fields, bookmarks, equations, embedded parts, comments, footnotes, relationships, and revision state are preserved.
- [ ] `.tex` commands, labels, citations, and macros remain valid.
- [ ] Markdown tables, links, citations, and code blocks remain intact.
- [ ] PDF-only limitations are reported.
- [ ] Relevant compilation, rendering, or structured-file checks were run.
- [ ] Failed, skipped, and unavailable checks are listed plainly.

## Delivery Template

```markdown
# 润色交付报告

## 范围

- 文件或章节：
- 润色等级：light / standard / deep
- 学科 profile：
- 目标期刊 profile：verified / partial / unavailable
- 输出形式：

## 主要修改

| 位置 | 严重度 | 句子功能 | 处置 | 修改说明 | 是否需作者确认 |
|---|---|---|---|---|---|
| | | | keep / rewrite / merge / move / delete / query | | |

## 逐句审查摘要

- 审查范围：
- 已审查单元数：
- 保留 / 改写 / 合并 / 移动 / 删除 / 待确认：
- 仅在工作记录中保留、未逐项交付的低风险判断：

## 作者待确认项

| 位置 | 问题 | 保留的原文或临时处理 | 所需证据或决定 |
|---|---|---|---|
| | | | |

## 期刊规范检查

| 要求 | 状态 | 证据 | 后续动作 |
|---|---|---|---|
| | pass / fail / unknown / not-applicable | | |

## 完整性核对

- 已比较：
- 无法验证：
- 新增或删除的引用：
- 移动、合并或删除的受保护命题：
- 数据、公式或结论风险：

## Word 公式核对

- 原生 OMML / 嵌入对象 / 图片候选：
- 编号、书签与交叉引用：
- 有意修改的公式及依据：
- 结构比较结果：
- 逐页渲染结果：
- Word 字段更新：已执行 / 未执行（原因）
- 待作者确认：

## 执行检查

- 已通过：
- 失败：
- 跳过或不可用：
```

Describe a clean result as “ready for author review.” Never promise acceptance, plagiarism-check outcomes, AI-detector outcomes, or compliance with requirements that were not verified.
