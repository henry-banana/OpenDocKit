<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.environments.md
Purpose: Explain the purpose and boundaries of runtime environments.
Use when: Different deployment or test contexts need safe use and ownership.
Suggested destination: docs/operations/environments.md
Boundary: Infrastructure/configuration owns actual values and resource listings.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Environments

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Environment map

{{Describe each environment's purpose, owner, access route and canonical configuration source.}}

## Separation

{{Explain data, identity, secrets, networking and deployment isolation between contexts.}}

## Promotion and use

{{State entry/exit checks, permitted experiments and how changes move between environments.}}

## Lifecycle

{{Describe provisioning/decommissioning authority, cost responsibilities and drift checks.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Environment use and ownership are clear.
- [ ] Sensitive boundaries are explicit.
- [ ] Configuration facts have one source.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
