<!-- OpenDocKit author guidance
ID: base.minimal.docs.operations.md
Purpose: Define ownership, rollout, reliability, incident and recovery procedures.
Use when: The project has operational or support responsibilities.
Suggested destination: docs/operations.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Operations

## Ownership and environment

{{Name operating/support teams, environment/configuration authority and deployment dependencies; remove operations that do not apply.}}

## Release and recovery

{{Describe rollout, compatibility, rollback, backup/restore and disaster recovery with stop conditions and actual evidence.}}

## Reliability and visibility

{{Define workload assumptions, SLI/SLO/alert ownership, logging/trace privacy and capacity/cost measurement sources.}}

## Routine and incident work

{{Link actionable runbooks, maintenance, incident escalation and support paths; preserve incident history separately from current procedure.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
