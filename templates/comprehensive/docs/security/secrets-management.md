<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.security.secrets-management.md
Purpose: Explain secure credential handling throughout its lifecycle.
Use when: A project uses keys, tokens or private configuration.
Suggested destination: docs/security/secrets-management.md
Boundary: Use references to approved storage; never put secret values or personal credentials here.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Secrets Management

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Inventory and access

{{Identify secret classes, consumers, storage authority and access ownership without exposing values.}}

## Lifecycle

{{Describe provisioning, delivery, rotation, revocation and expiration responsibilities.}}

## Local and CI use

{{Explain safe developer/pipeline access, redaction and separation between environments.}}

## Incident response

{{Link leak detection, revocation/recovery steps and checks confirming removed access.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Secret values are absent.
- [ ] Rotation and revocation have owners.
- [ ] Environment access and incident response are clear.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
