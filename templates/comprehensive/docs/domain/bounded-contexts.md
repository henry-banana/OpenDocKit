<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.domain.bounded-contexts.md
Purpose: Identify where business meaning and responsibility change.
Use when: Multiple domains use different models or ownership boundaries.
Suggested destination: docs/domain/bounded-contexts.md
Boundary: A context is not automatically a microservice or deployment unit.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Bounded Contexts

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Context map

{{Name each context, purpose, vocabulary, owner and model boundary.}}

## Interactions

{{Describe upstream/downstream relationships, shared concepts and integration responsibilities.}}

## Translation and authority

{{Identify canonical sources, translation rules and which context decides disputed facts.}}

## Evolution

{{Record coupling risks, boundary-change triggers and affected consumers.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Each boundary has a meaning and owner.
- [ ] Cross-context translations are explicit.
- [ ] Deployment choices are not assumed.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
