<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.branching-strategy.md
Purpose: Explain how changes reach supported branches and releases.
Use when: Several contributors or release lines need integration conventions.
Suggested destination: docs/engineering/branching-strategy.md
Boundary: Repository protection and CI config own enforced settings.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Branching Strategy

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Branch purposes

{{Describe current branch roles, support windows and the authority deciding them.}}

## Change flow

{{Explain how contributors start work, review, integrate and coordinate dependent changes.}}

## Release and fixes

{{Describe hotfix/backport expectations, compatibility decisions and recovery when integration fails.}}

## Evidence and policy

{{Link enforced platform policy, required checks and exceptions ownership.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Branch roles serve the release model.
- [ ] Fix and backport flows are clear.
- [ ] Enforced rules have a canonical source.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
