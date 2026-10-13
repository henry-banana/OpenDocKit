<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.capacity-planning.md
Purpose: Explain expected workload and decisions about system limits.
Use when: Growth, seasonality or dependencies threaten performance/reliability.
Suggested destination: docs/operations/capacity-planning.md
Boundary: Actual metrics and resource config remain in their canonical systems.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Capacity Planning

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Demand model

{{Describe user/workload drivers, evidence, peak scenarios and uncertainty in forecasts.}}

## Constraints and headroom

{{Link measured limits, dependency quotas, agreed performance targets and resource assumptions.}}

## Response options

{{Compare scaling, optimization, admission limits and cost/reliability trade-offs.}}

## Review triggers

{{Name thresholds for investigation, decision ownership and next measurement needed.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Forecasts show uncertainty and source.
- [ ] Limits reference measurements.
- [ ] Capacity responses have triggers and owners.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
