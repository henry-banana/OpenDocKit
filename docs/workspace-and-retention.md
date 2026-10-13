# Work records, storage and retention

## Shared authority

Current project facts and useful team research/specs/plans/reviews are shared
knowledge. Samples place work records under docs/specs, docs/designs, docs/plans,
docs/tasks and the corresponding record folders. A team's existing tracker can
own live task state instead of duplicating it in Markdown.

Track drafts with their actual proposed state. Maintain active records and
preserve closed evidence with explicit corrections/successors. ADRs record
significant decisions; a roadmap owns direction or points to the tracker. A team
handover differs from a private session-resume handoff.

## Personal work and native resources

The source includes personal samples under .agents/plans, tasks, sessions,
handoffs and artifacts. Shared .agents/skills is a different responsibility.
Actual clients may store runtime history elsewhere; use their supported native
or external personal storage when appropriate. A directory name alone makes
nothing private, ignored or discoverable by a client.

Merge applicable .gitignore.example rules before storing personal output:

```gitignore
/.agents/plans/
/.agents/tasks/
/.agents/sessions/
/.agents/handoffs/
/.agents/artifacts/
/.claude/settings.local.json
```

Root anchors keep the same templates nested in this library visible. Keep shared
skills, team records and selected shared configuration tracked. Already tracked
files remain tracked even after adding ignore rules; removing them from tracking
or public history is a separate reviewed action. Git ignores are not read
permissions, a secret store or a backup policy.

## Retention and parent workspaces

Refresh an active personal handoff with observed goals, checkout, checks, blockers
and next action; verify it when resuming. Retain raw/detailed sessions only for a
named purpose and promote lasting outcomes into shared sources. Set appropriate
confidentiality, access and backup outside the template itself.

Commands, tests and Git operations belong in the actual checkout. A sibling notes
directory can still belong to an ancestor Git repository: check its Git root.
External notes need accessible explicit pointers when agents must read them.

References: [Git ignore semantics](https://git-scm.com/docs/gitignore),
[ADR guidance](https://adr.github.io/).
