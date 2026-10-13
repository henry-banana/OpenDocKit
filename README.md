<h1 align="center">OpenDocKit</h1>

<p align="center">
  <strong>Project documentation. Ready to make your own.</strong><br>
  An open-source template library for business, engineering and agent-assisted work.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2563eb?style=flat-square" alt="License: MIT"></a>
  <a href="#quick-start"><img src="https://img.shields.io/badge/use-copy%20%26%20fill-0f766e?style=flat-square" alt="Use: copy and fill"></a>
  <a href="#project-status"><img src="https://img.shields.io/badge/status-in%20development-d97706?style=flat-square" alt="Status: in development"></a>
</p>

<p align="center">
  <a href="INDEX.md"><strong>Explore the templates</strong></a> ·
  <a href="#quick-start">Get started</a> ·
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="https://github.com/henry-banana/OpenDocKit/issues/new/choose">Report an issue</a>
</p>

---

Starting a project means deciding what to document, where each file belongs and
how the team will keep it useful. OpenDocKit gives that work a starting structure:
from business needs and architecture to testing, releases and ongoing operations.

Choose a compact document per concern or a detailed folder structure. Add the
project-specific and agent workflow samples you need, copy them into your repo
and fill them with your own facts. Your team owns the result.

<p align="center"><strong>Clone → Browse → Copy → Fill</strong></p>

## Why OpenDocKit?

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🗂️ A place for the whole lifecycle</h3>
      Start with business and requirements, then carry the same documentation
      structure through design, engineering, delivery and maintenance.
    </td>
    <td width="50%" valign="top">
      <h3>📐 Two levels of detail</h3>
      Keep a concern in one file or split it into focused documents. Expand where
      ownership or complexity calls for it.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🤝 Shared by people and agents</h3>
      Role briefs, team records and optional native agent files connect readers
      to the same project knowledge.
    </td>
    <td width="50%" valign="top">
      <h3>✍️ Yours after copying</h3>
      Edit ordinary files in your own repository. Select useful samples, remove
      what you do not need and maintain them with your team.
    </td>
  </tr>
</table>

## What's included

| Area | What you'll find |
| --- | --- |
| **Business & product** | Business needs, stakeholders, requirements, domain rules, product behavior and acceptance |
| **Design & engineering** | Architecture, UX, frontend/backend components, interfaces, data, quality and security |
| **Delivery & operations** | Development conventions, deployment, reliability, releases, incidents and support |
| **Team work records** | Research, specs, designs, plans, tasks, ADRs, reviews, verification, sprints and handoffs |
| **Project-specific concerns** | Services, mobile, desktop, CLI/libraries, data workloads, AI systems, games, embedded and product extensions |
| **Agent workflows** | Shared instructions, skills, reviewer definitions, configuration samples and personal continuity records |
| **Repository essentials** | README, contribution, governance, conduct, security, support, changelog and license samples |

[Browse by concern, project type or role →](INDEX.md)

## Choose how much detail to keep

Both representations mirror the files of an adopting project:

<table>
  <tr>
    <th width="50%">Minimal</th>
    <th width="50%">Comprehensive</th>
  </tr>
  <tr>
    <td valign="top">
      <pre>docs/
├── business.md
├── architecture.md
├── quality.md
└── specs/
    └── spec-id.md</pre>
      One current file per concern, with separate repeatable work records.<br><br>
      <a href="templates/minimal/"><strong>Browse minimal →</strong></a>
    </td>
    <td valign="top">
      <pre>docs/
├── business/
├── architecture/
├── quality/
└── specs/
    └── spec-id.md</pre>
      Focused concern folders for different owners, detail and review cycles.<br><br>
      <a href="templates/comprehensive/"><strong>Browse comprehensive →</strong></a>
    </td>
  </tr>
</table>

These are excerpts of the available structure, not mandatory file lists.
If you're unsure, start with minimal. Either representation can serve a
production project; expand a concern when it becomes difficult to maintain in
one document, and update its facts and incoming links together.

## Quick start

You need Git to clone the library and any editor to fill the templates. You can
also download the source from GitHub. Using templates requires no package install
or agent client.

```sh
git clone https://github.com/henry-banana/OpenDocKit.git
cd OpenDocKit
```

1. **Choose** [minimal](templates/minimal/) or
   [comprehensive](templates/comprehensive/).
2. **Browse** [INDEX.md](INDEX.md) and select the files you need. You can also copy
   a representation and remove unneeded parts before adopting it.
3. **Copy** into your project, preserving paths beneath the chosen representation.
   Merge any existing files deliberately.
4. **Fill** the `{{...}}` prompts with project facts. Use and then remove author
   guidance comments; review the links, owners and configuration you retained.

### A concrete copy example

```text
OpenDocKit/templates/minimal/          your-project/
├── docs/architecture.md          →   ├── docs/architecture.md
├── docs/mobile.md                →   ├── docs/mobile.md
└── docs/specs/spec-id.md          →   └── docs/specs/offline-sync.md
```

The `templates/minimal/` wrapper stays in this library. To use the comprehensive
architecture instead, copy `templates/comprehensive/docs/architecture/` into
`your-project/docs/architecture/` and move its facts from any existing document.

[Explore all available source files →](INDEX.md#all-source-files)

## Working with agents

Use the same project documents for human review and agent context. The library
includes role briefs, workflow guidance and optional native samples for Codex,
Claude, Copilot, Cursor, Kiro and OpenCode.

Choose only the client files you use and adapt them deliberately. Shared team
records and personal plans/sessions/raw output have different tracking needs;
set specific ignore rules before storing private content. A directory name such
as `.agents/` does not itself make its contents private.

[Browse agent and personal workflow samples →](INDEX.md#agent-and-personal-workflow)

## Documentation

| Looking for | Start here |
| --- | --- |
| A particular template or project type | [Template index](INDEX.md) |
| How to add content or run maintainer checks | [Contributing](CONTRIBUTING.md) |
| Questions, bugs or missing coverage | [Support](SUPPORT.md) |
| Changes since an earlier copy | [Changelog](CHANGELOG.md) |
| A sensitive security concern | [Security policy](SECURITY.md) |

OpenDocKit's root policies describe this library. Their counterparts inside
`templates/` are samples for adopting projects.

## Project status

OpenDocKit is under active development. Validation covers source structure,
index coverage and library links; current validation limits are recorded in
[CONTRIBUTING.md](CONTRIBUTING.md#current-maintenance-limits).
Review and adapt your copies. Client loading and productivity gains have not
been established by static source checks.

## Contributing

Help make project documentation easier to start and maintain. Contributions can
be as small as correcting a confusing prompt or broken link, or as substantial
as covering a missing reader task with a well-scoped template.

Read [CONTRIBUTING.md](CONTRIBUTING.md), open an
[issue](https://github.com/henry-banana/OpenDocKit/issues/new/choose) or send a pull
request. Share practical examples and primary sources where they help explain a
change. Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).

If OpenDocKit helps your project, share the workflow you used and what was still
missing. That feedback helps improve the library for the next team.

## License

[MIT](LICENSE) · Copyright © 2026 OpenDocKit contributors.

Preserve applicable notices when reusing content. License texts inside
`templates/` are choices for adopting projects; third-party material retains its
own terms and attribution.
