# Optional agent integration samples

## Select real client resources

Use [INDEX](../INDEX.md#agent-and-personal-workflow) for actual available paths.
Native filenames can be discovered by a client after copying, so select the files
for clients you use and review them before activation. Available samples cover
Codex configuration/AGENTS/skills, Claude rules/settings/reviewer/skills, Copilot
instructions (minimal), Cursor rules, Kiro steering and OpenCode reviewer roles.
No client runtime or credential is installed by this library.

Consult the selected client's current official documentation before changing
settings/frontmatter. Static parsing covers only the shipped syntax and limited
inertness rules. It does not establish client loading or semantic support for an
installed client version. Actual loading trials are NOT RUN unless recorded with
client version, commands and observed evidence.

## Facts, skills and roles

Root instructions route to the adopted project's authoritative docs and checks.
Skills describe scoped repeatable work; role definitions describe responsibility
and allowed output. Shared skills can be tracked while personal plans, tasks,
sessions, handoffs and raw output have their own storage/ignore policy.
See [storage guidance](workspace-and-retention.md).

Generic Claude plugin entries are disabled, and executable hooks are not enabled.
Codex configuration does not supply credentials or a model/provider selection.
Sample reviewer definitions do not authorize delegation in the maintainer repo.

## Plugins and product extensions

Product-extension documents describe extending the team's application. A coding
agent's plugin consumes its vendor's packaging and trust rules; marketplace
publishing is another responsibility. Neither the directory tree nor a workflow
document installs or activates a plugin. Adopt hooks only after checking the
selected client's semantics, execution scope and project needs.
