<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.domain.invariants.md
Purpose: State properties that must remain true across domain operations.
Use when: Concurrency, partial failure or transitions threaten business correctness.
Suggested destination: docs/domain/invariants.md
Boundary: Keep ordinary validation messages in requirements; focus on always-true domain properties.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Invariants

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Invariant definitions

{{Assign each invariant an ID, scope, business justification and precise predicate.}}

## Threatening operations

{{List writes, concurrent actions, retries and partial failures that could violate it.}}

## Enforcement and checking

{{Link transaction/constraint/test mechanisms and describe residual limits or compensation.}}

## Exceptions and evolution

{{State whether any exception is legal and who can change the invariant.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Predicates are checkable.
- [ ] Concurrency and failure risks are addressed.
- [ ] Enforcement has an authoritative location.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
