<!-- OpenDocKit author guidance
ID: template.comprehensive.docs.roles.qa.md
Purpose: Provide a sourced TL;DR and actionable reading route for Quality Assurance / Quality Control.
Use when: This audience or responsibility is relevant to the project.
Suggested destination: docs/roles/qa.md
Boundary: Summaries and navigation link canonical authority; no duplicate live work state.
Adoption: Fill actual facts and sources, adjust links to adopted files, then remove author guidance.
-->
# Quality Assurance / Quality Control Brief

## Reader goal

Understand quality risks, acceptance and the evidence needed to judge correctness.

{{State the reader's current responsibility/project familiarity; tailor this brief to the task.}}

## TL;DR

- **Acceptance:** {{Summarize the highest-impact behavior/invariants and applicable quality/accessibility expectations. Link the source for each summary statement.}}
- **Risk coverage:** {{Summarize failure scenarios, test environments/data and important gaps in verification. Link the source for each summary statement.}}
- **Evidence and disposition:** {{Summarize actual verification findings and release blockers; pending and NOT RUN are not success. Link the source for each summary statement.}}

## Actions and sources

- [product](../product/README.md)
- [domain](../domain/README.md)
- [experience](../experience/README.md)
- [quality](../quality/README.md)
- [security](../security/README.md)
- [plans records](../plans/README.md)
- [verification records](../verification/README.md)
- [reviews records](../reviews/README.md)
- [releases records](../releases/README.md)

{{Describe which sources this role must create/review/accept and the receiving role or authority.}}

## Maintenance

{{Name brief owner, source links/revisions reviewed and important uncertainties. Refresh when those sources or responsibilities change. Closed-work history remains at its original records; do not keep a second live status table here.}}

## Completion check

- [ ] Summary statements have current authoritative sources.
- [ ] Adopted paths, owner and review triggers are accurate.
- [ ] Pending decisions/checks and completed evidence remain distinct.
