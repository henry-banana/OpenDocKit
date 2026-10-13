"""Malformed public inputs produce findings; validation never follows escapes."""

from pathlib import Path
import tempfile
import unittest

from tools.validate_contracts import validate_contracts
from tools.validate_native_samples import validate_native_samples


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_contract_path_type_is_diagnostic(self):
        issues = validate_contracts(self.root, [{"kind": "contract", "path": []}])
        self.assertIn("UNSAFE_PATH", {issue.code for issue in issues})

    def test_native_path_type_is_diagnostic(self):
        issues = validate_native_samples(
            self.root, {"templates": [{"kind": "native-config", "path": []}]}
        )
        self.assertIn("UNSAFE_PATH", {issue.code for issue in issues})

    def test_missing_native_file_is_diagnostic(self):
        issues = validate_native_samples(
            self.root,
            {"templates": [{"kind": "native-config", "path": "missing.json"}]},
        )
        self.assertIn("MISSING_TEMPLATE", {issue.code for issue in issues})

    def test_unknown_contract_extension_is_not_compiled_as_proto(self):
        (self.root / "schema.txt").write_text('syntax = "proto3";', encoding="utf-8")
        issues = validate_contracts(
            self.root, [{"kind": "contract", "path": "schema.txt"}]
        )
        self.assertIn("CONTRACT_FORMAT", {issue.code for issue in issues})

    def test_dot_is_not_a_file_path(self):
        from tools.validate_library import safe_relative

        self.assertFalse(safe_relative("."))

    def test_graphql_named_text_file_is_an_unsupported_format(self):
        (self.root / "graphql.txt").write_text(
            "type Query { value: String }", encoding="utf-8"
        )
        issues = validate_contracts(
            self.root, [{"kind": "contract", "path": "graphql.txt"}]
        )
        self.assertIn("CONTRACT_FORMAT", {issue.code for issue in issues})


if __name__ == "__main__":
    unittest.main()
