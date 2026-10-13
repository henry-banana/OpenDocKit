<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.test-plan.md
Purpose: Specify checks for a particular change, release or risk.
Use when: A verification effort needs defined scope and expected results.
Suggested destination: docs/plans/test-plan-id.md
Boundary: Strategy owns overall method; report owns actual outcomes; test-management tools can own case execution.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Test Plan

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Scope and requirements

{{Link requirement/quality IDs and state included/excluded risk, assumptions and acceptance owner.}}

## Setup and cases

{{Record environment, safe test data, prerequisites, actions and expected outcomes for positive/negative/boundary scenarios.}}

## Execution and evidence

{{Name who runs which checks, how failures/not-run cases are recorded and where evidence lives.}}

## Exit and cleanup

{{State completion/stop criteria, defect handling, retest conditions and data/environment cleanup.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Cases map to the stated risks.
- [ ] Expected outcomes and setup are reproducible.
- [ ] Exit decisions include failures and not-run checks.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
