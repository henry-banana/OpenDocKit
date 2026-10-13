<!-- OpenDocKit author guidance
ID: template.comprehensive.AGENTS.md
Purpose: Route the agent to current project facts, actual checks and the right retention.
Use when: This audience or responsibility is relevant to the project.
Suggested destination: AGENTS.md
Boundary: Summaries and navigation link canonical authority; no duplicate live work state.
Adoption: Fill actual facts and sources, adjust links to adopted files, then remove author guidance.
-->
# Project Agent Instructions

## Entry and task scope

Start at [project overview](docs/overview.md) and [documentation map](docs/README.md). Read only relevant sources for the requested task; verify the actual checkout before commands/Git.

{{State project-specific boundaries, protected scope and approval/delegation requirements.}}

## Task routes

Behavior/rules → docs product/domain/interfaces. Structural changes → docs architecture and decisions. UI/component changes → docs experience/components. Checks → docs engineering/quality and verification. Deployment/incidents → docs operations/releases/incidents. Use docs/specs/designs/plans/tasks only when they are the chosen work authority.

## Maintain, verify and report

When a change affects facts or work state, update the authoritative docs/record and affected overview/role summaries. Follow [documentation maintenance](docs/documentation-maintenance.md). Keep personal continuity in .agents; .agents/skills may be shared, so do not blanket-ignore it. Preserve closed evidence and report actual failed/skipped/NOT RUN checks.

{{Link the actual build/test/check commands and working directory; do not invent success or approval.}}

## Completion check

- [ ] Summary statements have current authoritative sources.
- [ ] Adopted paths, owner and review triggers are accurate.
- [ ] Pending decisions/checks and completed evidence remain distinct.
