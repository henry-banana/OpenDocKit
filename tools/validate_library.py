"""Read-only validation of actual template sources and library navigation."""

from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import json
import os
import re
import sys

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.issues import Issue
from tools.paths import safe_relative as safe_relative
from tools.markdown import readable_markdown, validate_links
from tools.validate_templates import validate_templates


EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".ruff_cache",
    ".pytest_cache",
}


def library_markdown_paths(root: Path) -> list[Path]:
    """Source links are already checked inside their copy roots."""
    paths = []
    for directory, folders, files in os.walk(root, followlinks=False):
        folders[:] = [
            name
            for name in folders
            if name not in EXCLUDED_DIRECTORIES
            and not (Path(directory) == root and name == "templates")
        ]
        paths.extend(
            Path(directory) / name
            for name in files
            if Path(name).suffix in {".md", ".mdc"}
        )
    return sorted(paths)


def validate_library(root: Path) -> list[Issue]:
    root = root.resolve()
    issues = validate_templates(root)
    try:
        index = (root / "INDEX.md").read_text(encoding="utf-8")
    except FileNotFoundError:
        index = ""
    except (OSError, UnicodeError) as error:
        issues.append(Issue("MARKDOWN_PARSE", "INDEX.md", str(error)))
        index = ""
    indexed = set()
    for target in re.findall(
        r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)", readable_markdown(index)
    ):
        try:
            parsed = urlsplit(target.strip().strip("<>"))
        except ValueError:
            continue  # The link validator reports malformed targets.
        if not parsed.scheme and not parsed.netloc:
            indexed.add(unquote(parsed.path))
    for mode in ("minimal", "comprehensive"):
        folder = root / "templates" / mode
        for path in sorted(folder.rglob("*")) if folder.is_dir() else []:
            if path.is_file():
                relative = path.relative_to(root).as_posix()
                if relative not in indexed:
                    issues.append(
                        Issue("INDEX_ENTRY", relative, "Missing from root INDEX.md.")
                    )
    issues.extend(validate_links(root, library_markdown_paths(root), []))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Library checkout to check; defaults to this checkout.",
    )
    parser.add_argument(
        "--scope",
        choices=("all", "templates"),
        default="all",
        help="all: actual templates, complete INDEX and library Markdown links; templates: copy roots only.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Diagnostic output format.",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    issues = validate_library(root) if args.scope == "all" else validate_templates(root)
    if args.format == "json":
        from dataclasses import asdict

        print(
            json.dumps(
                {
                    "scope": args.scope,
                    "status": "FAIL" if issues else "PASS",
                    "issues": [asdict(issue) for issue in issues],
                },
                indent=2,
            )
        )
    else:
        for issue in issues:
            print(f"FAIL {issue.code} {issue.path}: {issue.message}")
        status = "FAIL" if issues else "PASS"
        print(
            f"{status} scope={args.scope} findings={len(issues)}; read-only static validation"
        )
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
