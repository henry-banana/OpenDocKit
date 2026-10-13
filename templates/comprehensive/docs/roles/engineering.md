<!-- OpenDocKit author guidance
ID: template.comprehensive.docs.roles.engineering.md
Purpose: Provide a sourced TL;DR and actionable reading route for Engineering.
Use when: This audience or responsibility is relevant to the project.
Suggested destination: docs/roles/engineering.md
Boundary: Summaries and navigation link canonical authority; no duplicate live work state.
Adoption: Fill actual facts and sources, adjust links to adopted files, then remove author guidance.
-->
# Engineering Brief

## Reader goal

Understand the system and the constraints that govern a change.

{{State the reader's current responsibility/project familiarity; tailor this brief to the task.}}

## TL;DR

- **System shape:** {{Summarize system boundaries, component responsibilities and critical runtime/data flow. Link the source for each summary statement.}}
- **Correctness constraints:** {{Summarize invariants, contract/security/compatibility obligations that must survive changes. Link the source for each summary statement.}}
- **Working and checking:** {{Summarize actual development/check sources, relevant decision rationale and known technical risks. Link the source for each summary statement.}}

## Actions and sources

- [architecture](../architecture/README.md)
- [domain](../domain/README.md)
- [interfaces](../interfaces/README.md)
- [data](../data/README.md)
- [engineering](../engineering/README.md)
- [security](../security/README.md)
- [specs records](../specs/README.md)
- [designs records](../designs/README.md)
- [plans records](../plans/README.md)
- [reviews records](../reviews/README.md)
- [verification records](../verification/README.md)

{{Describe which sources this role must create/review/accept and the receiving role or authority.}}

## Maintenance

{{Name brief owner, source links/revisions reviewed and important uncertainties. Refresh when those sources or responsibilities change. Closed-work history remains at its original records; do not keep a second live status table here.}}

## Completion check

- [ ] Summary statements have current authoritative sources.
- [ ] Adopted paths, owner and review triggers are accurate.
- [ ] Pending decisions/checks and completed evidence remain distinct.
