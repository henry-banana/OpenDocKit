<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.observability.md
Purpose: Explain signals used to understand behavior and act on problems.
Use when: A running system needs diagnosis, measurement or alert decisions.
Suggested destination: docs/operations/observability.md
Boundary: Dashboards/rules/config own signal definitions; this document explains why/how to use them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Observability

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Questions and signals

{{Map user/system questions to logs, metrics, traces or other signals and canonical sources.}}

## Context and privacy

{{Describe correlation, cardinality, access, sensitive-data handling and retention limits.}}

## Action and diagnosis

{{Link alert conditions to ownership, runbooks, dashboards and decision expectations.}}

## Coverage and quality

{{Record blind spots, sampling/lag limits, verification and changes affecting signals.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Signals answer operational questions.
- [ ] Alerts have actionable ownership.
- [ ] Privacy and coverage limits are visible.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
