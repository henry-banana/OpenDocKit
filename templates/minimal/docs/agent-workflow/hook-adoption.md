<!-- OpenDocKit author guidance
ID: agent-workflow.minimal.docs.agent-workflow.hook-adoption.md
Purpose: Define deliberate native hook setup and verification without enabled generic execution.
Use when: The team explicitly selects a client hook.
Suggested destination: docs/agent-workflow/hook-adoption.md
Boundary: Guidance only; no executable hook is enabled.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Optional Hook Adoption

## Trigger and client

{{Choose an actual client event and scope; verify version/format and identify explicit user activation. This library supplies guidance, not an enabled hook.}}

## Action and permissions

{{Define exact command/cwd, inputs/output, timeout, failure behavior and permission boundary. Keep credentials and remote code out; never reuse another client format.}}

## Verification and disable path

{{Test the selected hook in an isolated fixture before activation; record actual results and how to disable/revert. Hook execution remains NOT RUN until observed.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
