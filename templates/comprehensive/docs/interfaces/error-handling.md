<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.interfaces.error-handling.md
Purpose: Make failures predictable and actionable for consumers.
Use when: Consumers need to distinguish invalid requests, transient faults and conflicts.
Suggested destination: docs/interfaces/error-handling.md
Boundary: The contract owns actual error schema; this guide explains semantics and recovery.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Error Handling

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Error model

{{Link canonical error structure and classify stable error identifiers and public messages.}}

## Recovery behavior

{{Describe retryability, idempotency expectations, backoff authority and required consumer action.}}

## Information boundaries

{{State correlation/support details allowed publicly and sensitive information withheld.}}

## Examples and changes

{{Provide representative failure scenarios and compatibility rules for changing errors.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Error categories guide recovery.
- [ ] Public information boundaries are clear.
- [ ] Schema and compatibility authority are linked.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
