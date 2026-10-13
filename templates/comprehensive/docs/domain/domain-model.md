<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.domain.domain-model.md
Purpose: Describe business concepts, relationships and lifecycle semantics.
Use when: Rules depend on entities, value objects, roles or transitions.
Suggested destination: docs/domain/domain-model.md
Boundary: This is a conceptual model, not a copy of database tables or classes.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Domain Model

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Concepts and identity

{{Describe each business concept, its identity, lifecycle and relevant examples.}}

## Relationships and boundaries

{{Show associations, cardinality, ownership and context boundaries with their business meaning.}}

## Behavior and invariants

{{Link rules, legal state transitions and constraints that must hold across operations.}}

## Uncertainty and validation

{{Record disputed definitions and scenarios reviewed with domain stakeholders.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Identity and relationships have business meaning.
- [ ] Transitions link to rules and invariants.
- [ ] Stakeholder uncertainties are visible.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
