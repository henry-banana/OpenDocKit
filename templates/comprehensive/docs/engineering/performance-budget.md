<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.performance-budget.md
Purpose: Record agreed limits that guide performance decisions.
Use when: A change could exceed latency, size, throughput or resource expectations.
Suggested destination: docs/engineering/performance-budget.md
Boundary: NFR owns targets; this record binds applicable limits to measured conditions and references.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Performance Budget

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Scope and authority

{{Link requirement IDs, approving owner and the user/system scenario governed by each budget.}}

## Budget definitions

{{Record metric, unit, limit source, workload/device/network conditions and measurement procedure.}}

## Trade-offs and exceptions

{{Describe competing goals, approved deviations, duration and who accepts their consequences.}}

## Enforcement

{{Link measurement checks, alert/review actions and how the budget changes when evidence improves.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Limits have an approved source.
- [ ] Measurement conditions are specified.
- [ ] Exceeding a budget leads to an owned decision.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
