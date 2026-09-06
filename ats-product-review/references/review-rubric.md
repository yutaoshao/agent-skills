# ATS Product Review Rubric

| Dimension | Review question | Typical blocker |
|---|---|---|
| Goal and users | Is the user outcome and audience explicit? | No owner or user value for a core path |
| Lifecycle | Are stages, states, transitions, and terminal outcomes complete? | Two artifacts assign different meanings to the same state |
| Ownership | Does each decision and task have one accountable role? | Item can wait forever or be approved by nobody |
| Permissions | Are navigation, data, field, and action permissions distinct? | Deep link/API bypasses a role boundary |
| Data integrity | Are candidate-job-resume relationships and history preserved? | Retry or reassociation loses or duplicates history |
| Integrations | Are delivery, retry, timeout, reconciliation, and manual fallback defined? | External failure appears as false success |
| Acceptance | Can every requirement be observed and verified? | Required behavior has no test oracle |
| Scope | Is MVP separated from future automation and reporting? | A future capability gates the core path |
| UX comprehension | Can the intended role understand the next action and error? | Internal codes or ambiguous labels block work |
| Privacy and audit | Are sensitive data visibility and audit expectations explicit? | Unauthorized role can read or export candidate data |

Use severity Blocker, High, Medium, or Low and confidence Verified, Inferred,
Unknown, or Decision Needed. Severity describes consequence; confidence describes
the evidence supporting the finding.
