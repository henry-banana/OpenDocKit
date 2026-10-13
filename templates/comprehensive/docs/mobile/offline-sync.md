<!-- OpenDocKit author guidance
ID: mobile.comprehensive.docs.mobile.offline-sync.md
Purpose: Choose local/remote authorities, offline actions, queue persistence and sync ownership.
Use when: This mobile capability is relevant to the project.
Suggested destination: docs/mobile/offline-sync.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Offline data and synchronization

## Scope and authority

{{Choose local/remote authorities, offline actions, queue persistence and sync ownership.}}

## Failure and evolution

{{Specify conflict resolution, ordering, retries/idempotency, tombstones and interrupted-sync recovery.}}

## Verification and ownership

{{Test airplane mode, process death, duplicate events and stale data; state unresolved consistency limits.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
