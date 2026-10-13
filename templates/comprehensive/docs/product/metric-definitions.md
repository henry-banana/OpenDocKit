<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.product.metric-definitions.md
Purpose: Keep measurement meaning consistent across reports and experiments.
Use when: Several consumers calculate or interpret the same metric.
Suggested destination: docs/product/metric-definitions.md
Boundary: Outcome targets remain in success metrics or NFR; executable queries remain in code.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Metric Definitions

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Metric identity

{{State name, purpose, owner, unit, population and the decisions using the metric.}}

## Calculation and source

{{Specify numerator/denominator, window, exclusions, source events/datasets and canonical query reference.}}

## Quality and interpretation

{{Describe missing data, lag, bias, segmentation and known interpretation limits.}}

## Change control

{{Record definition version, compatibility impact, backfill needs and notification/review ownership.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Two readers can reproduce the same meaning.
- [ ] Source and exclusions are explicit.
- [ ] Definition changes identify affected consumers.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
