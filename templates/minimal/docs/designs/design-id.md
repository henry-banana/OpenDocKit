<!-- OpenDocKit author guidance
ID: template.minimal.docs.designs.design-id.md
Purpose: Explain a proposed solution and its trade-offs.
Use when: A change needs technical/UX design review.
Suggested destination: docs/designs/design-id.md
Boundary: Architecture describes the current system; this record describes the scoped proposal.
Adoption: Copy manually, fill actual facts and source links, then remove author guidance.
-->
# Change Solution Design

## Context and acceptance

{{Link change/spec ID, current architecture/domain/contracts, constraints and decision owner.}}

## Proposed behavior and structure

{{Explain affected components/flows/data/UI states and failure handling, at the scope needed for implementation.}}

## Alternatives and verification

{{Compare alternatives and consequences; map risky assumptions to actual verification plans.}}

## Promotion and history

{{When accepted and implemented, update canonical current docs and link significant ADRs. Preserve this proposal as history; do not leave it competing as current architecture.}}

## Open questions

{{Name unresolved decisions, owners and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope, authority and ownership are explicit.
- [ ] Facts and summaries point to their canonical sources.
- [ ] Evidence and lifecycle state are observed; unrun checks are marked NOT RUN.
