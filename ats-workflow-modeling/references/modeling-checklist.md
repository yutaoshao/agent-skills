# ATS Workflow Modeling Checklist

Use only the sections that match the supplied product scope.

## Boundary

- Product and workflow being modeled
- Actors and external systems
- In-scope objects and out-of-scope behavior
- Evidence sources and claim states

## State Table

| ID | Current state | Trigger | Actor | Preconditions | Action | Side effects | Next state | Failure/manual fallback |
|---|---|---|---|---|---|---|---|---|

Check that every terminal state is intentional, every decision has an owner,
and every transition has a user-visible result.

## Permission Matrix

| Role | Navigation | Data scope | View fields | Mutations | Decisions | Admin actions |
|---|---|---|---|---|---|---|

Separate "can see the page" from "can see a candidate's data" and from "can
perform the action". Record whether a permission is row-, field-, stage-, or
organization-scoped.

## Integration Closure

For each external call, identify request owner, idempotency key or duplicate
guard, timeout/retry behavior, delivery status, reconciliation, and manual
fallback. Do not claim delivery merely because an API request returned.

## Review Questions

- Can an item become stuck with no owner?
- Can two screens show different stages for the same application?
- Can a rejected candidate remain in the active pipeline unintentionally?
- Can a role access HR-only data through a deep link or API?
- Can a retry duplicate a calendar event, message, offer, or audit record?
- Can an administrator diagnose failure without exposing candidate data to other
  roles?
