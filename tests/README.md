# Maintainer tests

Run from the OpenDocKit checkout after the setup in [tools](../tools/README.md):

```sh
python -B -m unittest discover -s tests -v
```

For one module:

```sh
python -B -m unittest tests.test_template_sources -v
```

The suite checks the validators, not the production behavior of a project that
adopts a template. Run the full actual-library audit after the suite; passing synthetic tests does
not mean the current template tree or library navigation passes.

## Coverage

| Test module | Behavior protected |
| --- | --- |
| `test_validate_library.py` | Catalog-free full audit, index registration, CLI exit/output behavior, local links and read-only boundaries |
| `test_template_sources.py` | Source checks independent of stale catalog, destination/ID integrity, representation boundaries and read-only behavior |
| `test_validator_boundaries.py` | Malformed paths and missing native samples become findings; unsupported contracts are not compiled |
| `test_validate_contracts.py` | Valid/invalid interface formats, duplicate YAML keys, offline references and compiler failures |
| `test_native_samples.py` | Native syntax, frontmatter, provenance and disabled generic hooks/plugins |
| `test_storage_policy.py` | Actual comprehensive ignore example in disposable Git recipients, tracked-file caveat and shared-source visibility |
| `test_template_consistency.py` | Shared root boilerplate agrees between representations |

`support.py` holds reusable synthetic template/index fixtures. Tests must not import
other test modules or depend on historical demo assets. Format/parser tests use
the real installed libraries. Integration tests create temporary repositories
and never change the working checkout's index or configure a real agent client.

The ignore-policy tests describe the rules in the current source sample; they do
not certify that all privacy guidance agrees with those rules. Such content
consistency requires source review and the library audits.

## Evidence boundaries

Earlier adoption/evaluation tests required `examples/` and `evaluation/` assets
that are no longer in this checkout. Those obsolete checks were removed rather
than skipped or replaced by invented trials. Current source/link/format regressions remain; they are not adoption trials.
Restore meaningful adoption experiments
with their real fixtures and protocol in a future approved scope.

Git tests skip when Git is unavailable. Symbolic-link tests skip when the host
does not permit creating links; CI includes Ubuntu to exercise those cases.
Report the test count, failures and skips as observed, and separately identify
whether source/full audits and client/adoption checks ran.
