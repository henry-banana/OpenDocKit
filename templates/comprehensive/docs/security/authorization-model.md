<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.security.authorization-model.md
Purpose: Describe who may perform actions on which resources.
Use when: Permissions influence behavior, security or business ownership.
Suggested destination: docs/security/authorization-model.md
Boundary: Authentication establishes identity; policy code owns executable evaluation.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Authorization Model

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Subjects and resources

{{Define actor/resource types, tenancy, ownership and trusted identity attributes.}}

## Decisions

{{Record action, conditions, scope, default outcome and policy source for important permissions.}}

## Edge cases

{{Cover delegation, revocation, cross-tenant access, state changes and administrative exceptions.}}

## Verification

{{Link allow/deny tests, audit evidence and authority for policy changes.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Permission scope and defaults are explicit.
- [ ] Deny and cross-boundary cases are considered.
- [ ] Policies map to checks.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
