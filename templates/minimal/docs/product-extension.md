<!-- OpenDocKit author guidance
ID: product-extension.minimal.docs.product-extension.md
Purpose: Describe product-extension-specific behavior, failure modes and verification.
Use when: The project has product-extension responsibilities.
Suggested destination: docs/product-extension.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Product Extension

## Extension surface

{{Define extension points, host lifecycle, APIs/events and data/resource ownership. Specify errors, capability negotiation, loading/unloading and version boundaries. Test representative extensions against host invariants and contract authority.}}

## Host compatibility

{{Declare extension/host version ranges, API stability and migration policy. Handle incompatible metadata, removed hooks and dependent extensions. Verify supported version pairs and graceful rejection of unsupported ones.}}

## Extension isolation

{{Map extension capabilities to privileges, trust boundaries and data access. Describe sandbox/process isolation, untrusted inputs, resource limits and revocation. Verify denied capability/failed extension behavior; package discovery is not an isolation guarantee.}}

## Extension distribution

{{Define package manifest, component layout, integrity/provenance and publication authority. Separate local loading, registry/marketplace policy and updates/removal. Test packaged loading and compatibility; no enabled remote code or claimed marketplace approval by default.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
