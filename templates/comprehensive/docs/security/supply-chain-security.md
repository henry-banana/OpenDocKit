<!-- OpenDocKit author guidance
ID: base.comprehensive.docs.security.supply-chain-security.md
Purpose: Explain provenance and trust of code, dependencies and release artifacts.
Use when: Third-party or build inputs influence delivered software.
Suggested destination: docs/security/supply-chain-security.md
Boundary: Manifests/SBOM/build attestations own exact inventory; link them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Supply Chain Security

| Record | Value |
|---|---|
| Scope | {{Specific product, component, change or audience covered}} |
| Owner | {{Role or team responsible for accuracy and decisions}} |
| State | {{Proposed / current / superseded / retired, as applicable}} |
| Authority | {{This record's authority and links to canonical code, contracts or external records}} |

## Inputs and trust

{{Identify code/dependency/tool sources, acquisition boundaries and ownership of trust decisions.}}

## Build and distribution

{{Describe reproducible inputs, integrity checks, release authority and artifact provenance.}}

## Monitoring and response

{{Link dependency review/vulnerability handling, update ownership and compromised-input response.}}

## Exceptions and evidence

{{Record allowed exceptions, source/license review and actual provenance verification limits.}}

## Open questions

| Question or assumption | Owner | Next evidence/action | Decision affected |
|---|---|---|---|
| {{Unresolved item, or state that none remain}} | {{Owner}} | {{Action}} | {{Decision}} |

## Completion check

- [ ] Inputs and release authority are traceable.
- [ ] Compromised inputs have a response route.
- [ ] Provenance claims have evidence.
- [ ] Canonical sources and related records are linked in the adopted project.
- [ ] Author guidance and placeholders are resolved; evidence and document state are accurate.
