<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.domain.business-workflows.md
Purpose: Describe actors and business state across an end-to-end process.
Use when: A process crosses roles, approvals or bounded contexts.
Suggested destination: docs/domain/business-workflows.md
Boundary: UI navigation and runtime implementation are separate views.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Business Workflows

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Entry and outcome

{{State the initiating event, prerequisites, participants and business completion condition.}}

## Steps and responsibility

{{For each step record actor, action, state change, required decision and handoff.}}

## Exceptions and recovery

{{Describe timeout, rejection, cancellation, duplicate requests and manual intervention paths.}}

## Controls and evidence

{{Link applicable rules, approvals and records proving the business outcome.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Handoffs have responsible actors.
- [ ] Failure and cancellation paths are described.
- [ ] Completion is a business outcome.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
