<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.security.threat-model.md
Purpose: Analyze credible misuse and prioritize security responses.
Use when: A trust boundary, exposed capability or sensitive workflow changes.
Suggested destination: docs/security/threat-model.md
Boundary: A model is not a certification; verification and residual-risk acceptance need evidence.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Threat Model

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## System and assumptions

{{Scope the model, assets, actors, dependencies, trust boundaries and current/proposed behavior.}}

## Threat scenarios

{{For each threat describe attacker capability, entry point, abused flow, prerequisites and impact.}}

## Controls and decisions

{{Link mitigations, detection, alternatives, residual risk and acceptance authority.}}

## Validation and maintenance

{{Specify checks, open questions, owners and changes that trigger remodeling.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Threats have credible paths and impacts.
- [ ] Controls and residual risk have owners.
- [ ] The model has a verification/update route.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
