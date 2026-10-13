<!-- OpenDocKit author guidance
ID: base.minimal.docs.changes.change-id.verification.md
Purpose: Record what was actually checked and what remains uncertain.
Use when: A change/release needs evidence before an acceptance decision.
Suggested destination: docs/verification/verification-id.md
Boundary: Plans own intended checks; this report owns execution facts and evidence.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Verification Report

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Scope and provenance

{{Record version/change, requirement/check references, environment, runner and actual execution context.}}

## Results

{{For each check report PASS/FAIL/NOT RUN with observed outcome and evidence reference.}}

## Findings and limits

{{Describe defects, coverage gaps, flaky/inconclusive results and their impact on acceptance.}}

## Decision

{{Record responsible review, accepted exceptions and follow-up; do not infer approval from test counts.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Results reference actual execution.
- [ ] Failures and not-run cases remain visible.
- [ ] Acceptance has an accountable decision.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
