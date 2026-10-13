<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.data.backup-recovery.md
Purpose: Describe dataset backup and restoration as a data capability.
Use when: Persisted data needs a recoverable state.
Suggested destination: docs/data/backup-recovery.md
Boundary: System-wide disaster recovery lives in operations; focus on this dataset/store.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Backup Recovery

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Recovery objectives

{{Link agreed loss/downtime objectives and explain data consistency required after restoration.}}

## Backup coverage

{{Describe sources, scope, schedule authority, encryption/access and known omissions.}}

## Restore and reconcile

{{Link restore procedure, consistency checks, downstream reconciliation and failure escalation.}}

## Evidence and review

{{Record actual restore exercises or not-run status, findings and responsible owners.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Backup coverage matches critical state.
- [ ] Restoration includes consistency checks.
- [ ] Backup success is not treated as restore evidence.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
