# Journal Profile Schema

Create a task-local `journal-profile.md` when the user asks for target-journal compliance. Do not store time-sensitive journal requirements in this skill as universal facts.

## Source Policy

Use sources in this order:

1. official author instructions or submission checklist;
2. official manuscript template and submission-system fields;
3. official notices that amend the instructions;
4. recent articles on the journal's official site, used only to observe editorial practice.

Record the source title, URL or supplied filename, publisher or journal owner, and access date. Separate explicit requirements from observed conventions. When official sources conflict, prefer the clearly newer source and record the conflict. Mark unverifiable items `unknown`.

Do not infer requirements from inclusion in 北大核心, CSCD, CSSCI, or another index. These indexes classify journals; they do not supply a shared manuscript style.

## Profile Template

```markdown
# Journal Profile

## Identity

- Journal:
- Discipline:
- Article type:
- Submission language:
- Profile checked on:

## Sources

| ID | Source type | Official title or filename | URL | Access date | Currentness notes |
|---|---|---|---|---|---|
| S1 | Author instructions | | | | |

## Requirement Matrix

| Area | Requirement | Source | Rule type | Verification status | Notes |
|---|---|---|---|---|---|
| Title | | S1 | hard / observed | verified / unknown | |
| Chinese abstract | | | | | |
| English abstract | | | | | |
| Keywords | | | | | |
| Main-text length | | | | | |
| Heading levels | | | | | |
| Figures and tables | | | | | |
| Equation object and editability | OMML / MathType-OLE / other | | | | |
| Inline and displayed equations | | | | | |
| Equation typography | variables / functions / units / vectors / matrices | | | | |
| Display layout and spacing | alignment / tabs / indentation / line spacing | | | | |
| Equation numbering | scope / sequence / parentheses / placement | | | | |
| Equation cross-references | wording / fields / bookmarks | | | | |
| Multiline equations | break and alignment rules | | | | |
| Symbols and definitions | | | | | |
| Units and nomenclature | | | | | |
| References | | | | | |
| Author and affiliation | | | | | |
| Funding | | | | | |
| Ethics and consent | | | | | |
| Conflict of interest | | | | | |
| Data and code availability | | | | | |
| Anonymization | | | | | |
| File format | | | | | |
| Supplementary material | | | | | |

## Unknowns and Conflicts

- [Requirement or conflict] - [why unresolved] - [author action needed]

## Manuscript Compliance

| Requirement | Status | Manuscript evidence | Required action |
|---|---|---|---|
| | pass / fail / unknown / not-applicable | | |
```

## Interpretation Rules

- Use `hard` only for wording explicitly stated by an official source.
- Use `observed` for patterns inferred from published articles; never present these as mandatory.
- Use `pass` only when the manuscript contains inspectable evidence satisfying the requirement.
- Use `fail` only when both the requirement and manuscript state are known.
- Use `unknown` when the requirement, manuscript state, or currentness cannot be verified.
- Use `not-applicable` only when the article type clearly excludes the requirement.
- Cite the profile source when recommending a format change.
- Record equation requirements at the listed level of detail; do not turn one observed font, tab position, object type, or numbering sample into a journal-wide rule.
- Recheck the profile at the time of each new submission cycle; journal instructions can change.

Do not claim “符合中文核心规范.” State the narrower result, such as “checked against the official author instructions accessed on YYYY-MM-DD,” and retain the unresolved items.
