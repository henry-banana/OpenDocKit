<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.engineering.codebase-guide.md
Purpose: Orient contributors to responsibilities and change locations.
Use when: Repository structure is too large or surprising to infer quickly.
Suggested destination: docs/engineering/codebase-guide.md
Boundary: The filesystem owns exact listings; document meaning and non-obvious boundaries.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Codebase Guide

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Entry points

{{Identify executable/library entry points, main responsibilities and canonical source locations.}}

## Structure and dependencies

{{Explain relevant modules, permitted dependencies, ownership and generated/vendor boundaries.}}

## Change routes

{{Describe where representative features, tests, contracts and configuration changes belong.}}

## Checks and pitfalls

{{Link required checks and document hidden constraints or recurring errors.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Responsibilities map to source locations.
- [ ] Common change routes are clear.
- [ ] Generated and maintained sources are distinguished.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
