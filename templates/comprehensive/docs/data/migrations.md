<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.data.migrations.md
Purpose: Describe safe evolution of stored data and schema.
Use when: A change affects persisted state or consumers of it.
Suggested destination: docs/data/migrations.md
Boundary: Migration scripts own executable steps; this record owns rationale, compatibility and evidence.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Migrations

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Change and affected consumers

{{Describe old/new semantics, scale, dependencies and the reason for the migration.}}

## Transition sequence

{{Link scripts and order deploy/backfill/cleanup operations, including mixed-version operation.}}

## Failure and recovery

{{Define stop signals, verification, rollback or forward repair and irreversible steps.}}

## Evidence and ownership

{{Record rehearsals or not-run state, reviewers, execution ownership and completion evidence.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Mixed-version behavior is considered.
- [ ] Irreversible steps and recovery are explicit.
- [ ] Completion has checks and an owner.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
