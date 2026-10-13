<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.interfaces.event-contracts.md
Purpose: Explain event meaning, delivery assumptions and producer/consumer duties.
Use when: Independent components communicate through messages or events.
Suggested destination: docs/interfaces/event-contracts.md
Boundary: AsyncAPI/schema owns wire definitions; this document owns business semantics.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Event Contracts

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Event catalog

{{Record event meaning, producer, consumers, authoritative schema and occurrence conditions.}}

## Delivery semantics

{{Specify ordering, duplication, replay, retention and timing assumptions without claiming stronger guarantees.}}

## Evolution

{{Describe compatibility, schema rollout and coordination across producer/consumer versions.}}

## Failure and evidence

{{Explain invalid messages, dead-letter handling, reconciliation and consumer verification references.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Event meaning and occurrence are clear.
- [ ] Delivery guarantees are bounded.
- [ ] Evolution and failure duties have owners.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
