<!-- OpenDocKit author guidance
ID: mobile.minimal.docs.mobile.md
Purpose: Describe mobile-specific behavior, failure modes and verification.
Use when: The project has mobile responsibilities.
Suggested destination: docs/mobile.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Mobile

## Supported devices and OS

{{List OS versions, device classes, form factors, input/accessibility requirements and feature availability. Describe incompatible OS/API behavior, deprecation and cross-platform divergence. Specify device/OS test matrix, ownership and evidence before claiming support.}}

## Platform permissions

{{Map each requested permission to user value, data scope and least required access. Describe denied/revoked/restricted states, rationale UX and platform policy differences. Test fresh install, revocation and recovery; link privacy/data authority.}}

## Offline data and synchronization

{{Choose local/remote authorities, offline actions, queue persistence and sync ownership. Specify conflict resolution, ordering, retries/idempotency, tombstones and interrupted-sync recovery. Test airplane mode, process death, duplicate events and stale data; state unresolved consistency limits.}}

## Background work

{{Describe scheduled/push/location tasks, lifecycle transitions and resource constraints. Specify cancellation, battery/OS restrictions, suspension, duplicate dispatch and foreground recovery. Test background/terminated/restricted modes and record actual supported scheduling behavior.}}

## Device testing

{{Map risky features to real/emulated device scenarios, OS versions and network conditions. Define data reset, accessibility, orientation, memory/battery/performance and interrupted-session fixtures. Record actual device/OS/build and results; emulation does not prove every hardware behavior.}}

## Store delivery

{{Name package identifiers, platform signing owners, build/version channels and store authorities. Describe review requirements, phased rollout, incompatible data changes and update/recovery constraints. Record checks, approval status and rollback/forward-fix plan; no claimed store approval without evidence.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
