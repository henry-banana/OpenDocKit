"""The full audit follows actual sources and navigation, without a catalog."""

from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

from tests.support import library_fixture
from tools.validate_library import validate_library


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.minimal, self.comprehensive = library_fixture(self.root)

    def codes(self):
        return {issue.code for issue in validate_library(self.root)}

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_valid_library_without_catalog(self):
        self.assertEqual(self.codes(), set())

    def test_obsolete_catalog_is_not_a_source_authority(self):
        self.write("catalog.json", "{obsolete")
        self.assertEqual(self.codes(), set())

    def test_missing_index_is_reported(self):
        (self.root / "INDEX.md").unlink()
        self.assertIn("INDEX_ENTRY", self.codes())

    def test_missing_index_entry_is_reported(self):
        self.write("INDEX.md", "# Index\n")
        self.assertIn("INDEX_ENTRY", self.codes())

    def test_reference_inside_example_code_does_not_index_a_source(self):
        self.write(
            "INDEX.md",
            "# Index\n```md\n[Product](templates/minimal/docs/product.md)\n```\n",
        )
        self.assertIn("INDEX_ENTRY", self.codes())

    def test_non_utf8_index_is_diagnostic(self):
        (self.root / "INDEX.md").write_bytes(b"\xff")
        self.assertIn("MARKDOWN_PARSE", self.codes())

    def test_source_failure_is_not_hidden_by_full_scope(self):
        self.minimal.write_text(
            self.minimal.read_text(encoding="utf-8").replace(
                "docs/product.md", "docs/business.md"
            ),
            encoding="utf-8",
        )
        self.assertIn("TEMPLATE_GUIDANCE", self.codes())

    def test_broken_library_link_is_reported(self):
        self.write("docs/guide.md", "# Guide\n\n[Missing](gone.md)\n")
        self.assertIn("BROKEN_LINK", self.codes())

    def test_broken_anchor_is_reported(self):
        self.write(
            "README.md",
            "# Start\n\n[Product](templates/minimal/docs/product.md#absent)\n",
        )
        self.assertIn("BROKEN_ANCHOR", self.codes())

    def test_fenced_links_are_examples(self):
        self.write("README.md", "# Start\n\n```md\n[Example](missing.md)\n```\n")
        self.assertNotIn("BROKEN_LINK", self.codes())

    def test_escaping_library_link_is_reported(self):
        self.write("README.md", "# Start\n\n[Private](../outside.md)\n")
        self.assertIn("UNSAFE_LINK", self.codes())

    def test_environment_directories_are_excluded(self):
        self.write(".venv/guide.md", "[Example](missing.md)\n")
        self.assertNotIn("BROKEN_LINK", self.codes())

    def test_non_utf8_library_document_is_reported(self):
        (self.root / "README.md").write_bytes(b"\xff")
        self.assertIn("MARKDOWN_PARSE", self.codes())

    def test_read_only_full_validation(self):
        before = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*")
            if p.is_file()
        }
        validate_library(self.root)
        after = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*")
            if p.is_file()
        }
        self.assertEqual(before, after)

    def test_default_cli_passes_without_catalog(self):
        script = Path(__file__).resolve().parents[1] / "tools/validate_library.py"
        result = subprocess.run(
            [
                sys.executable,
                "-B",
                str(script),
                "--root",
                str(self.root),
                "--format",
                "json",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(
            json.loads(result.stdout), {"scope": "all", "status": "PASS", "issues": []}
        )

    def test_cli_failure_stays_nonzero_with_json_output(self):
        self.write("INDEX.md", "# Index\n")
        script = Path(__file__).resolve().parents[1] / "tools/validate_library.py"
        result = subprocess.run(
            [
                sys.executable,
                "-B",
                str(script),
                "--root",
                str(self.root),
                "--format",
                "json",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["status"], "FAIL")

    def test_symlink_escape_is_reported(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.md"
            target.write_text("# Private\n", encoding="utf-8")
            try:
                (self.root / "README.md").symlink_to(target)
            except OSError as error:
                self.skipTest(f"Host does not permit symbolic links: {error}")
            self.assertIn("UNSAFE_LINK", self.codes())


if __name__ == "__main__":
    unittest.main()
