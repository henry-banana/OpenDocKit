<!-- OpenDocKit author guidance
ID: base.minimal.docs.data.md
Purpose: Explain data meaning, ownership, persistence, lifecycle and recovery.
Use when: Data is persisted, shared, changed or recovered.
Suggested destination: docs/data.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Data

## Meaning and authority

{{Describe data entities, dictionary/schema authority, classification, producers/consumers and ownership.}}

## Persistence and integrity

{{Explain storage choices, consistency/concurrency, transactions, constraints and relevant query/index assumptions.}}

## Lifecycle and change

{{Record retention/deletion, import/export, migration, compatibility, audit and privacy obligations; link pipeline specifics from an optional data-workload addition.}}

## Recovery and checks

{{Specify backup/restore responsibilities, recovery objectives, integrity checks and actual restore evidence; distinguish targets from observed results.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
