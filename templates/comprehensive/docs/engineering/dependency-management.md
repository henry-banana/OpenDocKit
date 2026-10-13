<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.dependency-management.md
Purpose: Explain dependency selection, updates and provenance responsibilities.
Use when: Third-party packages affect compatibility, security or reproducibility.
Suggested destination: docs/engineering/dependency-management.md
Boundary: Lockfiles/manifests own exact versions; this guide explains the decision process.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Dependency Management

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Inventory and authority

{{Link dependency manifests, lockfiles and relevant direct/transitive ownership.}}

## Selection

{{Describe need evaluation, maintenance/compatibility/licensing checks and alternatives before adding a dependency.}}

## Updates and removal

{{Explain update checks, regression verification, deprecation and how unused dependencies are removed.}}

## Risk response

{{Link vulnerability/provenance handling, escalation and exceptions for constrained updates.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Selection addresses a real need.
- [ ] Versions are reproducible from canonical sources.
- [ ] Updates and known risks have an action route.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
