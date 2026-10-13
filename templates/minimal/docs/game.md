<!-- OpenDocKit author guidance
ID: game.minimal.docs.game.md
Purpose: Describe game-specific behavior, failure modes and verification.
Use when: The project has game responsibilities.
Suggested destination: docs/game.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Game

## Gameplay state

{{Describe mechanics, world/entities, timing, state transitions and gameplay invariants. Define determinism/network authority where applicable, pause/restart and failure interactions. Link acceptance/playtest scenarios and measured balance evidence; separate design hypotheses.}}

## Asset lifecycle

{{Define source/build asset authority, formats/import settings, naming and license/provenance. Describe conversion/versioning, dependency rebuilds, platform variants and size budgets. Verify missing/corrupt assets and builds; document ownership and reproducibility.}}

## Saved state

{{Define persistent/transient state, format/version and write/backup authority. Handle interrupted writes, corruption, migration, removed content and cloud conflicts. Test old saves, recovery and round-trips against gameplay invariants.}}

## Game performance

{{Define target hardware, frame/memory/load budgets and measurement scenes. Identify rendering/CPU/IO bottlenecks, thermal/resource behavior and platform-specific features. Record build/hardware/settings, profiling methods and distributions; targets are not observed success.}}

## Playtest and release

{{Define test goals, cohort/platform/build, scenarios and feedback collection. Separate reproducible defects from balance/experience hypotheses; link fixes and release risks. Record actual observations, accessibility and release evidence without inventing participants.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
