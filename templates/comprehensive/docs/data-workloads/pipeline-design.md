<!-- OpenDocKit author guidance
ID: data.comprehensive.docs.data-workloads.pipeline-design.md
Purpose: Explain transformation, orchestration and recovery of a data pipeline.
Use when: A pipeline has ordering, quality or failure behavior worth reviewing.
Suggested destination: docs/data-workloads/pipeline-design.md
Boundary: Code and orchestration configuration own exact transformations/schedules.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Pipeline Design

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Inputs and outputs

{{Describe sources, sinks, semantics, dependencies, owners and intended consumption.}}

## Processing stages

{{Explain transformations, checkpoints, partitioning and relevant ordering/concurrency decisions.}}

## Failures and replay

{{Address idempotency, retries, duplicate/corrupt data, late arrival and reprocessing boundaries.}}

## Quality and operations

{{Link checks, freshness measures, access controls and runbooks for degraded processing.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Stage semantics are understandable.
- [ ] Replay and failure assumptions are explicit.
- [ ] Quality and operational checks have owners.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
