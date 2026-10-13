"""Validate the shipped interface skeletons without executing target code.

AsyncAPI checks intentionally cover this library's blank 3.0 skeleton, not
arbitrary expanded event definitions. Use the official parser after adoption.
"""

from pathlib import Path
from importlib import import_module
import json
import subprocess
import sys
import tempfile

from tools.issues import Issue
from tools.paths import contained_file


def validate_contracts(root: Path, entries: list[dict]) -> list[Issue]:
    issues: list[Issue] = []
    for row in entries:
        if not isinstance(row, dict) or row.get("kind") != "contract":
            continue
        relative = row.get("path")
        if not contained_file(root, relative):
            issues.append(
                Issue(
                    "UNSAFE_PATH",
                    str(relative),
                    "Use a contained portable contract path.",
                )
            )
            continue
        path = root / relative
        name = path.name
        if not path.is_file():
            issues.append(
                Issue("MISSING_TEMPLATE", relative, "Registered contract is absent.")
            )
            continue
        if not path.resolve().is_relative_to(root.resolve()):
            issues.append(
                Issue("UNSAFE_PATH", relative, "Contract resolves outside the library.")
            )
            continue
        try:
            text = path.read_text(encoding="utf-8")
            if name.endswith(".json"):
                try:
                    obj = json.loads(text)
                except ValueError as error:
                    issues.append(Issue("CONTRACT_PARSE", relative, str(error)))
                    continue
                from jsonschema import Draft202012Validator

                Draft202012Validator.check_schema(obj)
            elif name.endswith(".yaml"):
                import yaml

                try:
                    obj = load_unique_yaml(text)
                except yaml.YAMLError as error:
                    issues.append(Issue("CONTRACT_PARSE", relative, str(error)))
                    continue
                if not isinstance(obj, dict):
                    raise ValueError("A contract must be an object.")
                reject_external_references(obj)
                if name.startswith("openapi"):
                    if obj.get("openapi") != "3.1.0":
                        raise ValueError("The shipped OpenAPI skeleton declares 3.1.0.")
                    from openapi_spec_validator import validate

                    validate(obj)
                else:
                    if obj.get("asyncapi") != "3.0.0":
                        raise ValueError(
                            "The shipped AsyncAPI skeleton declares 3.0.0."
                        )
                    info = obj.get("info")
                    if not isinstance(info, dict) or not all(
                        isinstance(info.get(k), str) and info[k]
                        for k in ["title", "version"]
                    ):
                        raise ValueError(
                            "AsyncAPI info requires non-empty title and version strings."
                        )
                    if obj.get("channels") != {} or obj.get("operations") != {}:
                        raise ValueError(
                            "Expanded event definitions require the official AsyncAPI parser; this check covers the shipped blank skeleton."
                        )
            elif path.suffix == ".graphql":
                from graphql import build_schema, validate_schema

                errors = validate_schema(build_schema(text))
                if errors:
                    raise ValueError("; ".join(str(e) for e in errors))
            elif path.suffix == ".proto":
                # Verify availability before starting the compiler.
                import_module("grpc_tools")

                with tempfile.TemporaryDirectory(prefix="opendockit-proto-") as temp:
                    temp_path = Path(temp)
                    source = temp_path / "schema.proto"
                    source.write_text(text, encoding="utf-8")
                    result = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "grpc_tools.protoc",
                            "--proto_path=" + str(temp_path),
                            "--descriptor_set_out=" + str(temp_path / "schema.pb"),
                            str(source),
                        ],
                        capture_output=True,
                        text=True,
                        timeout=20,
                    )
                    if result.returncode:
                        raise ValueError(
                            result.stderr.strip() or "Proto compilation failed."
                        )
            else:
                issues.append(
                    Issue(
                        "CONTRACT_FORMAT",
                        relative,
                        "Supported formats: JSON Schema, OpenAPI/AsyncAPI YAML, GraphQL and Protocol Buffers.",
                    )
                )
        except ImportError as error:
            issues.append(
                Issue(
                    "DEPENDENCY",
                    relative,
                    f"{error}; install maintainer requirements-dev.txt.",
                )
            )
        except (OSError, UnicodeError, subprocess.TimeoutExpired) as error:
            issues.append(Issue("CONTRACT_PARSE", relative, str(error)))
        except Exception as error:
            # Format libraries use different exception types; report all validation
            # failures without aborting the remaining library checks.
            issues.append(Issue("CONTRACT_SCHEMA", relative, str(error)))
    return issues


def reject_external_references(value: object) -> None:
    """Keep validation offline; adopted multi-file contracts need their own tooling."""
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "$ref" and (
                not isinstance(item, str) or not item.startswith("#")
            ):
                raise ValueError(
                    "External references are not fetched by the library validator."
                )
            reject_external_references(item)
    elif isinstance(value, list):
        for item in value:
            reject_external_references(item)


def load_unique_yaml(text: str) -> object:
    """Reject silent last-key-wins mistakes in contract authoring."""
    import yaml

    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        loader.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise yaml.constructor.ConstructorError(
                    "contract mapping",
                    node.start_mark,
                    f"duplicate key: {key}",
                    key_node.start_mark,
                )
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping
    )
    return yaml.load(text, Loader=UniqueLoader)
