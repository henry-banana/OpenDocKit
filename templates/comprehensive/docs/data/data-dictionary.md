<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.data.data-dictionary.md
Purpose: Keep field meaning and interpretation consistent for data consumers.
Use when: Shared fields need units, semantics or constraints explained.
Suggested destination: docs/data/data-dictionary.md
Boundary: Generate structural facts when possible; do not maintain a second schema by hand.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Data Dictionary

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Dataset context

{{Identify dataset, version/source, owners and consumers using these definitions.}}

## Field semantics

{{For each important field record meaning, units, allowed interpretation and authoritative schema reference.}}

## Missing and exceptional values

{{Explain nulls, defaults, sentinel values, time zones, precision and classification where relevant.}}

## Changes

{{Record compatibility and notification expectations for changed meanings or units.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Units and missing-value semantics are explicit.
- [ ] Structural facts reference schema authority.
- [ ] Meaning changes identify affected consumers.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
