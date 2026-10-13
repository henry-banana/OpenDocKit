<!-- OpenDocKit author guidance
ID: data.comprehensive.docs.data-workloads.data-lineage.md
Purpose: Explain how sources affect derived datasets and consumers.
Use when: Impact analysis or governance needs data-flow relationships.
Suggested destination: docs/data-workloads/data-lineage.md
Boundary: Link generated lineage where available instead of copying volatile dependency facts.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Data Lineage

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Scope and authority

{{Name datasets, consumers, lineage source and the precision/coverage of this view.}}

## Relationships

{{Describe source-to-transform-to-output edges, meaning changes and ownership boundaries.}}

## Impact and access

{{Explain affected consumers, sensitive-data propagation and consequences of a source change or deletion.}}

## Gaps and maintenance

{{Record unobserved edges, confidence, validation and update responsibility.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Readers can trace important source-to-consumer paths.
- [ ] Coverage gaps are explicit.
- [ ] Generated facts have a single authority.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
