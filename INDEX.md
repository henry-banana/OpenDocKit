# Template Index

Browse by the information you need, then choose one representation. Every source
file lives under `templates/minimal/` or `templates/comprehensive/`; paths beneath
that root map to your adopting project. See [README](README.md#quick-start) for
copying and [CONTRIBUTING](CONTRIBUTING.md#author-templates) for authoring rules.

This index follows the actual source tree. A listed file is an available sample,
not a requirement to adopt it or a claim that every source reference is already
consistent. See [current maintenance limits](CONTRIBUTING.md#current-maintenance-limits).

- [Start and navigate](#start-and-navigate)
- [Current project knowledge](#current-project-knowledge)
- [Project-specific concerns](#project-specific-concerns)
- [Shared work records](#shared-work-records)
- [Role briefs](#role-briefs)
- [Agent and personal workflow](#agent-and-personal-workflow)
- [Repository essentials](#repository-essentials)
- [Interface contracts](#interface-contracts)
- [All source files](#all-source-files)

## Start and navigate

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| Project introduction | [README.md](templates/minimal/README.md) | [README.md](templates/comprehensive/README.md) |
| Documentation map | [docs/README.md](templates/minimal/docs/README.md) | [docs/README.md](templates/comprehensive/docs/README.md) |
| Project overview and TL;DR | [docs/overview.md](templates/minimal/docs/overview.md) | [docs/overview.md](templates/comprehensive/docs/overview.md) |
| Documentation maintenance | [docs/documentation-maintenance.md](templates/minimal/docs/documentation-maintenance.md) | [docs/documentation-maintenance.md](templates/comprehensive/docs/documentation-maintenance.md) |
| Project context | [CONTEXT.md](templates/minimal/CONTEXT.md) | [CONTEXT.md](templates/comprehensive/CONTEXT.md) |
| Repository roadmap | [ROADMAP.md](templates/minimal/ROADMAP.md) | [ROADMAP.md](templates/comprehensive/ROADMAP.md) |

## Current project knowledge

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| Business need, value and stakeholders | [docs/business.md](templates/minimal/docs/business.md) | [docs/business/](templates/comprehensive/docs/business/) |
| Users, requirements and acceptance | [docs/product.md](templates/minimal/docs/product.md) | [docs/product/](templates/comprehensive/docs/product/) |
| System structure and tradeoffs | [docs/architecture.md](templates/minimal/docs/architecture.md) | [docs/architecture/](templates/comprehensive/docs/architecture/) |
| Terms, rules, states and invariants | [docs/domain.md](templates/minimal/docs/domain.md) | [docs/domain/](templates/comprehensive/docs/domain/) |
| APIs, events and integrations | [docs/interfaces.md](templates/minimal/docs/interfaces.md) | [docs/interfaces/](templates/comprehensive/docs/interfaces/) |
| Data ownership, models and lifecycle | [docs/data.md](templates/minimal/docs/data.md) | [docs/data/](templates/comprehensive/docs/data/) |
| UX, interaction and accessibility | [docs/experience.md](templates/minimal/docs/experience.md) | [docs/experience/](templates/comprehensive/docs/experience/) |
| Component-specific development | [docs/components.md](templates/minimal/docs/components.md) | [docs/components/](templates/comprehensive/docs/components/) |
| Development and review conventions | [docs/engineering.md](templates/minimal/docs/engineering.md) | [docs/engineering/](templates/comprehensive/docs/engineering/) |
| Quality and test strategy | [docs/quality.md](templates/minimal/docs/quality.md) | [docs/quality/](templates/comprehensive/docs/quality/) |
| Threats, privacy and controls | [docs/security.md](templates/minimal/docs/security.md) | [docs/security/](templates/comprehensive/docs/security/) |
| Deployment, reliability and recovery | [docs/operations.md](templates/minimal/docs/operations.md) | [docs/operations/](templates/comprehensive/docs/operations/) |
| Work, release and feedback conventions | [docs/delivery.md](templates/minimal/docs/delivery.md) | [docs/delivery/](templates/comprehensive/docs/delivery/) |
| User learning and reference | [docs/user-documentation.md](templates/minimal/docs/user-documentation.md) | [docs/user-documentation/](templates/comprehensive/docs/user-documentation/) |

Use architecture for system boundaries and components for implementation-specific
ownership and conventions. The comprehensive component map includes
[frontend](templates/comprehensive/docs/components/frontend/README.md) and
[backend](templates/comprehensive/docs/components/backend/README.md) samples.

## Project-specific concerns

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| HTTP/services and asynchronous processing | [docs/service.md](templates/minimal/docs/service.md) | [docs/service/](templates/comprehensive/docs/service/) |
| Mobile devices, offline behavior and stores | [docs/mobile.md](templates/minimal/docs/mobile.md) | [docs/mobile/](templates/comprehensive/docs/mobile/) |
| Desktop platform/distribution concerns | [docs/desktop.md](templates/minimal/docs/desktop.md) | [docs/desktop/](templates/comprehensive/docs/desktop/) |
| CLI and public library interfaces | [docs/cli-library.md](templates/minimal/docs/cli-library.md) | [docs/cli-library/](templates/comprehensive/docs/cli-library/) |
| Data pipelines and workloads | [docs/data-workloads.md](templates/minimal/docs/data-workloads.md) | [docs/data-workloads/](templates/comprehensive/docs/data-workloads/) |
| Model/prompt systems and evaluation | [docs/ai-systems.md](templates/minimal/docs/ai-systems.md) | [docs/ai-systems/](templates/comprehensive/docs/ai-systems/) |
| Game systems and asset pipelines | [docs/game.md](templates/minimal/docs/game.md) | [docs/game/](templates/comprehensive/docs/game/) |
| Embedded hardware/firmware constraints | [docs/embedded.md](templates/minimal/docs/embedded.md) | [docs/embedded/](templates/comprehensive/docs/embedded/) |
| Extensions to a host product | [docs/product-extension.md](templates/minimal/docs/product-extension.md) | [docs/product-extension/](templates/comprehensive/docs/product-extension/) |

Add relevant files from the same representation. Product extensions describe
extending a host application; configuring an AI agent's skills/plugins is a
separate concern in the workflow samples below.

## Shared work records

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| Research findings and experiments | [docs/research/](templates/minimal/docs/research/) | [docs/research/](templates/comprehensive/docs/research/) |
| Requirements, scoped specifications and proposals | [docs/specs/](templates/minimal/docs/specs/) | [docs/specs/](templates/comprehensive/docs/specs/) |
| Solution/design records | [docs/designs/](templates/minimal/docs/designs/) | [docs/designs/](templates/comprehensive/docs/designs/) |
| Implementation, testing and migration plans | [docs/plans/](templates/minimal/docs/plans/) | [docs/plans/](templates/comprehensive/docs/plans/) |
| Tasks and work breakdown | [docs/tasks/](templates/minimal/docs/tasks/) | [docs/tasks/](templates/comprehensive/docs/tasks/) |
| Architectural decision records | [docs/decisions/](templates/minimal/docs/decisions/) | [docs/decisions/](templates/comprehensive/docs/decisions/) |
| Reviews, feedback and findings | [docs/reviews/](templates/minimal/docs/reviews/) | [docs/reviews/](templates/comprehensive/docs/reviews/) |
| Observed verification results | [docs/verification/](templates/minimal/docs/verification/) | [docs/verification/](templates/comprehensive/docs/verification/) |
| Sprint planning and retrospectives | [docs/sprints/](templates/minimal/docs/sprints/) | [docs/sprints/](templates/comprehensive/docs/sprints/) |
| Release notes, checklists and migrations | [docs/releases/](templates/minimal/docs/releases/) | [docs/releases/](templates/comprehensive/docs/releases/) |
| Incident investigation and learning | [docs/incidents/](templates/minimal/docs/incidents/) | [docs/incidents/](templates/comprehensive/docs/incidents/) |
| Shared delivery/ownership handoffs | [docs/handoffs/](templates/minimal/docs/handoffs/) | [docs/handoffs/](templates/comprehensive/docs/handoffs/) |

Rename record placeholders such as `spec-id.md` or `plan-id.md` to meaningful
project identifiers. Link related records by that identifier; a shared task
tracker can own live task state instead of duplicating it here. Maintain active
records and preserve closed history with explicit corrections or successors.
Portable request samples also live in
[minimal delivery requests](templates/minimal/docs/delivery/requests/) and
[comprehensive delivery requests](templates/comprehensive/docs/delivery/requests/).

## Role briefs

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| Business analyst | [docs/roles/ba.md](templates/minimal/docs/roles/ba.md) | [docs/roles/ba.md](templates/comprehensive/docs/roles/ba.md) |
| Product owner | [docs/roles/po.md](templates/minimal/docs/roles/po.md) | [docs/roles/po.md](templates/comprehensive/docs/roles/po.md) |
| Project manager | [docs/roles/pm.md](templates/minimal/docs/roles/pm.md) | [docs/roles/pm.md](templates/comprehensive/docs/roles/pm.md) |
| Engineering | [docs/roles/engineering.md](templates/minimal/docs/roles/engineering.md) | [docs/roles/engineering.md](templates/comprehensive/docs/roles/engineering.md) |
| QA / quality control | [docs/roles/qa.md](templates/minimal/docs/roles/qa.md) | [docs/roles/qa.md](templates/comprehensive/docs/roles/qa.md) |
| Operations | [docs/roles/operations.md](templates/minimal/docs/roles/operations.md) | [docs/roles/operations.md](templates/comprehensive/docs/roles/operations.md) |

The [minimal role map](templates/minimal/docs/roles/README.md) and
[comprehensive role map](templates/comprehensive/docs/roles/README.md) route readers
to summaries and authoritative documents. A role brief summarizes relevant facts,
risks and next actions; it does not create another requirements/backlog authority.

## Agent and personal workflow

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| Shared agent resources / personal storage | [.agents/README.md](templates/minimal/.agents/README.md) | [.agents/README.md](templates/comprehensive/.agents/README.md) |
| Team workflow, responsibilities and verification | [docs/agent-workflow.md](templates/minimal/docs/agent-workflow.md) | [docs/agent-workflow/](templates/comprehensive/docs/agent-workflow/) |
| Root agent instructions | [AGENTS.md](templates/minimal/AGENTS.md) | [AGENTS.md](templates/comprehensive/AGENTS.md) |
| Documentation agent instructions | [docs/AGENTS.md](templates/minimal/docs/AGENTS.md) | [docs/AGENTS.md](templates/comprehensive/docs/AGENTS.md) |
| Portable skill definition | [.agents/skills/template/SKILL.md](templates/minimal/.agents/skills/template/SKILL.md) | [.agents/skills/template/SKILL.md](templates/comprehensive/.agents/skills/template/SKILL.md) |
| Personal plan | [.agents/plans/plan-id.md](templates/minimal/.agents/plans/plan-id.md) | [.agents/plans/plan-id.md](templates/comprehensive/.agents/plans/plan-id.md) |
| Personal task record | [.agents/tasks/task-id.md](templates/minimal/.agents/tasks/task-id.md) | [.agents/tasks/task-id.md](templates/comprehensive/.agents/tasks/task-id.md) |
| Personal session record | [.agents/sessions/session-id.md](templates/minimal/.agents/sessions/session-id.md) | [.agents/sessions/session-id.md](templates/comprehensive/.agents/sessions/session-id.md) |
| Personal resume handoff | [.agents/handoffs/HANDOFF.md](templates/minimal/.agents/handoffs/HANDOFF.md) | [.agents/handoffs/HANDOFF.md](templates/comprehensive/.agents/handoffs/HANDOFF.md) |
| Raw output guidance | [.agents/artifacts/README.md](templates/minimal/.agents/artifacts/README.md) | [.agents/artifacts/README.md](templates/comprehensive/.agents/artifacts/README.md) |
| Claude shared settings / disabled plugin sample | [.claude/settings.json](templates/minimal/.claude/settings.json) | [.claude/settings.json](templates/comprehensive/.claude/settings.json) |
| Claude instructions | [.claude/rules/project.md](templates/minimal/.claude/rules/project.md) | [.claude/rules/project.md](templates/comprehensive/.claude/rules/project.md) |
| Claude reviewer definition | [.claude/agents/reviewer.md](templates/minimal/.claude/agents/reviewer.md) | [.claude/agents/reviewer.md](templates/comprehensive/.claude/agents/reviewer.md) |
| Claude project skill | [.claude/skills/project-review/SKILL.md](templates/minimal/.claude/skills/project-review/SKILL.md) | [.claude/skills/project-review/SKILL.md](templates/comprehensive/.claude/skills/project-review/SKILL.md) |
| Codex project configuration | [.codex/config.toml](templates/minimal/.codex/config.toml) | [.codex/config.toml](templates/comprehensive/.codex/config.toml) |
| Cursor rules | [.cursor/rules/project.mdc](templates/minimal/.cursor/rules/project.mdc) | [.cursor/rules/project.mdc](templates/comprehensive/.cursor/rules/project.mdc) |
| Kiro steering | [.kiro/steering/project.md](templates/minimal/.kiro/steering/project.md) | [.kiro/steering/project.md](templates/comprehensive/.kiro/steering/project.md) |
| OpenCode reviewer definition | [.opencode/agents/reviewer.md](templates/minimal/.opencode/agents/reviewer.md) | [.opencode/agents/reviewer.md](templates/comprehensive/.opencode/agents/reviewer.md) |

Additional samples:

- [Copilot repository instructions](templates/minimal/.github/copilot-instructions.md)
  are currently available in minimal only; adapt them explicitly if needed in a
  comprehensive recipient.
- [Hook adoption guidance — minimal](templates/minimal/docs/agent-workflow/hook-adoption.md)
  and [comprehensive](templates/comprehensive/docs/agent-workflow/hook-adoption.md)
  explain project-specific setup; these are documents, not enabled hooks.
- [Git ignore example](templates/comprehensive/.gitignore.example) is available in both representations: [minimal](templates/minimal/.gitignore.example)
  and comprehensive. Merge applicable rules into the adopting project's
  `.gitignore`; an `.example` file does not activate rules.

Personal record samples currently sit under `.agents/` in the source tree. That
name does not make them private or ignored, and the ignore example takes effect only after it is merged into the recipient
policy. Set the intended destination and tracking deliberately.
Shared `.agents/skills/` and private session/raw records have different purposes.
Client definitions are optional sample files; selecting them does not install a
client, load a reviewer or activate plugins.

## Repository essentials

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| Project introduction | [README.md](templates/minimal/README.md) | [README.md](templates/comprehensive/README.md) |
| Current project context | [CONTEXT.md](templates/minimal/CONTEXT.md) | [CONTEXT.md](templates/comprehensive/CONTEXT.md) |
| Repository roadmap | [ROADMAP.md](templates/minimal/ROADMAP.md) | [ROADMAP.md](templates/comprehensive/ROADMAP.md) |
| User-facing change history | [CHANGELOG.md](templates/minimal/CHANGELOG.md) | [CHANGELOG.md](templates/comprehensive/CHANGELOG.md) |
| Contribution workflow | [CONTRIBUTING.md](templates/minimal/CONTRIBUTING.md) | [CONTRIBUTING.md](templates/comprehensive/CONTRIBUTING.md) |
| Community behavior | [CODE_OF_CONDUCT.md](templates/minimal/CODE_OF_CONDUCT.md) | [CODE_OF_CONDUCT.md](templates/comprehensive/CODE_OF_CONDUCT.md) |
| Governance and decision authority | [GOVERNANCE.md](templates/minimal/GOVERNANCE.md) | [GOVERNANCE.md](templates/comprehensive/GOVERNANCE.md) |
| Vulnerability reporting | [SECURITY.md](templates/minimal/SECURITY.md) | [SECURITY.md](templates/comprehensive/SECURITY.md) |
| Support routes | [SUPPORT.md](templates/minimal/SUPPORT.md) | [SUPPORT.md](templates/comprehensive/SUPPORT.md) |
| MIT license text | [LICENSE-MIT](templates/minimal/LICENSE-MIT) | [LICENSE-MIT](templates/comprehensive/LICENSE-MIT) |
| Apache license text | [LICENSE-APACHE](templates/minimal/LICENSE-APACHE) | [LICENSE-APACHE](templates/comprehensive/LICENSE-APACHE) |

These files are recipient-project samples. OpenDocKit's own policies are the
root community files. Select a suitable license for your project and prepare its
actual `LICENSE` and notices; the alternative texts are not an instruction to
apply two licenses automatically.

## Interface contracts

| Find information about | Minimal | Comprehensive |
| --- | --- | --- |
| HTTP API — OpenAPI | [contracts/openapi.yaml](templates/minimal/contracts/openapi.yaml) | [contracts/openapi.yaml](templates/comprehensive/contracts/openapi.yaml) |
| Events — AsyncAPI | [contracts/asyncapi.yaml](templates/minimal/contracts/asyncapi.yaml) | [contracts/asyncapi.yaml](templates/comprehensive/contracts/asyncapi.yaml) |
| Structured values — JSON Schema | [contracts/json-schema.json](templates/minimal/contracts/json-schema.json) | [contracts/json-schema.json](templates/comprehensive/contracts/json-schema.json) |
| GraphQL schema | [contracts/graphql.graphql](templates/minimal/contracts/graphql.graphql) | [contracts/graphql.graphql](templates/comprehensive/contracts/graphql.graphql) |
| Protocol Buffers schema | [contracts/protobuf.proto](templates/minimal/contracts/protobuf.proto) | [contracts/protobuf.proto](templates/comprehensive/contracts/protobuf.proto) |

These are starting skeletons, not complete APIs. Define actual project contracts
and use the appropriate format tooling. The maintainer validator's supported
syntax and limits are explained in [CONTRIBUTING](CONTRIBUTING.md#local-checks).

## All source files

Expand a representation for its complete file list. The directories and filenames
are the source authority; this manually maintained index should change alongside
source additions, moves or removals.

<details>
<summary>Minimal — complete source list</summary>

**Repository root**

- [.gitignore.example](templates/minimal/.gitignore.example)
- [AGENTS.md](templates/minimal/AGENTS.md)
- [CHANGELOG.md](templates/minimal/CHANGELOG.md)
- [CODE_OF_CONDUCT.md](templates/minimal/CODE_OF_CONDUCT.md)
- [CONTEXT.md](templates/minimal/CONTEXT.md)
- [CONTRIBUTING.md](templates/minimal/CONTRIBUTING.md)
- [GOVERNANCE.md](templates/minimal/GOVERNANCE.md)
- [LICENSE-APACHE](templates/minimal/LICENSE-APACHE)
- [LICENSE-MIT](templates/minimal/LICENSE-MIT)
- [README.md](templates/minimal/README.md)
- [ROADMAP.md](templates/minimal/ROADMAP.md)
- [SECURITY.md](templates/minimal/SECURITY.md)
- [SUPPORT.md](templates/minimal/SUPPORT.md)

**.agents**

- [.agents/artifacts/README.md](templates/minimal/.agents/artifacts/README.md)
- [.agents/handoffs/HANDOFF.md](templates/minimal/.agents/handoffs/HANDOFF.md)
- [.agents/plans/plan-id.md](templates/minimal/.agents/plans/plan-id.md)
- [.agents/README.md](templates/minimal/.agents/README.md)
- [.agents/sessions/session-id.md](templates/minimal/.agents/sessions/session-id.md)
- [.agents/skills/template/SKILL.md](templates/minimal/.agents/skills/template/SKILL.md)
- [.agents/tasks/task-id.md](templates/minimal/.agents/tasks/task-id.md)

**.claude**

- [.claude/agents/reviewer.md](templates/minimal/.claude/agents/reviewer.md)
- [.claude/rules/project.md](templates/minimal/.claude/rules/project.md)
- [.claude/settings.json](templates/minimal/.claude/settings.json)
- [.claude/skills/project-review/SKILL.md](templates/minimal/.claude/skills/project-review/SKILL.md)

**.codex**

- [.codex/config.toml](templates/minimal/.codex/config.toml)

**.cursor**

- [.cursor/rules/project.mdc](templates/minimal/.cursor/rules/project.mdc)

**.github**

- [.github/copilot-instructions.md](templates/minimal/.github/copilot-instructions.md)

**.kiro**

- [.kiro/steering/project.md](templates/minimal/.kiro/steering/project.md)

**.opencode**

- [.opencode/agents/reviewer.md](templates/minimal/.opencode/agents/reviewer.md)

**contracts**

- [contracts/asyncapi.yaml](templates/minimal/contracts/asyncapi.yaml)
- [contracts/graphql.graphql](templates/minimal/contracts/graphql.graphql)
- [contracts/json-schema.json](templates/minimal/contracts/json-schema.json)
- [contracts/openapi.yaml](templates/minimal/contracts/openapi.yaml)
- [contracts/protobuf.proto](templates/minimal/contracts/protobuf.proto)

**docs — current concern files**

- [docs/agent-workflow.md](templates/minimal/docs/agent-workflow.md)
- [docs/AGENTS.md](templates/minimal/docs/AGENTS.md)
- [docs/ai-systems.md](templates/minimal/docs/ai-systems.md)
- [docs/architecture.md](templates/minimal/docs/architecture.md)
- [docs/business.md](templates/minimal/docs/business.md)
- [docs/cli-library.md](templates/minimal/docs/cli-library.md)
- [docs/components.md](templates/minimal/docs/components.md)
- [docs/data-workloads.md](templates/minimal/docs/data-workloads.md)
- [docs/data.md](templates/minimal/docs/data.md)
- [docs/delivery.md](templates/minimal/docs/delivery.md)
- [docs/desktop.md](templates/minimal/docs/desktop.md)
- [docs/documentation-maintenance.md](templates/minimal/docs/documentation-maintenance.md)
- [docs/domain.md](templates/minimal/docs/domain.md)
- [docs/embedded.md](templates/minimal/docs/embedded.md)
- [docs/engineering.md](templates/minimal/docs/engineering.md)
- [docs/experience.md](templates/minimal/docs/experience.md)
- [docs/game.md](templates/minimal/docs/game.md)
- [docs/interfaces.md](templates/minimal/docs/interfaces.md)
- [docs/mobile.md](templates/minimal/docs/mobile.md)
- [docs/operations.md](templates/minimal/docs/operations.md)
- [docs/overview.md](templates/minimal/docs/overview.md)
- [docs/product-extension.md](templates/minimal/docs/product-extension.md)
- [docs/product.md](templates/minimal/docs/product.md)
- [docs/quality.md](templates/minimal/docs/quality.md)
- [docs/README.md](templates/minimal/docs/README.md)
- [docs/security.md](templates/minimal/docs/security.md)
- [docs/service.md](templates/minimal/docs/service.md)
- [docs/user-documentation.md](templates/minimal/docs/user-documentation.md)

**docs/agent-workflow**

- [docs/agent-workflow/hook-adoption.md](templates/minimal/docs/agent-workflow/hook-adoption.md)

**docs/decisions**

- [docs/decisions/ADR-0000.md](templates/minimal/docs/decisions/ADR-0000.md)
- [docs/decisions/README.md](templates/minimal/docs/decisions/README.md)

**docs/delivery**

- [docs/delivery/requests/bug-report.md](templates/minimal/docs/delivery/requests/bug-report.md)
- [docs/delivery/requests/documentation-issue.md](templates/minimal/docs/delivery/requests/documentation-issue.md)
- [docs/delivery/requests/feature-request.md](templates/minimal/docs/delivery/requests/feature-request.md)
- [docs/delivery/requests/pull-request.md](templates/minimal/docs/delivery/requests/pull-request.md)
- [docs/delivery/requests/template-request.md](templates/minimal/docs/delivery/requests/template-request.md)

**docs/designs**

- [docs/designs/design-id.md](templates/minimal/docs/designs/design-id.md)
- [docs/designs/README.md](templates/minimal/docs/designs/README.md)

**docs/handoffs**

- [docs/handoffs/handoff-id.md](templates/minimal/docs/handoffs/handoff-id.md)
- [docs/handoffs/README.md](templates/minimal/docs/handoffs/README.md)

**docs/incidents**

- [docs/incidents/incident-id.md](templates/minimal/docs/incidents/incident-id.md)
- [docs/incidents/README.md](templates/minimal/docs/incidents/README.md)

**docs/plans**

- [docs/plans/plan-id.md](templates/minimal/docs/plans/plan-id.md)
- [docs/plans/README.md](templates/minimal/docs/plans/README.md)

**docs/releases**

- [docs/releases/README.md](templates/minimal/docs/releases/README.md)
- [docs/releases/release-id.md](templates/minimal/docs/releases/release-id.md)

**docs/research**

- [docs/research/README.md](templates/minimal/docs/research/README.md)

**docs/reviews**

- [docs/reviews/README.md](templates/minimal/docs/reviews/README.md)
- [docs/reviews/review-id.md](templates/minimal/docs/reviews/review-id.md)

**docs/roles**

- [docs/roles/ba.md](templates/minimal/docs/roles/ba.md)
- [docs/roles/engineering.md](templates/minimal/docs/roles/engineering.md)
- [docs/roles/operations.md](templates/minimal/docs/roles/operations.md)
- [docs/roles/pm.md](templates/minimal/docs/roles/pm.md)
- [docs/roles/po.md](templates/minimal/docs/roles/po.md)
- [docs/roles/qa.md](templates/minimal/docs/roles/qa.md)
- [docs/roles/README.md](templates/minimal/docs/roles/README.md)

**docs/specs**

- [docs/specs/README.md](templates/minimal/docs/specs/README.md)
- [docs/specs/spec-id.md](templates/minimal/docs/specs/spec-id.md)

**docs/sprints**

- [docs/sprints/README.md](templates/minimal/docs/sprints/README.md)
- [docs/sprints/sprint-id.md](templates/minimal/docs/sprints/sprint-id.md)

**docs/tasks**

- [docs/tasks/README.md](templates/minimal/docs/tasks/README.md)
- [docs/tasks/task-id.md](templates/minimal/docs/tasks/task-id.md)

**docs/verification**

- [docs/verification/README.md](templates/minimal/docs/verification/README.md)
- [docs/verification/verification-id.md](templates/minimal/docs/verification/verification-id.md)

</details>

<details>
<summary>Comprehensive — complete source list</summary>

**Repository root**

- [.gitignore.example](templates/comprehensive/.gitignore.example)
- [AGENTS.md](templates/comprehensive/AGENTS.md)
- [CHANGELOG.md](templates/comprehensive/CHANGELOG.md)
- [CODE_OF_CONDUCT.md](templates/comprehensive/CODE_OF_CONDUCT.md)
- [CONTEXT.md](templates/comprehensive/CONTEXT.md)
- [CONTRIBUTING.md](templates/comprehensive/CONTRIBUTING.md)
- [GOVERNANCE.md](templates/comprehensive/GOVERNANCE.md)
- [LICENSE-APACHE](templates/comprehensive/LICENSE-APACHE)
- [LICENSE-MIT](templates/comprehensive/LICENSE-MIT)
- [README.md](templates/comprehensive/README.md)
- [ROADMAP.md](templates/comprehensive/ROADMAP.md)
- [SECURITY.md](templates/comprehensive/SECURITY.md)
- [SUPPORT.md](templates/comprehensive/SUPPORT.md)

**.agents**

- [.agents/artifacts/README.md](templates/comprehensive/.agents/artifacts/README.md)
- [.agents/handoffs/HANDOFF.md](templates/comprehensive/.agents/handoffs/HANDOFF.md)
- [.agents/plans/plan-id.md](templates/comprehensive/.agents/plans/plan-id.md)
- [.agents/README.md](templates/comprehensive/.agents/README.md)
- [.agents/sessions/session-id.md](templates/comprehensive/.agents/sessions/session-id.md)
- [.agents/skills/template/SKILL.md](templates/comprehensive/.agents/skills/template/SKILL.md)
- [.agents/tasks/task-id.md](templates/comprehensive/.agents/tasks/task-id.md)

**.claude**

- [.claude/agents/reviewer.md](templates/comprehensive/.claude/agents/reviewer.md)
- [.claude/rules/project.md](templates/comprehensive/.claude/rules/project.md)
- [.claude/settings.json](templates/comprehensive/.claude/settings.json)
- [.claude/skills/project-review/SKILL.md](templates/comprehensive/.claude/skills/project-review/SKILL.md)

**.codex**

- [.codex/config.toml](templates/comprehensive/.codex/config.toml)

**.cursor**

- [.cursor/rules/project.mdc](templates/comprehensive/.cursor/rules/project.mdc)

**.kiro**

- [.kiro/steering/project.md](templates/comprehensive/.kiro/steering/project.md)

**.opencode**

- [.opencode/agents/reviewer.md](templates/comprehensive/.opencode/agents/reviewer.md)

**contracts**

- [contracts/asyncapi.yaml](templates/comprehensive/contracts/asyncapi.yaml)
- [contracts/graphql.graphql](templates/comprehensive/contracts/graphql.graphql)
- [contracts/json-schema.json](templates/comprehensive/contracts/json-schema.json)
- [contracts/openapi.yaml](templates/comprehensive/contracts/openapi.yaml)
- [contracts/protobuf.proto](templates/comprehensive/contracts/protobuf.proto)

**docs — current concern files**

- [docs/AGENTS.md](templates/comprehensive/docs/AGENTS.md)
- [docs/documentation-maintenance.md](templates/comprehensive/docs/documentation-maintenance.md)
- [docs/overview.md](templates/comprehensive/docs/overview.md)
- [docs/README.md](templates/comprehensive/docs/README.md)

**docs/agent-workflow**

- [docs/agent-workflow/handoff-policy.md](templates/comprehensive/docs/agent-workflow/handoff-policy.md)
- [docs/agent-workflow/hook-adoption.md](templates/comprehensive/docs/agent-workflow/hook-adoption.md)
- [docs/agent-workflow/README.md](templates/comprehensive/docs/agent-workflow/README.md)
- [docs/agent-workflow/roles.md](templates/comprehensive/docs/agent-workflow/roles.md)
- [docs/agent-workflow/verification.md](templates/comprehensive/docs/agent-workflow/verification.md)
- [docs/agent-workflow/workflow.md](templates/comprehensive/docs/agent-workflow/workflow.md)

**docs/ai-systems**

- [docs/ai-systems/dataset-governance.md](templates/comprehensive/docs/ai-systems/dataset-governance.md)
- [docs/ai-systems/model-risk.md](templates/comprehensive/docs/ai-systems/model-risk.md)
- [docs/ai-systems/model-selection.md](templates/comprehensive/docs/ai-systems/model-selection.md)
- [docs/ai-systems/monitoring.md](templates/comprehensive/docs/ai-systems/monitoring.md)
- [docs/ai-systems/prompt-contracts.md](templates/comprehensive/docs/ai-systems/prompt-contracts.md)
- [docs/ai-systems/README.md](templates/comprehensive/docs/ai-systems/README.md)
- [docs/ai-systems/reproducibility.md](templates/comprehensive/docs/ai-systems/reproducibility.md)
- [docs/ai-systems/system-overview.md](templates/comprehensive/docs/ai-systems/system-overview.md)

**docs/architecture**

- [docs/architecture/building-blocks.md](templates/comprehensive/docs/architecture/building-blocks.md)
- [docs/architecture/constraints.md](templates/comprehensive/docs/architecture/constraints.md)
- [docs/architecture/crosscutting-concepts.md](templates/comprehensive/docs/architecture/crosscutting-concepts.md)
- [docs/architecture/deployment-view.md](templates/comprehensive/docs/architecture/deployment-view.md)
- [docs/architecture/overview.md](templates/comprehensive/docs/architecture/overview.md)
- [docs/architecture/quality-attributes.md](templates/comprehensive/docs/architecture/quality-attributes.md)
- [docs/architecture/README.md](templates/comprehensive/docs/architecture/README.md)
- [docs/architecture/risks-and-technical-debt.md](templates/comprehensive/docs/architecture/risks-and-technical-debt.md)
- [docs/architecture/runtime-view.md](templates/comprehensive/docs/architecture/runtime-view.md)
- [docs/architecture/system-context.md](templates/comprehensive/docs/architecture/system-context.md)

**docs/business**

- [docs/business/business-case.md](templates/comprehensive/docs/business/business-case.md)
- [docs/business/business-requirements.md](templates/comprehensive/docs/business/business-requirements.md)
- [docs/business/README.md](templates/comprehensive/docs/business/README.md)
- [docs/business/stakeholders.md](templates/comprehensive/docs/business/stakeholders.md)

**docs/cli-library**

- [docs/cli-library/command-contract.md](templates/comprehensive/docs/cli-library/command-contract.md)
- [docs/cli-library/compatibility.md](templates/comprehensive/docs/cli-library/compatibility.md)
- [docs/cli-library/integration-testing.md](templates/comprehensive/docs/cli-library/integration-testing.md)
- [docs/cli-library/packaging-release.md](templates/comprehensive/docs/cli-library/packaging-release.md)
- [docs/cli-library/public-api.md](templates/comprehensive/docs/cli-library/public-api.md)
- [docs/cli-library/README.md](templates/comprehensive/docs/cli-library/README.md)

**docs/components**

- [docs/components/backend/README.md](templates/comprehensive/docs/components/backend/README.md)
- [docs/components/frontend/README.md](templates/comprehensive/docs/components/frontend/README.md)
- [docs/components/README.md](templates/comprehensive/docs/components/README.md)

**docs/data**

- [docs/data/backup-recovery.md](templates/comprehensive/docs/data/backup-recovery.md)
- [docs/data/data-dictionary.md](templates/comprehensive/docs/data/data-dictionary.md)
- [docs/data/data-lifecycle.md](templates/comprehensive/docs/data/data-lifecycle.md)
- [docs/data/data-model.md](templates/comprehensive/docs/data/data-model.md)
- [docs/data/migrations.md](templates/comprehensive/docs/data/migrations.md)
- [docs/data/persistence.md](templates/comprehensive/docs/data/persistence.md)
- [docs/data/README.md](templates/comprehensive/docs/data/README.md)
- [docs/data/retention.md](templates/comprehensive/docs/data/retention.md)

**docs/data-workloads**

- [docs/data-workloads/data-contract.md](templates/comprehensive/docs/data-workloads/data-contract.md)
- [docs/data-workloads/data-lineage.md](templates/comprehensive/docs/data-workloads/data-lineage.md)
- [docs/data-workloads/data-quality.md](templates/comprehensive/docs/data-workloads/data-quality.md)
- [docs/data-workloads/dataset-catalog.md](templates/comprehensive/docs/data-workloads/dataset-catalog.md)
- [docs/data-workloads/pipeline-design.md](templates/comprehensive/docs/data-workloads/pipeline-design.md)
- [docs/data-workloads/README.md](templates/comprehensive/docs/data-workloads/README.md)

**docs/decisions**

- [docs/decisions/ADR-0000.md](templates/comprehensive/docs/decisions/ADR-0000.md)
- [docs/decisions/README.md](templates/comprehensive/docs/decisions/README.md)

**docs/delivery**

- [docs/delivery/acceptance-criteria.md](templates/comprehensive/docs/delivery/acceptance-criteria.md)
- [docs/delivery/README.md](templates/comprehensive/docs/delivery/README.md)
- [docs/delivery/requests/bug-report.md](templates/comprehensive/docs/delivery/requests/bug-report.md)
- [docs/delivery/requests/documentation-issue.md](templates/comprehensive/docs/delivery/requests/documentation-issue.md)
- [docs/delivery/requests/feature-request.md](templates/comprehensive/docs/delivery/requests/feature-request.md)
- [docs/delivery/requests/pull-request.md](templates/comprehensive/docs/delivery/requests/pull-request.md)
- [docs/delivery/requests/template-request.md](templates/comprehensive/docs/delivery/requests/template-request.md)

**docs/designs**

- [docs/designs/design-id.md](templates/comprehensive/docs/designs/design-id.md)
- [docs/designs/README.md](templates/comprehensive/docs/designs/README.md)
- [docs/designs/rfc-id.md](templates/comprehensive/docs/designs/rfc-id.md)

**docs/desktop**

- [docs/desktop/compatibility-testing.md](templates/comprehensive/docs/desktop/compatibility-testing.md)
- [docs/desktop/local-data.md](templates/comprehensive/docs/desktop/local-data.md)
- [docs/desktop/packaging-signing.md](templates/comprehensive/docs/desktop/packaging-signing.md)
- [docs/desktop/platform-integration.md](templates/comprehensive/docs/desktop/platform-integration.md)
- [docs/desktop/README.md](templates/comprehensive/docs/desktop/README.md)
- [docs/desktop/updates.md](templates/comprehensive/docs/desktop/updates.md)

**docs/domain**

- [docs/domain/bounded-contexts.md](templates/comprehensive/docs/domain/bounded-contexts.md)
- [docs/domain/business-rules.md](templates/comprehensive/docs/domain/business-rules.md)
- [docs/domain/business-workflows.md](templates/comprehensive/docs/domain/business-workflows.md)
- [docs/domain/domain-model.md](templates/comprehensive/docs/domain/domain-model.md)
- [docs/domain/glossary.md](templates/comprehensive/docs/domain/glossary.md)
- [docs/domain/invariants.md](templates/comprehensive/docs/domain/invariants.md)
- [docs/domain/README.md](templates/comprehensive/docs/domain/README.md)

**docs/embedded**

- [docs/embedded/firmware-update.md](templates/comprehensive/docs/embedded/firmware-update.md)
- [docs/embedded/hardware-interfaces.md](templates/comprehensive/docs/embedded/hardware-interfaces.md)
- [docs/embedded/hardware-testing.md](templates/comprehensive/docs/embedded/hardware-testing.md)
- [docs/embedded/provisioning-recovery.md](templates/comprehensive/docs/embedded/provisioning-recovery.md)
- [docs/embedded/README.md](templates/comprehensive/docs/embedded/README.md)
- [docs/embedded/resource-budgets.md](templates/comprehensive/docs/embedded/resource-budgets.md)

**docs/engineering**

- [docs/engineering/branching-strategy.md](templates/comprehensive/docs/engineering/branching-strategy.md)
- [docs/engineering/code-review.md](templates/comprehensive/docs/engineering/code-review.md)
- [docs/engineering/codebase-guide.md](templates/comprehensive/docs/engineering/codebase-guide.md)
- [docs/engineering/coding-conventions.md](templates/comprehensive/docs/engineering/coding-conventions.md)
- [docs/engineering/dependency-management.md](templates/comprehensive/docs/engineering/dependency-management.md)
- [docs/engineering/development-setup.md](templates/comprehensive/docs/engineering/development-setup.md)
- [docs/engineering/documentation-maintenance.md](templates/comprehensive/docs/engineering/documentation-maintenance.md)
- [docs/engineering/performance-budget.md](templates/comprehensive/docs/engineering/performance-budget.md)
- [docs/engineering/README.md](templates/comprehensive/docs/engineering/README.md)
- [docs/engineering/working-agreement.md](templates/comprehensive/docs/engineering/working-agreement.md)

**docs/experience**

- [docs/experience/accessibility-statement.md](templates/comprehensive/docs/experience/accessibility-statement.md)
- [docs/experience/accessibility.md](templates/comprehensive/docs/experience/accessibility.md)
- [docs/experience/brand-guidelines.md](templates/comprehensive/docs/experience/brand-guidelines.md)
- [docs/experience/browser-support.md](templates/comprehensive/docs/experience/browser-support.md)
- [docs/experience/component-guidelines.md](templates/comprehensive/docs/experience/component-guidelines.md)
- [docs/experience/content-guidelines.md](templates/comprehensive/docs/experience/content-guidelines.md)
- [docs/experience/design-system.md](templates/comprehensive/docs/experience/design-system.md)
- [docs/experience/information-architecture.md](templates/comprehensive/docs/experience/information-architecture.md)
- [docs/experience/interaction-patterns.md](templates/comprehensive/docs/experience/interaction-patterns.md)
- [docs/experience/localization.md](templates/comprehensive/docs/experience/localization.md)
- [docs/experience/README.md](templates/comprehensive/docs/experience/README.md)
- [docs/experience/user-flows.md](templates/comprehensive/docs/experience/user-flows.md)
- [docs/experience/ux-principles.md](templates/comprehensive/docs/experience/ux-principles.md)

**docs/game**

- [docs/game/asset-pipeline.md](templates/comprehensive/docs/game/asset-pipeline.md)
- [docs/game/gameplay-systems.md](templates/comprehensive/docs/game/gameplay-systems.md)
- [docs/game/performance-platforms.md](templates/comprehensive/docs/game/performance-platforms.md)
- [docs/game/playtesting-release.md](templates/comprehensive/docs/game/playtesting-release.md)
- [docs/game/README.md](templates/comprehensive/docs/game/README.md)
- [docs/game/save-compatibility.md](templates/comprehensive/docs/game/save-compatibility.md)

**docs/handoffs**

- [docs/handoffs/handoff-id.md](templates/comprehensive/docs/handoffs/handoff-id.md)
- [docs/handoffs/README.md](templates/comprehensive/docs/handoffs/README.md)

**docs/incidents**

- [docs/incidents/incident-id.md](templates/comprehensive/docs/incidents/incident-id.md)
- [docs/incidents/README.md](templates/comprehensive/docs/incidents/README.md)

**docs/interfaces**

- [docs/interfaces/api-conventions.md](templates/comprehensive/docs/interfaces/api-conventions.md)
- [docs/interfaces/api-overview.md](templates/comprehensive/docs/interfaces/api-overview.md)
- [docs/interfaces/authentication.md](templates/comprehensive/docs/interfaces/authentication.md)
- [docs/interfaces/compatibility.md](templates/comprehensive/docs/interfaces/compatibility.md)
- [docs/interfaces/error-handling.md](templates/comprehensive/docs/interfaces/error-handling.md)
- [docs/interfaces/event-contracts.md](templates/comprehensive/docs/interfaces/event-contracts.md)
- [docs/interfaces/external-integrations.md](templates/comprehensive/docs/interfaces/external-integrations.md)
- [docs/interfaces/README.md](templates/comprehensive/docs/interfaces/README.md)
- [docs/interfaces/versioning.md](templates/comprehensive/docs/interfaces/versioning.md)

**docs/mobile**

- [docs/mobile/background-work.md](templates/comprehensive/docs/mobile/background-work.md)
- [docs/mobile/device-testing.md](templates/comprehensive/docs/mobile/device-testing.md)
- [docs/mobile/offline-sync.md](templates/comprehensive/docs/mobile/offline-sync.md)
- [docs/mobile/permissions.md](templates/comprehensive/docs/mobile/permissions.md)
- [docs/mobile/platform-support.md](templates/comprehensive/docs/mobile/platform-support.md)
- [docs/mobile/README.md](templates/comprehensive/docs/mobile/README.md)
- [docs/mobile/store-release.md](templates/comprehensive/docs/mobile/store-release.md)

**docs/operations**

- [docs/operations/capacity-planning.md](templates/comprehensive/docs/operations/capacity-planning.md)
- [docs/operations/ci-cd.md](templates/comprehensive/docs/operations/ci-cd.md)
- [docs/operations/cost-management.md](templates/comprehensive/docs/operations/cost-management.md)
- [docs/operations/deployment.md](templates/comprehensive/docs/operations/deployment.md)
- [docs/operations/disaster-recovery.md](templates/comprehensive/docs/operations/disaster-recovery.md)
- [docs/operations/environments.md](templates/comprehensive/docs/operations/environments.md)
- [docs/operations/incident-response.md](templates/comprehensive/docs/operations/incident-response.md)
- [docs/operations/maintenance.md](templates/comprehensive/docs/operations/maintenance.md)
- [docs/operations/observability.md](templates/comprehensive/docs/operations/observability.md)
- [docs/operations/README.md](templates/comprehensive/docs/operations/README.md)
- [docs/operations/rollback.md](templates/comprehensive/docs/operations/rollback.md)
- [docs/operations/runbook.md](templates/comprehensive/docs/operations/runbook.md)
- [docs/operations/service-ownership.md](templates/comprehensive/docs/operations/service-ownership.md)
- [docs/operations/sli-slo.md](templates/comprehensive/docs/operations/sli-slo.md)
- [docs/operations/support-playbook.md](templates/comprehensive/docs/operations/support-playbook.md)

**docs/plans**

- [docs/plans/accessibility-test-plan-id.md](templates/comprehensive/docs/plans/accessibility-test-plan-id.md)
- [docs/plans/backfill-plan-id.md](templates/comprehensive/docs/plans/backfill-plan-id.md)
- [docs/plans/deprecation-plan-id.md](templates/comprehensive/docs/plans/deprecation-plan-id.md)
- [docs/plans/experiment-plan-id.md](templates/comprehensive/docs/plans/experiment-plan-id.md)
- [docs/plans/master-plan-id.md](templates/comprehensive/docs/plans/master-plan-id.md)
- [docs/plans/model-evaluation-plan-id.md](templates/comprehensive/docs/plans/model-evaluation-plan-id.md)
- [docs/plans/phase-plan-id.md](templates/comprehensive/docs/plans/phase-plan-id.md)
- [docs/plans/plan-id.md](templates/comprehensive/docs/plans/plan-id.md)
- [docs/plans/README.md](templates/comprehensive/docs/plans/README.md)
- [docs/plans/research-plan-id.md](templates/comprehensive/docs/plans/research-plan-id.md)
- [docs/plans/retirement-plan-id.md](templates/comprehensive/docs/plans/retirement-plan-id.md)
- [docs/plans/test-plan-id.md](templates/comprehensive/docs/plans/test-plan-id.md)
- [docs/plans/usability-test-plan-id.md](templates/comprehensive/docs/plans/usability-test-plan-id.md)

**docs/product**

- [docs/product/brief.md](templates/comprehensive/docs/product/brief.md)
- [docs/product/metric-definitions.md](templates/comprehensive/docs/product/metric-definitions.md)
- [docs/product/non-functional-requirements.md](templates/comprehensive/docs/product/non-functional-requirements.md)
- [docs/product/personas.md](templates/comprehensive/docs/product/personas.md)
- [docs/product/prd.md](templates/comprehensive/docs/product/prd.md)
- [docs/product/README.md](templates/comprehensive/docs/product/README.md)
- [docs/product/requirements.md](templates/comprehensive/docs/product/requirements.md)
- [docs/product/risk-assumptions.md](templates/comprehensive/docs/product/risk-assumptions.md)
- [docs/product/roadmap.md](templates/comprehensive/docs/product/roadmap.md)
- [docs/product/success-metrics.md](templates/comprehensive/docs/product/success-metrics.md)
- [docs/product/user-journeys.md](templates/comprehensive/docs/product/user-journeys.md)
- [docs/product/vision.md](templates/comprehensive/docs/product/vision.md)

**docs/product-extension**

- [docs/product-extension/compatibility.md](templates/comprehensive/docs/product-extension/compatibility.md)
- [docs/product-extension/extension-api.md](templates/comprehensive/docs/product-extension/extension-api.md)
- [docs/product-extension/packaging-distribution.md](templates/comprehensive/docs/product-extension/packaging-distribution.md)
- [docs/product-extension/permissions-isolation.md](templates/comprehensive/docs/product-extension/permissions-isolation.md)
- [docs/product-extension/README.md](templates/comprehensive/docs/product-extension/README.md)

**docs/quality**

- [docs/quality/README.md](templates/comprehensive/docs/quality/README.md)
- [docs/quality/testing-strategy.md](templates/comprehensive/docs/quality/testing-strategy.md)

**docs/releases**

- [docs/releases/README.md](templates/comprehensive/docs/releases/README.md)
- [docs/releases/release-id.md](templates/comprehensive/docs/releases/release-id.md)
- [docs/releases/release-id/checklist.md](templates/comprehensive/docs/releases/release-id/checklist.md)
- [docs/releases/release-id/launch-plan.md](templates/comprehensive/docs/releases/release-id/launch-plan.md)
- [docs/releases/release-id/migration.md](templates/comprehensive/docs/releases/release-id/migration.md)
- [docs/releases/release-id/notes.md](templates/comprehensive/docs/releases/release-id/notes.md)

**docs/research**

- [docs/research/experiment-id.md](templates/comprehensive/docs/research/experiment-id.md)
- [docs/research/README.md](templates/comprehensive/docs/research/README.md)
- [docs/research/research-id.md](templates/comprehensive/docs/research/research-id.md)

**docs/reviews**

- [docs/reviews/feedback-review-id.md](templates/comprehensive/docs/reviews/feedback-review-id.md)
- [docs/reviews/README.md](templates/comprehensive/docs/reviews/README.md)
- [docs/reviews/review-id.md](templates/comprehensive/docs/reviews/review-id.md)

**docs/roles**

- [docs/roles/ba.md](templates/comprehensive/docs/roles/ba.md)
- [docs/roles/engineering.md](templates/comprehensive/docs/roles/engineering.md)
- [docs/roles/operations.md](templates/comprehensive/docs/roles/operations.md)
- [docs/roles/pm.md](templates/comprehensive/docs/roles/pm.md)
- [docs/roles/po.md](templates/comprehensive/docs/roles/po.md)
- [docs/roles/qa.md](templates/comprehensive/docs/roles/qa.md)
- [docs/roles/README.md](templates/comprehensive/docs/roles/README.md)

**docs/security**

- [docs/security/authorization-model.md](templates/comprehensive/docs/security/authorization-model.md)
- [docs/security/compliance.md](templates/comprehensive/docs/security/compliance.md)
- [docs/security/data-processing-register.md](templates/comprehensive/docs/security/data-processing-register.md)
- [docs/security/privacy-risk.md](templates/comprehensive/docs/security/privacy-risk.md)
- [docs/security/README.md](templates/comprehensive/docs/security/README.md)
- [docs/security/secrets-management.md](templates/comprehensive/docs/security/secrets-management.md)
- [docs/security/secure-development.md](templates/comprehensive/docs/security/secure-development.md)
- [docs/security/security-architecture.md](templates/comprehensive/docs/security/security-architecture.md)
- [docs/security/supply-chain-security.md](templates/comprehensive/docs/security/supply-chain-security.md)
- [docs/security/threat-model.md](templates/comprehensive/docs/security/threat-model.md)

**docs/service**

- [docs/service/api-delivery.md](templates/comprehensive/docs/service/api-delivery.md)
- [docs/service/async-processing.md](templates/comprehensive/docs/service/async-processing.md)
- [docs/service/idempotency-retries.md](templates/comprehensive/docs/service/idempotency-retries.md)
- [docs/service/README.md](templates/comprehensive/docs/service/README.md)
- [docs/service/resilience.md](templates/comprehensive/docs/service/resilience.md)
- [docs/service/service-evolution.md](templates/comprehensive/docs/service/service-evolution.md)

**docs/specs**

- [docs/specs/proposal-id.md](templates/comprehensive/docs/specs/proposal-id.md)
- [docs/specs/README.md](templates/comprehensive/docs/specs/README.md)
- [docs/specs/spec-id.md](templates/comprehensive/docs/specs/spec-id.md)

**docs/sprints**

- [docs/sprints/README.md](templates/comprehensive/docs/sprints/README.md)
- [docs/sprints/retrospective-id.md](templates/comprehensive/docs/sprints/retrospective-id.md)
- [docs/sprints/sprint-id.md](templates/comprehensive/docs/sprints/sprint-id.md)

**docs/tasks**

- [docs/tasks/README.md](templates/comprehensive/docs/tasks/README.md)
- [docs/tasks/task-id.md](templates/comprehensive/docs/tasks/task-id.md)

**docs/user-documentation**

- [docs/user-documentation/explanation.md](templates/comprehensive/docs/user-documentation/explanation.md)
- [docs/user-documentation/faq.md](templates/comprehensive/docs/user-documentation/faq.md)
- [docs/user-documentation/how-to.md](templates/comprehensive/docs/user-documentation/how-to.md)
- [docs/user-documentation/installation.md](templates/comprehensive/docs/user-documentation/installation.md)
- [docs/user-documentation/quickstart.md](templates/comprehensive/docs/user-documentation/quickstart.md)
- [docs/user-documentation/README.md](templates/comprehensive/docs/user-documentation/README.md)
- [docs/user-documentation/reference.md](templates/comprehensive/docs/user-documentation/reference.md)
- [docs/user-documentation/troubleshooting.md](templates/comprehensive/docs/user-documentation/troubleshooting.md)
- [docs/user-documentation/tutorial.md](templates/comprehensive/docs/user-documentation/tutorial.md)

**docs/verification**

- [docs/verification/performance-review-id.md](templates/comprehensive/docs/verification/performance-review-id.md)
- [docs/verification/README.md](templates/comprehensive/docs/verification/README.md)
- [docs/verification/verification-id.md](templates/comprehensive/docs/verification/verification-id.md)

</details>
