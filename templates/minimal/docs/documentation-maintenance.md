<!-- OpenDocKit author guidance
ID: template.minimal.docs.documentation-maintenance.md
Purpose: Keep current facts, working records and reader summaries accurate.
Use when: A change affects behavior, design, contracts, work state or documentation.
Suggested destination: docs/documentation-maintenance.md
Boundary: One fact owner; local scratch and historical evidence are not competing current truth.
Adoption: Copy manually, fill actual facts and source links, then remove author guidance.
-->
# Documentation Maintenance

## Current knowledge

Update the authoritative current docs with behavior/design/contract changes. Specs describe requirements at their stated scope; distinguish current capability specifications from a proposed change and name the authority.

{{Assign owners, source links and meaningful review triggers rather than arbitrary auto-generated timestamps.}}

## Active and closed records

Maintain active shared specs/designs/plans/tasks through scope/dependency/decision changes. Keep draft/accepted/blocked/completed states honest. A tracker or local task records own live status once. After closure preserve history; corrections/successors are explicit rather than silently rewriting past intent.

## Summaries and navigation

overview.md and roles/ pages contain concise sourced summaries, important risks and task routes. Refresh them when linked authoritative facts change; record reviewed sources/revisions. Adjust links when adopting/deleting optional folders. A summary references live work authority rather than copying a mutable backlog.

## Personal continuity and promotion

Keep private plans/tasks/sessions/handoffs and raw output in .agents/ or native/external personal storage. Merge root .gitignore.example rules into the adopted project policy; the library example does not activate itself. Refresh one active handoff, verify it on resume and promote useful lasting outcomes into shared sources. Shared native skills remain in .agents/skills.

{{Name confidentiality/retention and evidence publication boundaries for this project.}}

## Open questions

{{Name unresolved decisions, owners and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Changed canonical sources and affected summaries/routes are updated together.
- [ ] Active records are maintained; historical corrections are traceable.
- [ ] No duplicate live tracker/task state or invented check/approval exists.
- [ ] Personal/raw content is deliberately retained and shared only when appropriate.
