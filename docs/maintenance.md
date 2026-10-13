# Maintainer checks

Template users browse, copy and fill without a runtime. Contributors use the
[environment and commands](../CONTRIBUTING.md#local-checks) from the checkout:

```sh
python -B -m unittest discover -s tests -v
python -B tools/validate_library.py --scope all
```

The default full check discovers actual template files, validates their structure,
paths/formats/copy boundaries, checks complete root INDEX registration and
validates library Markdown links. It does not require or produce catalog.json.
Use `--scope templates` to check source roots alone; `--root` selects another
checkout and `--format json` returns machine-readable findings.

See [tools](../tools/README.md) for precise limits and exit codes and
[tests](../tests/README.md) for regression/integration coverage. Validation is
read-only; Protocol Buffers compilation uses a disposable directory. Missing
dependencies fail rather than silently skip format validation.

Change source content, destinations, index entries and affected guidance together.
Preserve user edits and explain material moves in the changelog/migration notes.
Report observed test results, skips and CI evidence separately from real agent
loading, adoption trials and downstream product correctness. Publishing and
pushing are separate maintainer actions.
