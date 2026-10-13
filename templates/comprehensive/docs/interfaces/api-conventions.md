<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.interfaces.api-conventions.md
Purpose: Record common interface behavior and design conventions.
Use when: Multiple operations need predictable naming, semantics and cross-cutting behavior.
Suggested destination: docs/interfaces/api-conventions.md
Boundary: Contract definitions own concrete fields; conventions explain reusable decisions.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# API Conventions

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Scope and consistency

{{State which interfaces follow these conventions and existing standards they reuse.}}

## Request/response semantics

{{Describe identifiers, pagination, filtering, retries, idempotency and optionality as applicable.}}

## Errors and changes

{{Reference error conventions, compatibility rules and how exceptions are communicated.}}

## Review and enforcement

{{Link lint/tests/design review mechanisms and the owner approving departures.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Conventions address consumer decisions.
- [ ] Exceptions have ownership.
- [ ] Concrete operation facts stay in contracts.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
