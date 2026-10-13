<!-- OpenDocKit author guidance
ID: ai.comprehensive.docs.ai-systems.prompt-contracts.md
Purpose: Specify intended behavior of a prompt-driven capability.
Use when: An AI interaction needs stable expectations and evaluation cases.
Suggested destination: docs/ai-systems/prompt-contracts.md
Boundary: Prompt source owns exact text; this document owns behavior and trust boundaries.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Prompt Contracts

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Inputs and authority

{{Describe trusted instructions, untrusted user/retrieved content, context sources and allowed actions.}}

## Expected behavior

{{Define outputs, formats, uncertainty handling, refusal/escalation conditions and user-visible errors.}}

## Threats and limits

{{Address injection, leakage, unsupported claims and assumptions about tools/model behavior.}}

## Versioning and checks

{{Link prompt/model versions, evaluation cases and ownership of behavioral changes.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Input trust boundaries are explicit.
- [ ] Outputs and uncertainty behavior are testable.
- [ ] Version changes have evaluation evidence.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
