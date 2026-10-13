<!-- OpenDocKit author guidance
ID: agent-workflow.comprehensive.resources
Purpose: Separate shared native skills from personal work records and raw output.
Use when: Adopting agent workflow resources or personal session continuity samples.
Suggested destination: .agents/README.md
Boundary: Shared team knowledge lives in docs; native clients own their actual runtime/history format.
Adoption: Select needed files, set real tracking rules and fill project-specific retention.
-->
# Agent Resources and Personal Records

## Shared resources

[Skills](skills/template/SKILL.md) can be shared, versioned project resources.
An agent's skills, plugins and settings use that client's supported native format;
this directory does not install or load them automatically.

{{Identify shared native resources, owners and review boundaries for this project.}}

## Personal continuity

Personal [plans](plans/plan-id.md), [tasks](tasks/task-id.md),
[sessions](sessions/session-id.md), [resume handoff](handoffs/HANDOFF.md) and
[raw output guidance](artifacts/README.md) support individual work. Useful lasting
facts and decisions are promoted into the team's docs or tracker.

{{Set actual personal storage, confidentiality, retention and resume verification.}}

## Tracking and maintenance

Merge applicable rules from the root .gitignore.example into the adopting
project's policy before storing private output. The .example file is inert;
already tracked files remain tracked. Keep shared skills visible instead of
ignoring all of .agents. A directory name is not a secret store or read boundary.

{{Confirm these personal record paths are ignored or select external/native storage.}}

## Completion check

- [ ] Shared resources and private records have separate owners and tracking rules.
- [ ] Personal outputs are protected by the actual recipient policy before use.
- [ ] Active handoffs are verified on resume; durable outcomes have shared authority.
