<!-- OpenDocKit author guidance
ID: embedded.minimal.docs.embedded.md
Purpose: Describe embedded-specific behavior, failure modes and verification.
Use when: The project has embedded responsibilities.
Suggested destination: docs/embedded.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Embedded

## Hardware boundaries

{{Define board/revision, pin/protocol/voltage/timing constraints and peripheral ownership. Describe startup/reset, bus faults, shared resources and hardware variants. Link schematics/driver authority and measured interface tests.}}

## Firmware budgets

{{Specify memory/flash/stack/power/timing budgets, scheduling and measurement conditions. Identify worst-case concurrency, interrupt and resource-exhaustion behavior. Record measured firmware/board conditions; estimated limits are not proven deadlines.}}

## Firmware update

{{Define boot/update authority, image identity/verification and compatibility rules. Handle power loss, interrupted transfer, rollback/antirollback, state migration and recovery. Exercise failure points on actual or qualified test hardware and retain firmware hashes.}}

## Hardware verification

{{Define HIL/bench/emulation scope, board versions, instruments and fixtures. Cover timing, power/network loss, peripheral faults and environmental limits. Record actual hardware/calibration/build and results; simulation is not hardware certification.}}

## Device provisioning

{{Define identity/config provisioning, key ownership, enrollment and factory/service modes. Handle failed enrollment, reset, replacement, credential rotation and end-of-life data removal. Verify recoverable failures and accountable access; do not include real device secrets.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
