<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.interfaces.authentication.md
Purpose: Explain how consumers establish identity and handle credentials.
Use when: An interface requires authentication or has an intentional anonymous boundary.
Suggested destination: docs/interfaces/authentication.md
Boundary: Authorization decisions belong in the authorization model; do not include real secrets.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Authentication

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Identity and flows

{{Describe supported actor/credential types and the authentication sequence with authoritative references.}}

## Credential lifecycle

{{Explain issuance, storage expectations, rotation, expiry, revocation and recovery.}}

## Failure handling

{{Specify consumer behavior for missing/invalid/expired credentials and secure error information.}}

## Verification and ownership

{{Link authentication tests, trusted providers, known limits and the responsible security owner.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Credential lifecycle is explicit.
- [ ] Failure behavior is safe and understandable.
- [ ] Authorization and secret values are not duplicated.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
