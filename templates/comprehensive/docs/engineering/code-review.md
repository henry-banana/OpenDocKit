<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.code-review.md
Purpose: Guide review toward correctness, maintainability and observable requirements.
Use when: Contributions need a predictable, useful review process.
Suggested destination: docs/engineering/code-review.md
Boundary: Tool policy owns merge permissions; review guidance does not replace test execution.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Code Review

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Review preparation

{{Identify scope, requirement/design references, change description and evidence supplied by the author.}}

## Review dimensions

{{Check behavior, failure/concurrency/security cases, complexity, useful tests and affected docs.}}

## Discussion and decisions

{{Distinguish blocking findings from suggestions and record rationale for accepted trade-offs.}}

## Completion

{{State reviewer responsibilities, unresolved findings and actual checks required before integration.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Review covers behavior and important failure modes.
- [ ] Feedback distinguishes severity and rationale.
- [ ] Evidence is actual rather than assumed.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
