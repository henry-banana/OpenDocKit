<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.architecture.crosscutting-concepts.md
Purpose: Explain design approaches used across multiple components.
Use when: Shared mechanisms need consistent application and interpretation.
Suggested destination: docs/architecture/crosscutting-concepts.md
Boundary: Component-specific behavior stays in scoped designs or contracts.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Crosscutting Concepts

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Concept catalog

{{Identify shared concerns such as identity, transactions, errors, caching and observability.}}

## Approach and rationale

{{For each concern state the chosen approach, scope, assumptions and relevant decision references.}}

## Application rules

{{Explain how components apply the approach and where exceptions are permitted.}}

## Evidence and evolution

{{Link enforcement/tests and describe consequences of changing the shared approach.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Shared approaches have a scope.
- [ ] Exceptions and enforcement are visible.
- [ ] Component facts are not duplicated.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
