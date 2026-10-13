<!-- OpenDocKit author guidance
ID: base.minimal.docs.engineering.md
Purpose: Make development, tests, review and maintenance reproducible.
Use when: People or agents need to build, change and verify the project.
Suggested destination: docs/engineering.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Engineering

## Local development

{{Specify actual prerequisites, setup/config sources, build/run/check commands and required working directory; never invent a stack.}}

## Code and change workflow

{{Describe codebase boundaries, conventions, dependency changes, review and branching agreements with the actual task authority.}}

## Checks and test integration

{{Link the canonical quality guidance in quality.md, actual test/tool configuration, fixtures and check commands/cwd. Explain developer integration and failure handling; per-change test plans and observed results belong in plans/ and verification/.}}

## Maintenance and quality

{{Assign documentation/dependency ownership, change triggers and performance budgets; link actual CI/check outputs and acknowledge missing checks.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
