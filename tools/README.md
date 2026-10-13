# Maintainer tools

These checks maintain OpenDocKit itself. People adopting templates can browse,
copy and fill files without Python or these tools. Validation reads source files;
it does not install templates, update inventories or launch agent clients.

## Run locally

Use Python 3.11 or later. From the OpenDocKit checkout, create a virtual
environment and install the existing maintainer requirements:

```sh
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in PowerShell or
`source .venv/bin/activate` in a POSIX shell, then run:

```sh
python -m pip install -r requirements-dev.txt
python -B -m unittest discover -s tests -v
python -B tools/validate_library.py --scope templates
python -B tools/validate_library.py --scope all
```

The full audit is the default: `python -B tools/validate_library.py` is equivalent
to `--scope all`. The module entry point also works:
`python -B -m tools.validate_library --scope templates`.

## What each result means

| Check | What it checks | What a pass does not establish |
| --- | --- | --- |
| Regression suite | Validator behavior against valid and corrupted inputs, temporary Git ignore scenarios, shared boilerplate consistency | Whole-library consistency or user effectiveness |
| `--scope templates` | Actual `templates/minimal` and `templates/comprehensive` files, author IDs/destinations, filling structure, inline local links/copy boundaries, contract and native syntax | Root INDEX/library navigation, manual lifecycle applicability or native provenance |
| `--scope all` | Actual template checks plus complete root INDEX registration and library Markdown links | Real agent loading, adopted application behavior or completed human/agent trials |

The full audit is the default and includes the template checks. Source-only mode
is useful during focused template work; it does not certify library navigation.
Neither mode reads or requires catalog.json. The actual copy roots and root INDEX
are the source and navigation authorities.

Exit status is **0** for no findings, **1** for findings (including missing
dependencies), and **2** for invalid command-line arguments. Text diagnostics are
`FAIL CODE path: explanation`, followed by a scoped summary. For machine-readable
output or another checkout:

```sh
python -B tools/validate_library.py --root /path/to/OpenDocKit --scope templates --format json
```

JSON contains `scope`, `status` and an `issues` array with `code`, `path` and
`message`. A failure keeps the same exit status in either output format.

## Code responsibilities

| Module | Responsibility |
| --- | --- |
| `validate_library.py` | Full-library orchestration and the single CLI |
| `validate_templates.py` | Catalog-independent source discovery and content checks |
| `validate_contracts.py` | Interface skeleton validation and duplicate-key YAML parsing |
| `validate_native_samples.py` | Native syntax/frontmatter and disabled generic hook/plugin checks |
| `markdown.py`, `paths.py`, `issues.py` | Shared local-link, portable-path and diagnostic primitives |

Keep reusable checks in these modules and test fixtures in [tests](../tests/README.md).
Add a regression case for a validator behavior change. Keep source/index and link checks strict so missing content stays a finding.

## Limits and failure handling

- Inline Markdown links are checked locally; reference links, images, the full
  CommonMark grammar and external URL availability are outside this checker.
  Heading slugs approximate GitHub Markdown. Code fences, inline code and author
  comments are excluded from link checks.
- Native source discovery recognizes shipped client paths and checks syntax.
  Neither scope certifies format provenance. Review official references/client
  versions in associated guidance or PR evidence. No client is executed, so syntax
  success does not imply loading or semantic configuration support.
- Generic Claude settings must keep executable hooks and remote plugins disabled.
  This is a sample-content check, not an exhaustive security scan of every client.
- OpenAPI validation covers the shipped 3.1.0 skeleton; AsyncAPI checks cover the
  blank 3.0.0 skeleton only. Expanded event definitions need the official parser.
  YAML external references are rejected without fetching them. GraphQL and JSON
  Schema use their format libraries; Protocol Buffers invokes the installed
  compiler in a disposable directory with a timeout.
- Missing maintainer dependencies are findings. Git integration tests skip only
  when Git is unavailable; symbolic-link tests can skip on restricted Windows
  hosts. Report skips and actual environment alongside results.
- A syntax or inventory pass measures mechanical consistency. Template coverage,
  usefulness, factual accuracy and copy/adoption behavior still require review.

## Coverage and evidence

Lifecycle applicability is documented in the [coverage guide](../docs/coverage.md)
and reviewed manually; a complete index is not proof of every industry need.
Removed historical example/evaluation assets are not executed adoption evidence.
The historical migration map is a past snapshot, not the current inventory.
Record independent client loading and usefulness trials separately from static
PASS and regression-suite results.
