<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.data.persistence.md
Purpose: Explain storage choices and access semantics.
Use when: Developers/operators need to understand how state is stored and protected.
Suggested destination: docs/data/persistence.md
Boundary: Exact topology/configuration stays in infrastructure and migrations.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Persistence

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Storage responsibilities

{{Describe stores, data ownership, lifecycle and architectural decisions behind their use.}}

## Read/write semantics

{{Explain transactions, isolation, concurrency, caching and consistency assumptions.}}

## Failure and durability

{{Address partial writes, retries, corruption, recovery and enforcement of domain invariants.}}

## Operations and evolution

{{Link migrations, observability, access controls, capacity and recovery procedures.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Consistency and durability expectations are bounded.
- [ ] Failure paths protect invariants.
- [ ] Operational authority is discoverable.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
