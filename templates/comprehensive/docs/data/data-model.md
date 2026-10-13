<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.data.data-model.md
Purpose: Explain persisted/shared concepts and their relationships.
Use when: Data meaning and lifecycle are not obvious from the schema.
Suggested destination: docs/data/data-model.md
Boundary: The live schema/migrations own storage structure; this view explains meaning.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Data Model

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Scope and authority

{{Name datasets/stores, owners, schema sources and the conceptual/physical boundary.}}

## Entities and relationships

{{Explain identity, cardinality, ownership and business meaning for important structures.}}

## State and consistency

{{Describe lifecycle, consistency assumptions, invariant enforcement and relevant transitions.}}

## Evolution and risks

{{Link migrations, compatibility, sensitive-data handling and known model limitations.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Meaning and schema sources are clear.
- [ ] Identity and consistency assumptions are explicit.
- [ ] Evolution and privacy implications are linked.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
