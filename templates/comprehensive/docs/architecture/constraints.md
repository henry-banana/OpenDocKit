<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.architecture.constraints.md
Purpose: Record restrictions that bound feasible architectural choices.
Use when: Technology, organizational or external obligations restrict options.
Suggested destination: docs/architecture/constraints.md
Boundary: Distinguish a genuine constraint from an unreviewed preference.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Constraints

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Constraint register

{{Record ID, type, source, scope, owner and whether the constraint is mandatory or negotiable.}}

## Design effects

{{Explain which options are eliminated or made expensive and the dependencies involved.}}

## Exceptions

{{Describe who can grant an exception and what evidence or compensating action is needed.}}

## Review triggers

{{Identify expiry, changed conditions and the process for reconsidering constraints.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Every constraint has a source.
- [ ] Design effects are clear.
- [ ] Negotiable choices are not mislabeled mandatory.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
