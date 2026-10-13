<!-- OpenDocKit author guidance
ID: template.comprehensive.docs.components.README.md
Purpose: Route readers to independently maintained implementation components.
Use when: A system has components with separate ownership or conventions.
Suggested destination: docs/components/README.md
Boundary: Architecture owns system structure; this map routes to component detail.
Adoption: Copy manually, fill actual facts and source links, then remove author guidance.
-->
# Component Map

## Current map

Available samples: [frontend](frontend/README.md), [backend](backend/README.md).

{{Keep only actual components and identify their owners/current scope.}}

## Shared contracts

{{Link system/domain/interface/data/security authorities; identify component-specific differences.}}

## Maintenance

{{Review when component boundaries/owners/check commands change and remove obsolete routes.}}

## Open questions

{{Name unresolved decisions, owners and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope, authority and ownership are explicit.
- [ ] Facts and summaries point to their canonical sources.
- [ ] Evidence and lifecycle state are observed; unrun checks are marked NOT RUN.
