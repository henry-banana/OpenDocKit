# Changelog

Version history for OpenDocKit, organized using
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Unreleased

### Fixed

- CI no longer requires the retired catalog: the default full audit discovers
  actual templates, verifies root INDEX coverage and checks library Markdown links.
- Corrected personal-record IDs/destinations and source links after the move to
  .agents; added personal-storage guidance and aligned ignore examples in both
  representations, including private tasks without ignoring shared skills.
- Updated library guides and lifecycle links to the current source tree; retained
  historical migration data as history rather than live inventory.

### Removed

- Retired catalog-only validator and tests; current source/index/link regression
  coverage replaces the obsolete inventory contract.

## [1.0.0] - 2026-10-15

Initial version of the OpenDocKit documentation template library.

### Added

- Two repository-shaped template sets: `templates/minimal/` for compact concern
  documents and `templates/comprehensive/` for focused concern folders.
- Business, product, architecture, domain, interface, data, UX, component,
  engineering, quality, security, delivery, operations and user documentation.
- Project-specific samples for services, mobile, desktop, CLI/libraries, data
  workloads, AI systems, games, embedded systems and product extensions.
- Shared research, spec, design, plan, task, ADR, review, verification, sprint,
  release, incident and handoff records.
- Project overviews and role briefs for BA, PO, PM, engineering, QA and operations.
- Optional native agent instructions, configuration, skills, reviewer definitions
  and personal continuity samples.
- Open-source repository essentials and interface contract skeletons.
- README with a project overview, feature grid, layout previews and copy examples;
  template index with task-oriented navigation and complete source lists.
- Contribution, conduct, security and support policies for OpenDocKit itself.
- GitHub issue forms, PR template, validation workflow and dependency update
  configuration.
- Read-only source validators, JSON diagnostics and regression/integration tests
  for paths, copy boundaries, template metadata, native syntax and contracts.

### Known limitations

- In 1.0.0, some destinations/links and the full audit still followed the retired
  catalog/layout. The fixes above address these issues.
- Client loading, adoption trials and productivity gains have not been established
  by the static checks.

See [current maintenance limits](CONTRIBUTING.md#current-maintenance-limits).
This entry records the initial repository version; a Git tag and GitHub Release
have not been published.
