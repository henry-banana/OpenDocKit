<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.architecture.deployment-view.md
Purpose: Explain how software responsibilities map to runtime infrastructure.
Use when: Operations or architecture decisions depend on placement and environments.
Suggested destination: docs/architecture/deployment-view.md
Boundary: Infrastructure configuration owns exact deployed resources and values.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Deployment View

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Environment topology

{{Describe supported environments, nodes, regions and workload placement with a diagram if useful.}}

## Mapping and dependencies

{{Map components to runtime units and describe networking/storage/external dependencies.}}

## Deployment qualities

{{Explain availability, scaling, isolation and recovery choices against NFR IDs.}}

## Authority and drift

{{Link infrastructure/config sources and state the owner and trigger for updating this view.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Component placement is understandable.
- [ ] Quality trade-offs reference requirements.
- [ ] Infrastructure facts have canonical sources.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
