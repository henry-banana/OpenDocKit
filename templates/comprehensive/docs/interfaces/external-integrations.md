<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.interfaces.external-integrations.md
Purpose: Describe responsibility and failure handling across third-party boundaries.
Use when: A product depends on an external system or provider.
Suggested destination: docs/interfaces/external-integrations.md
Boundary: Provider documentation owns its API details; link the supported version.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# External Integrations

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Integration purpose

{{Describe the capability, provider, owner, trust boundary and authoritative contract/documentation.}}

## Data and identity

{{Explain data exchanged, identity/permission model, classification and retention implications.}}

## Failure and limits

{{Address timeouts, retries, quotas, outages, reconciliation and provider change signals.}}

## Operations and exit

{{Link monitoring, support escalation, sandbox checks and replacement/decommissioning considerations.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Provider facts have a source/version.
- [ ] Failure and reconciliation behavior are understood.
- [ ] Integration ownership and exit are defined.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
