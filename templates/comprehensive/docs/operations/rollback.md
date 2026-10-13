<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.operations.rollback.md
Purpose: Describe recovery from a harmful deployment or change.
Use when: A release may need reversal or forward repair.
Suggested destination: docs/operations/rollback.md
Boundary: Do not assume persisted-data changes are reversible; link migration-specific constraints.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Rollback

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Trigger and authority

{{State observed stop conditions, version scope and who may initiate recovery.}}

## Compatibility and state

{{Describe artifact/config/schema combinations, data consequences and irreversible changes.}}

## Recovery sequence

{{Link verified rollback or forward-repair steps and dependencies that must be coordinated.}}

## Verification and communication

{{Define restored-behavior checks, reconciliation, stakeholder updates and follow-up evidence.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Recovery is compatible with persisted state.
- [ ] Irreversible changes have forward-repair plans.
- [ ] Restoration has observable verification.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
