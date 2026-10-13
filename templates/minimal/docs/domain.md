<!-- OpenDocKit author guidance
ID: base.minimal.docs.domain.md
Purpose: Define domain terms, state transitions, rules and invariants.
Use when: Behavior depends on business meaning or correctness rules.
Suggested destination: docs/domain.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Domain

## Language and boundaries

{{Define precise terms, actors, bounded contexts and ownership; link product behavior without repeating it.}}

## Model and lifecycle

{{Describe entities/value objects, identity, state transitions and legal operations, including cancellation and retries.}}

## Rules and invariants

{{Assign checkable predicates and stable IDs; cover concurrent updates, partial failure and exceptions with decision authority.}}

## Flows and verification

{{Trace important business flows across boundaries; identify enforcement, tests, compensation and still-unverified assumptions.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
