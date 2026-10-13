<!-- OpenDocKit author guidance
ID: template.comprehensive.docs.components.frontend.README.md
Purpose: Explain frontend-specific responsibilities and development boundaries.
Use when: This component actually exists and requires independently maintained detail.
Suggested destination: docs/components/frontend/README.md
Boundary: Do not duplicate product/domain/contracts/data/security authorities.
Adoption: Copy manually, fill actual facts and source links, then remove author guidance.
-->
# Frontend Component Guide

## Scope and sources

{{Name component boundary/owner, architecture context and shared authorities; do not invent a stack.}}

## Implementation and interaction

{{Describe local code structure, lifecycle/flows, component-specific conventions and failure handling; link contracts and shared rules.}}

## Development and verification

{{Give actual setup/run/check sources and working directory, expected evidence and constraints. Update when the component or its boundaries change.}}

## Open questions

{{Name unresolved decisions, owners and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope, authority and ownership are explicit.
- [ ] Facts and summaries point to their canonical sources.
- [ ] Evidence and lifecycle state are observed; unrun checks are marked NOT RUN.
