<!-- OpenDocKit author guidance
ID: service.comprehensive.docs.service.async-processing.md
Purpose: Define message/job ownership, delivery assumptions, ordering and processing transactions.
Use when: This service capability is relevant to the project.
Suggested destination: docs/service/async-processing.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Asynchronous work

## Scope and authority

{{Define message/job ownership, delivery assumptions, ordering and processing transactions.}}

## Failure and evolution

{{Specify ack/retry/dead-letter, poison events, replay, schema evolution and cancellation.}}

## Verification and ownership

{{Verify duplicates, lag, crashes and replay without claiming exactly-once from a label.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
