<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.disaster-recovery.md
Purpose: Plan restoration of service after a major failure.
Use when: Service continuity depends on recoverable infrastructure and state.
Suggested destination: docs/operations/disaster-recovery.md
Boundary: Dataset restore procedures remain their own runbooks; objectives need business authority.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Disaster Recovery

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Failure scope and objectives

{{Describe covered disasters, affected dependencies and approved recovery/loss objectives.}}

## Recovery approach

{{Explain restoration order, identity/config/data sources, alternate operation and resource assumptions.}}

## Execution and reconciliation

{{Link procedures, checks, traffic transition and consistency validation across dependencies.}}

## Exercises and limits

{{Record actual rehearsal evidence or not-run state, known gaps and improvement owners.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Objectives have business authority.
- [ ] Restoration considers dependency order and consistency.
- [ ] Exercises and gaps are reported honestly.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
