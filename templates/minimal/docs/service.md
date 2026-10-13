<!-- OpenDocKit author guidance
ID: service.minimal.docs.service.md
Purpose: Describe service-specific behavior, failure modes and verification.
Use when: The project has service responsibilities.
Suggested destination: docs/service.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Service

## Service delivery

{{Link canonical interface contract, consumers, deployment units and compatibility obligations. Specify traffic switching, readiness, config dependencies and deployment order for contract changes. Verify old/new consumers and rollout stop conditions with actual revision/evidence.}}

## Retries and idempotency

{{Identify retryable operations, key scope, deduplication lifetime and result authority. Define timeout/partial success, replay, concurrent requests and backoff limits. Test duplicate and interrupted operations against checkable domain invariants.}}

## Asynchronous work

{{Define message/job ownership, delivery assumptions, ordering and processing transactions. Specify ack/retry/dead-letter, poison events, replay, schema evolution and cancellation. Verify duplicates, lag, crashes and replay without claiming exactly-once from a label.}}

## Service resilience

{{Define dependency budgets, overload limits, failure isolation and fallback semantics. Specify timeouts, circuit behavior, degraded modes and recovery with ownership. Exercise dependency outage and overload; compare actual behavior with SLO/quality authority.}}

## Service evolution

{{Identify consumers, state/schema dependencies and compatibility windows. Plan expand/contract, deployment sequencing, migration and retirement without breaking old consumers. Record contract/migration tests, rollback constraints and actual release evidence.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
