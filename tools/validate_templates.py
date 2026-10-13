"""Validate actual copy roots without treating an old catalog as current truth.

Source discovery checks syntax and copy boundaries. Lifecycle applicability and native provenance need review of their guidance and
primary sources; neither validation scope establishes those claims.
"""

from pathlib import Path
import re

from tools.issues import Issue
from tools.markdown import readable_markdown, validate_links
from tools.paths import contained_file
from tools.validate_contracts import validate_contracts
from tools.validate_native_samples import validate_native_samples


def native_sample(destination: str) -> bool:
    """Recognize native client surfaces, excluding personal records and issue bodies."""
    path = Path(destination)
    if path.name.upper() in {"AGENTS.MD", "CLAUDE.MD", "GEMINI.MD", "SKILL.MD"}:
        return True
    return (
        destination.startswith(
            (".claude/", ".codex/", ".cursor/", ".kiro/", ".opencode/")
        )
        or destination == ".github/copilot-instructions.md"
    )


def validate_templates(root: Path) -> list[Issue]:
    root = root.resolve()
    source = root / "templates"
    copy_roots = [source / mode for mode in ("minimal", "comprehensive")]
    issues = []
    if not source.is_dir():
        return [
            Issue("SOURCE_ROOT", "templates", "Template source directory is absent.")
        ]
    for folder in source.iterdir():
        if folder.is_dir() and folder not in copy_roots:
            issues.append(
                Issue(
                    "SOURCE_ROOT",
                    folder.relative_to(root).as_posix(),
                    "Expected minimal or comprehensive copy root.",
                )
            )
        elif folder.is_file():
            issues.append(
                Issue(
                    "SOURCE_ROOT",
                    folder.relative_to(root).as_posix(),
                    "Copyable source must belong to a representation.",
                )
            )
    identifiers = set()
    paths = set()
    contracts = []
    native = []
    markdown = []
    for folder in copy_roots:
        if not folder.is_dir() or not folder.resolve().is_relative_to(source.resolve()):
            issues.append(
                Issue(
                    "SOURCE_ROOT",
                    folder.relative_to(root).as_posix(),
                    "A contained copy root is required.",
                )
            )
            continue
        files = sorted(path for path in folder.rglob("*") if path.is_file())
        if not files:
            issues.append(
                Issue(
                    "SOURCE_ROOT",
                    folder.relative_to(root).as_posix(),
                    "Copy root contains no samples.",
                )
            )
        for path in files:
            relative = path.relative_to(root).as_posix()
            destination = path.relative_to(folder).as_posix()
            if not contained_file(root, relative) or not path.resolve().is_relative_to(
                folder.resolve()
            ):
                issues.append(
                    Issue(
                        "UNSAFE_PATH",
                        relative,
                        "Use a portable path contained in its copy root.",
                    )
                )
                continue
            folded = relative.casefold()
            if folded in paths:
                issues.append(
                    Issue("DUPLICATE_PATH", relative, "Case-insensitive collision.")
                )
            paths.add(folded)
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                issues.append(Issue("TEMPLATE_CONTENT", relative, str(error)))
                continue
            if not text.strip():
                issues.append(
                    Issue("TEMPLATE_CONTENT", relative, "Empty samples do not count.")
                )
            if path.suffix in {".md", ".mdc"}:
                markdown.append(path)
            if destination.startswith("contracts/"):
                contracts.append({"path": relative, "kind": "contract"})
                continue
            is_native = native_sample(destination)
            if is_native:
                native.append({"path": relative, "kind": "native-config"})
            guide = re.search(r"<!-- OpenDocKit author guidance\n(.*?)-->", text, re.S)
            if guide:
                fields = dict(re.findall(r"^([^:\n]+):\s*(.*)$", guide[1], re.M))
                required = (
                    "ID",
                    "Purpose",
                    "Use when",
                    "Suggested destination",
                    "Boundary",
                    "Adoption",
                )
                if (
                    not all(fields.get(key, "").strip() for key in required)
                    or fields.get("Suggested destination") != destination
                ):
                    issues.append(
                        Issue(
                            "TEMPLATE_GUIDANCE",
                            relative,
                            "Need complete author guidance and the actual copy-relative destination.",
                        )
                    )
                identifier = fields.get("ID")
                if identifier in identifiers:
                    issues.append(Issue("DUPLICATE_ID", relative, str(identifier)))
                identifiers.add(identifier)
                visible = readable_markdown(text)
                if (
                    not re.search(r"^# .+", visible, re.M)
                    or len(re.findall(r"^## .+", visible, re.M)) < 3
                    or "{{" not in visible
                    or "## Completion check" not in visible
                    or "- [ ]" not in visible
                ):
                    issues.append(
                        Issue(
                            "TEMPLATE_CONTENT",
                            relative,
                            "Need a title, specific filling prompts and completion criteria.",
                        )
                    )
            elif (
                path.suffix == ".md"
                and not is_native
                and destination
                not in {".agents/artifacts/README.md", ".local/artifacts/README.md"}
            ):
                issues.append(
                    Issue(
                        "TEMPLATE_GUIDANCE",
                        relative,
                        "Documentation sample lacks author guidance.",
                    )
                )
    issues.extend(validate_links(root, markdown, copy_roots))
    issues.extend(validate_contracts(root, contracts))
    issues.extend(
        validate_native_samples(root, {"templates": native}, require_provenance=False)
    )
    return issues
