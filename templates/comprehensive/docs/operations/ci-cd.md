<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.ci-cd.md
Purpose: Explain the build and delivery pipeline's responsibilities.
Use when: Contributors/operators need to interpret pipeline gates and failures.
Suggested destination: docs/operations/ci-cd.md
Boundary: Actual pipeline configuration is authoritative; this library does not provide a setup sample.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# CI/CD

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Pipeline map

{{Describe stages, inputs/outputs, triggers and canonical configuration sources.}}

## Gates and evidence

{{Explain what checks prove, failure/not-run behavior and approval authority at important transitions.}}

## Credentials and artifacts

{{Describe trust/access boundaries, secret references and artifact/version provenance.}}

## Failure and maintenance

{{Provide diagnosis/escalation routes and ownership of pipeline changes.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Gates explain meaningful evidence.
- [ ] Trust and artifact provenance are clear.
- [ ] Failures have a diagnosis route.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
