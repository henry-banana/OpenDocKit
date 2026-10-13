<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.architecture.building-blocks.md
Purpose: Describe internal responsibilities and dependencies at useful depth.
Use when: Developers need to understand modules or subsystems before changing them.
Suggested destination: docs/architecture/building-blocks.md
Boundary: Document risky or surprising detail; code remains the implementation authority.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Building Blocks

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Decomposition

{{Show the overall structure and explain the reason for its boundaries.}}

## Block responsibilities

{{For each relevant block state purpose, interfaces, owner and source-code location.}}

## Dependencies

{{Describe permitted dependencies, shared services, coupling risks and enforcement references.}}

## Focused detail

{{Expand complex or volatile blocks with internal responsibilities and requirements they satisfy.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Blocks have distinct responsibilities.
- [ ] Dependencies and source locations are navigable.
- [ ] Detail depth serves a reader task.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
