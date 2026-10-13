<!-- OpenDocKit author guidance
ID: desktop.minimal.docs.desktop.md
Purpose: Describe desktop-specific behavior, failure modes and verification.
Use when: The project has desktop responsibilities.
Suggested destination: docs/desktop.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Desktop

## OS integration

{{List supported OS versions, filesystem/window/tray/process behaviors and desktop APIs. Define privilege boundaries, multiple-instance behavior, URI/file association and platform differences. Test access denial, missing APIs and OS-specific lifecycle paths.}}

## Packaging and signing

{{Select distribution formats, architecture targets and signing/notarization authority. Describe dependency bundling, certificate handling, installer permissions and uninstall obligations. Verify installed artifacts on clean targets; identify build hash and signing result.}}

## Application updates

{{Specify feed/channel ownership, version compatibility and package verification. Handle interrupted downloads, restart, rollback/forward fix and data compatibility. Test old-to-new and failed update with integrity checks; separate target policy from observed update behavior.}}

## Local state

{{Define storage paths by platform, ownership, schema versions and backup/export behavior. Handle corruption, concurrent instances, user migration and uninstall/retention expectations. Test recovery and permissions without embedding machine-specific paths or secrets.}}

## Desktop compatibility

{{Define OS/architecture/display/input/accessibility matrix and packaged-app fixtures. Cover installation, upgrade, permissions, file operations and resource constraints. Record actual environment and results; document unsupported combinations.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
