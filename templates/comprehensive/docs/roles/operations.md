<!-- OpenDocKit author guidance
ID: template.comprehensive.docs.roles.operations.md
Purpose: Provide a sourced TL;DR and actionable reading route for Operations / DevOps.
Use when: This audience or responsibility is relevant to the project.
Suggested destination: docs/roles/operations.md
Boundary: Summaries and navigation link canonical authority; no duplicate live work state.
Adoption: Fill actual facts and sources, adjust links to adopted files, then remove author guidance.
-->
# Operations / DevOps Brief

## Reader goal

Understand ownership, deployment dependencies, failure response and recovery.

{{State the reader's current responsibility/project familiarity; tailor this brief to the task.}}

## TL;DR

- **Operating model:** {{Summarize actual environments, owners, dependencies and reliability expectations. Link the source for each summary statement.}}
- **Release and recovery:** {{Summarize rollout/compatibility/rollback and backup/restore constraints with actual evidence state. Link the source for each summary statement.}}
- **Current risks:** {{Summarize significant incidents, support/maintenance limits and pending operational decisions. Link the source for each summary statement.}}

## Actions and sources

- [operations](../operations/README.md)
- [engineering](../engineering/README.md)
- [architecture](../architecture/README.md)
- [data](../data/README.md)
- [security](../security/README.md)
- [releases records](../releases/README.md)
- [incidents records](../incidents/README.md)
- [verification records](../verification/README.md)
- [handoffs records](../handoffs/README.md)

{{Describe which sources this role must create/review/accept and the receiving role or authority.}}

## Maintenance

{{Name brief owner, source links/revisions reviewed and important uncertainties. Refresh when those sources or responsibilities change. Closed-work history remains at its original records; do not keep a second live status table here.}}

## Completion check

- [ ] Summary statements have current authoritative sources.
- [ ] Adopted paths, owner and review triggers are accurate.
- [ ] Pending decisions/checks and completed evidence remain distinct.
