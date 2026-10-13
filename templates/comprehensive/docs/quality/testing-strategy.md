<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.testing-strategy.md
Purpose: Explain how verification effort addresses system risks.
Use when: A team needs shared expectations across testing layers.
Suggested destination: docs/quality/testing-strategy.md
Boundary: Scoped test plans choose cases; actual results belong in verification reports.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Testing Strategy

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Risks and scope

{{Identify critical behavior, quality requirements and risks the strategy must address.}}

## Layers and methods

{{Explain unit/integration/system/manual or other methods and why each is useful here.}}

## Environments and data

{{Describe isolation, representative inputs, flakiness control and safe data handling.}}

## Decision and maintenance

{{State release/change evidence expectations, ownership, coverage gaps and review triggers.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Methods correspond to actual risks.
- [ ] Data and environments support trustworthy results.
- [ ] Gaps and evidence expectations are explicit.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
