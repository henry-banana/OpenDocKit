<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.interfaces.versioning.md
Purpose: Explain interface evolution and supported compatibility boundaries.
Use when: Consumers need to plan upgrades or tolerate changing behavior.
Suggested destination: docs/interfaces/versioning.md
Boundary: Release notes record concrete changes; this policy owns version meanings and support decisions.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Versioning

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Version identity

{{Describe how consumers select/identify versions and which dimensions can change independently.}}

## Compatibility classification

{{Define additive, breaking and behavioral changes with examples relevant to this interface.}}

## Transition and support

{{Explain deprecation notices, migration routes, support ownership and agreed transition criteria.}}

## Verification

{{Link compatibility tests and how version decisions are reviewed before release.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Consumers can identify their contract version.
- [ ] Breaking changes have a transition route.
- [ ] Support policy has actual authority.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
