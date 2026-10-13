<!-- OpenDocKit author guidance
ID: cli-library.minimal.docs.cli-library.md
Purpose: Describe cli-library-specific behavior, failure modes and verification.
Use when: The project has cli-library responsibilities.
Suggested destination: docs/cli-library.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Cli Library

## Command behavior

{{Specify arguments, environment/config precedence, stdin/stdout/stderr and exit code meanings. Define noninteractive behavior, cancellation, invalid input, completion and stable machine-readable output. Test shell/platform cases and failure exits; link actual command implementation/reference.}}

## Library API

{{Define public symbols, types/lifecycle, invariants and resource/thread ownership. Specify errors, side effects, concurrency and supported integrations; keep generated API reference canonical. Verify representative consumers and misuse cases against the API contract.}}

## Consumer compatibility

{{Declare runtime/platform/version support and semantic compatibility policy. Identify behavioral/type/binary changes, deprecation windows and feature negotiation. Test old consumers on new artifacts and document exact unsupported cases.}}

## Package delivery

{{Define artifact/registry identity, build reproducibility and provenance/signing owners. Describe dependency/runtime metadata, distribution channels and release/yank/recovery policy. Verify the built package in a clean consuming project; no fabricated registry publication.}}

## Consumer testing

{{Select representative consumer versions, imports/commands and installation methods. Cover missing optional dependencies, platform behavior, errors and upgrades. Record artifact hash, environment and actual consumer results.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
