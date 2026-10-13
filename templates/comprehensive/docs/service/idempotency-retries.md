<!-- OpenDocKit author guidance
ID: service.comprehensive.docs.service.idempotency-retries.md
Purpose: Identify retryable operations, key scope, deduplication lifetime and result authority.
Use when: This service capability is relevant to the project.
Suggested destination: docs/service/idempotency-retries.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Retries and idempotency

## Scope and authority

{{Identify retryable operations, key scope, deduplication lifetime and result authority.}}

## Failure and evolution

{{Define timeout/partial success, replay, concurrent requests and backoff limits.}}

## Verification and ownership

{{Test duplicate and interrupted operations against checkable domain invariants.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
