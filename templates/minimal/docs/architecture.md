<!-- OpenDocKit author guidance
ID: base.minimal.docs.architecture.md
Purpose: Explain system boundaries, structure, runtime and significant trade-offs.
Use when: Designing, reviewing or evolving system structure.
Suggested destination: docs/architecture.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Architecture

## Context and constraints

{{Identify system boundary, external actors/dependencies, deployment assumptions and hard constraints; reference product/domain/contract authorities.}}

## Structure and runtime

{{Explain components and responsibilities, critical request/event flows, concurrency, failure handling and deployment/recovery boundaries.}}

## Quality and trade-offs

{{Show how design meets quality requirements; record alternatives, costs, operational consequences and accepted residual risks.}}

## Decisions and evolution

{{Link significant ADRs and compatibility/migration constraints. Identify design intent versus observed implementation and debt owners.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
