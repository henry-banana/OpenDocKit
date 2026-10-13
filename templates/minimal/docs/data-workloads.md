<!-- OpenDocKit author guidance
ID: data.minimal.docs.data-workloads.md
Purpose: Describe data-workloads-specific behavior, failure modes and verification.
Use when: The project has data-workloads responsibilities.
Suggested destination: docs/data-workloads.md
Boundary: Reference common authoritative facts instead of duplicating them.
Adoption: Copy, fill meaningful fields, link canonical sources and remove author guidance.
-->
# Data Workloads

## Backfill Plan

{{Plan bounded historical reprocessing without corrupting live data. Specify failure/evolution boundaries and link common authority; do not duplicate mutable facts. Record actual checks, limitations, responsibility and next action.}}

## Data Contract

{{Agree data semantics and quality between producers and consumers. Specify failure/evolution boundaries and link common authority; do not duplicate mutable facts. Record actual checks, limitations, responsibility and next action.}}

## Data Lineage

{{Explain how sources affect derived datasets and consumers. Specify failure/evolution boundaries and link common authority; do not duplicate mutable facts. Record actual checks, limitations, responsibility and next action.}}

## Data Quality

{{Define dataset-specific correctness and fitness expectations. Specify failure/evolution boundaries and link common authority; do not duplicate mutable facts. Record actual checks, limitations, responsibility and next action.}}

## Dataset Catalog

{{Help consumers discover a dataset and its trustworthy owner/source. Specify failure/evolution boundaries and link common authority; do not duplicate mutable facts. Record actual checks, limitations, responsibility and next action.}}

## Pipeline Design

{{Explain transformation, orchestration and recovery of a data pipeline. Specify failure/evolution boundaries and link common authority; do not duplicate mutable facts. Record actual checks, limitations, responsibility and next action.}}

## Open questions

{{Record each material unknown, its owner and next evidence/action; state none when resolved.}}

## Completion check

- [ ] Scope and facts have a named authority.
- [ ] Material constraints and unknowns have owners.
- [ ] Evidence states describe observed events; pending checks are not claimed as passed.
