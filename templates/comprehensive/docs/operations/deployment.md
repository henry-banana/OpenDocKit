<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.deployment.md
Purpose: Guide an operator through a controlled deployment.
Use when: A runtime change requires repeatable execution and checks.
Suggested destination: docs/operations/deployment.md
Boundary: Pipeline/IaC owns executable configuration; release checklist owns readiness decisions.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Deployment

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Prerequisites

{{Identify artifact/version, environment, permissions, change authority and required readiness evidence.}}

## Execution

{{Link verified commands/pipeline with working directory, dependencies, sequence and expected state.}}

## Verification and stop

{{Define observable health/behavior checks, stop conditions and decision owner.}}

## Recovery and handoff

{{Link rollback/forward repair, monitoring window, communication and ownership transfer.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Execution is reproducible from canonical sources.
- [ ] Stop and verification signals are explicit.
- [ ] Recovery and handoff are reachable.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
