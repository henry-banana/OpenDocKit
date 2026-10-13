"""Static, offline checks. These checks never assert client loading."""

from pathlib import Path
import json
import re
import tomllib
from tools.issues import Issue
from tools.validate_contracts import load_unique_yaml
from tools.paths import contained_file

CLIENTS = {
    "portable",
    "codex",
    "claude",
    "copilot",
    "cursor",
    "gemini",
    "kiro",
    "opencode",
}


def validate_native_samples(
    root: Path, inventory: dict, *, require_provenance: bool = True
) -> list[Issue]:
    issues = []
    if not isinstance(inventory, dict) or not isinstance(
        inventory.get("templates"), list
    ):
        return [
            Issue("NATIVE_METADATA", "native samples", "Native entries must be a list.")
        ]
    for row in inventory["templates"]:
        if not isinstance(row, dict) or row.get("kind") not in (
            "native-config",
            "agent-guidance",
        ):
            continue
        relative = row.get("path")
        if not contained_file(root, relative):
            issues.append(
                Issue(
                    "UNSAFE_PATH",
                    str(relative),
                    "Native file escapes library or has an invalid path.",
                )
            )
            continue
        path = root / relative
        if not path.is_file():
            issues.append(
                Issue("MISSING_TEMPLATE", relative, "Native sample is absent.")
            )
            continue
        if require_provenance and (
            not isinstance(row.get("client"), str)
            or row.get("client") not in CLIENTS
            or any(
                not isinstance(row.get(k), str) or not row[k]
                for k in [
                    "surface",
                    "reference_url",
                    "checked_on",
                    "client_version",
                    "syntax_check",
                    "loading_check",
                ]
            )
        ):
            issues.append(
                Issue(
                    "NATIVE_METADATA",
                    relative,
                    "Need known client, format provenance and loading evidence.",
                )
            )
        try:
            text = path.read_text(encoding="utf-8")
            meta = None
            if path.suffix == ".json":
                meta = json.loads(text)
                if not isinstance(meta, dict):
                    raise ValueError("Settings must be a JSON object.")
                if meta.get("hooks") or any(
                    v is not False for v in meta.get("enabledPlugins", {}).values()
                ):
                    issues.append(
                        Issue(
                            "NATIVE_ACTIVATION",
                            relative,
                            "Generic samples must not enable executable hooks or remote plugins.",
                        )
                    )
            elif path.suffix == ".toml":
                meta = tomllib.loads(text)
            else:
                match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
                if match:
                    meta = load_unique_yaml(match.group(1))
                if path.name == "SKILL.md" and (
                    not isinstance(meta, dict)
                    or not all(
                        isinstance(meta.get(k), str) and meta[k].strip()
                        for k in ["name", "description"]
                    )
                ):
                    issues.append(
                        Issue(
                            "NATIVE_METADATA",
                            relative,
                            "Skill needs name and description frontmatter.",
                        )
                    )
                if path.suffix == ".mdc" and (
                    not isinstance(meta, dict)
                    or not isinstance(meta.get("alwaysApply"), bool)
                ):
                    issues.append(
                        Issue(
                            "NATIVE_METADATA",
                            relative,
                            "Cursor requires a boolean alwaysApply field.",
                        )
                    )
                if "/.kiro/steering/" in relative and (
                    not isinstance(meta, dict)
                    or meta.get("inclusion")
                    not in {"manual", "always", "auto", "fileMatch"}
                ):
                    issues.append(
                        Issue(
                            "NATIVE_METADATA",
                            relative,
                            "Kiro steering inclusion mode required.",
                        )
                    )
                if "/.claude/agents/" in relative and (
                    not isinstance(meta, dict)
                    or not meta.get("name")
                    or not meta.get("description")
                ):
                    issues.append(
                        Issue(
                            "NATIVE_METADATA",
                            relative,
                            "Claude role needs name and description.",
                        )
                    )
                if "/.opencode/agents/" in relative and (
                    not isinstance(meta, dict)
                    or not meta.get("description")
                    or meta.get("mode") not in {"primary", "subagent", "all"}
                ):
                    issues.append(
                        Issue(
                            "NATIVE_METADATA",
                            relative,
                            "OpenCode role needs description and mode.",
                        )
                    )
        except Exception as error:
            issues.append(Issue("NATIVE_PARSE", relative, str(error)))
    return issues
