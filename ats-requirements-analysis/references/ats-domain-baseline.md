# ATS Domain Baseline

This is a reusable vocabulary aid, not a company policy. Replace it with the
project's confirmed terminology when the supplied evidence disagrees.

## Actors

- HR/recruiter: imports candidates, performs screening, coordinates interviews,
  and owns hiring operations.
- Business reviewer or hiring manager: evaluates role fit and may own a hiring
  decision for a stage.
- Interviewer: reviews permitted candidate material and submits interview
  feedback for an assigned round.
- System administrator: manages configuration, diagnostics, and operational
  access; should not automatically receive HR data access.
- Candidate: an external person represented by one or more applications.

## Objects

Job, candidate, application, resume/artifact, interview round, feedback, offer,
task/notification, and talent-pool record. Keep the candidate identity separate
from a job-specific application so rejection from one job does not erase the
person's reusable history.

## Common Questions

- Is this a person-level record or a job-level relationship?
- Which role owns the next decision?
- Which status is authoritative, and where is it persisted?
- Which fields are visible to each role, and which are internal-only?
- What is retained after rejection, withdrawal, deletion, or reassociation?
- What happens when an external source, mailbox, calendar, or notifier fails?
