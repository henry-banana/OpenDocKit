"""Small synthetic source fixtures, independent of changing product examples."""

from pathlib import Path

DOCUMENT = """<!-- OpenDocKit author guidance
ID: test.brief
Purpose: Describe the user problem.
Use when: Defining an initiative.
Suggested destination: docs/product.md
Boundary: Design lives in architecture.
Adoption: Fill actual evidence.
-->
# Product

## Problem
{{Describe the problem.}}

## Evidence
{{Link evidence.}}

## Completion check
- [ ] Evidence supports the problem.
"""


def library_fixture(root: Path) -> tuple[Path, Path]:
    paths = []
    for mode in ("minimal", "comprehensive"):
        path = root / "templates" / mode / "docs/product.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            DOCUMENT.replace("ID: test.brief", "ID: test." + mode + ".brief"),
            encoding="utf-8",
        )
        paths.append(path)
    (root / "INDEX.md").write_text(
        "# Index\n\n"
        + "\n".join("[Product](" + p.relative_to(root).as_posix() + ")" for p in paths)
        + "\n",
        encoding="utf-8",
    )
    return tuple(paths)
