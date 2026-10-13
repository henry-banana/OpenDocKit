# Contributing to OpenDocKit

Help people find the right document, fill it with useful information and maintain
it as their project changes. Clearer writing, practical coverage and reliable
maintainer checks are all welcome. Please follow the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Find a useful contribution

Start with the [README](README.md), [template index](INDEX.md) and the nearest
existing template. A contribution should improve a concrete reader task or
decision. Extending an existing document is often better than adding a second
authority for the same facts.

For a substantial new domain or structural change, open a
[template request or improvement issue](https://github.com/henry-banana/OpenDocKit/issues/new/choose)
first. Describe the user need, existing gap, proposed destination and tradeoffs.
Small wording/link fixes can go straight to a pull request. Sensitive findings
follow [SECURITY.md](SECURITY.md).

## Author templates

### Placement and detail

- Put copyable content beneath `templates/minimal/` or
  `templates/comprehensive/`, using the destination path an adopting repo needs.
- Use a single current document per concern in minimal; use focused concern
  folders in comprehensive. Repeatable records can remain separate in either.
  Explain when a contribution applies to only one representation.
- Organize facts by concern and scoped responsibility. Reader roles share those
  facts through summaries and links rather than duplicate documents.
- Keep shared specs/plans/tasks and other team records distinct from personal
  sessions, private working plans and raw output. State intended tracking and
  maintenance where that distinction affects use.

### Documentation content

Use the existing `OpenDocKit author guidance` comment for documentation samples:
a unique ID, purpose, use trigger, copy-relative suggested destination, boundary
and adoption instructions. Keep the destination aligned with the physical path.
The ID labels the sample; it does not require a separate catalog.

Provide specific `{{...}}` filling prompts, meaningful sections and an observable
completion checklist. Name unknowns and evidence needs rather than inventing
facts, approvals or successful checks. Reader summaries should identify what
matters and point to their authoritative sources.

Links inside a copy root must stay inside that representation. If a destination
is project-specific or optional, use an explicit filling prompt or explain which
files must be adopted together. Keep library navigation in root [INDEX](INDEX.md),
not in a recipient project's README.

For shared root boilerplate, the comprehensive version is the authoring source;
mirror the body in minimal. Their representation-specific author guidance can
differ. Concern documents are intentionally authored for their respective forms.

### Native files and interface contracts

Use real client filenames, syntax and frontmatter. Explain the client/surface,
primary reference, relevant version/date and what was actually checked in the
associated guidance or PR. Keep syntax validation separate from client loading.
Generic samples keep executable hooks and remote plugins disabled until an
adopting team deliberately configures them.

Contract and license files retain their native format; do not force Markdown
prompts into JSON, YAML, GraphQL, Protocol Buffers or standard license text.
Shipped interface skeletons need validation appropriate to their format and
scope before downstream use.

### Sources and reuse

Link primary sources for specific external practices or format claims.
Distinguish observed practice from a proposed improvement. Write original
material rather than copying upstream templates without compatible terms.
Include attribution and preserve third-party notices where applicable.
Contributions are distributed under this repository's [MIT license](LICENSE),
with applicable third-party terms retained.

## Local checks

People using templates need no development environment. Contributors modifying
validators or checking source consistency need Python 3.11+ and Git for the Git
integration tests. From this checkout:

```sh
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in PowerShell or
`source .venv/bin/activate` in a POSIX shell, then run:

```sh
python -m pip install -r requirements-dev.txt
python -B -m unittest discover -s tests -v
python -B tools/validate_library.py --scope all
```

For prose-only changes, review links, anchors, destinations and examples in the
changed files. Validator changes need relevant regression tests; use real format
libraries and isolated Git fixtures where applicable. The
[test guide](tests/README.md) explains coverage and host-dependent skips.

The validator is read-only. The default full check validates actual template
files, complete INDEX registration and library Markdown links. Use
`--scope templates` for source roots alone. Neither scope grades prose, establishes
factual accuracy, loads clients or measures user effectiveness.

## Submit a pull request

1. Fork the repository and create a branch for one coherent change.
2. Edit the relevant source and update affected index entries, links and copy
   guidance. Keep unrelated working changes out of the PR.
3. Review the copied result from the reader's perspective. For native samples,
   record client testing only if you actually performed it.
4. Run applicable checks and report exact results, failures, skips and checks not
   run. Identify pre-existing findings separately from new regressions.
5. Use the PR template to explain the problem, resulting behavior, scope,
   supporting sources and any remaining work.

Update [CHANGELOG.md](CHANGELOG.md) under **Unreleased** for a notable user-facing
change. Typo fixes need not create individual changelog entries. Maintainers
review usefulness, overlap, copy behavior, evidence and reuse terms; a passing
test suite alone is not acceptance of new content.

## Current maintenance limits

The actual source tree and Markdown index are the navigation authority; no
machine-readable catalog is required. Update both when source files move or are
added. Static native checks cover syntax and selected generic inertness rules;
record format provenance and real loading evidence in associated guidance/review.

Inline Markdown links are checked locally, with approximate GitHub heading slugs.
External URLs, reference-style links, HTML/image links and the full CommonMark
grammar are outside the validator; review those where applicable. Expanded event
contracts and adopted client configurations need their own checks.

A passing suite/audit does not establish downstream product correctness or
measured usefulness. Historical adoption/evaluation assets are no longer present;
real client/adoption/effectiveness trials are NOT RUN unless independently
recorded. The historical migration map is retained as history, not live inventory.
