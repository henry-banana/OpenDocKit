<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.architecture.system-context.md
Purpose: Show the system boundary and external relationships.
Use when: Dependencies or users need a shared boundary view.
Suggested destination: docs/architecture/system-context.md
Boundary: Do not confuse context relationships with internal component structure.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# System Context

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Boundary

{{Define the system being described, responsibilities in scope and what remains external.}}

## Actors and neighbors

{{List human roles, external systems, their owners and the purpose of each interaction.}}

## Information flows

{{Describe exchanged information, trust boundaries, interfaces and failure assumptions.}}

## Constraints and changes

{{Record dependency limitations and changes that would require updating the context.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] System boundary is explicit.
- [ ] External dependencies have owners.
- [ ] Trust and information flows are visible.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
