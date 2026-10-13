<!-- OpenDocKit author guidance
ID: base.minimal.docs.interfaces.md
Purpose: Locate interface contracts and explain interaction/evolution semantics.
Use when: Independent consumers or integrations need stable expectations.
Suggested destination: docs/interfaces.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Interfaces

## Consumers and contract authority

{{List interface consumers and actual machine-contract/source owners; remove protocol sections that do not apply.}}

## Interaction semantics

{{Specify messages/operations, inputs/outputs, authentication/authorization boundaries and failure meanings; do not duplicate schemas.}}

## Evolution and integrations

{{Document version/compatibility rules, deprecation, dependent systems, retries/idempotency where relevant and responsibility for changes.}}

## Verification and ownership

{{Identify contract/consumer checks, test fixtures and ownership; distinguish a syntactically valid skeleton from a working interface.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
