<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.security.security-architecture.md
Purpose: Explain how security controls protect assets across trust boundaries.
Use when: System design contains identity, sensitive data or exposed interfaces.
Suggested destination: docs/security/security-architecture.md
Boundary: Threat model identifies risk; code/configuration owns control implementation.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Security Architecture

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Assets and boundaries

{{Describe protected assets, classifications, actors, trust zones and relevant architecture references.}}

## Control approach

{{Explain identity, isolation, data protection and detection choices against security requirements.}}

## Failure and residual risk

{{Describe degraded control behavior, dependency failures and accepted gaps with authority.}}

## Verification and ownership

{{Link control checks, threat references, operational response and update owners.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Controls map to assets and threats.
- [ ] Failure and residual risk are explicit.
- [ ] Implementation and verification sources are reachable.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
