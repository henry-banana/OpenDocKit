"""Source checks must work without the root catalog and retain copy boundaries."""

from pathlib import Path
import tempfile
import unittest

from tools import validate_library as library


from tests.support import DOCUMENT


class TemplateSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for mode in ("minimal", "comprehensive"):
            (self.root / "templates" / mode).mkdir(parents=True)
        self.path = self.root / "templates/minimal/docs/product.md"
        self.write(self.path, DOCUMENT)
        self.comprehensive = self.root / "templates/comprehensive/docs/product.md"
        self.write(
            self.comprehensive,
            DOCUMENT.replace("ID: test.brief", "ID: test.comprehensive.brief"),
        )

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def issues(self):
        validator = getattr(library, "validate_templates", None)
        self.assertIsNotNone(
            validator, "An explicit catalog-independent source check is required."
        )
        return validator(self.root)

    def codes(self):
        return {issue.code for issue in self.issues()}

    def test_source_check_does_not_require_or_repair_catalog(self):
        (self.root / "catalog.json").write_text("{stale", encoding="utf-8")
        before = (self.root / "catalog.json").read_bytes()
        self.assertEqual(self.codes(), set())
        self.assertEqual((self.root / "catalog.json").read_bytes(), before)

    def test_destination_must_match_copy_relative_path(self):
        self.write(self.path, DOCUMENT.replace("docs/product.md", "docs/business.md"))
        self.assertIn("TEMPLATE_GUIDANCE", self.codes())

    def test_duplicate_author_ids_across_representations_are_reported(self):
        self.write(self.root / "templates/comprehensive/docs/product.md", DOCUMENT)
        self.assertIn("DUPLICATE_ID", self.codes())

    def test_unknown_representation_is_reported(self):
        self.write(self.root / "templates/extra/docs/product.md", DOCUMENT)
        self.assertIn("SOURCE_ROOT", self.codes())

    def test_copy_cannot_depend_on_other_representation(self):
        self.write(
            self.root / "templates/comprehensive/docs/architecture.md",
            "# Architecture\n",
        )
        self.write(
            self.path,
            DOCUMENT + "\n[Design](../../comprehensive/docs/architecture.md)\n",
        )
        self.assertIn("SHELF_LINK", self.codes())

    def test_missing_local_reference_is_reported(self):
        self.write(self.path, DOCUMENT + "\n[Missing](missing.md)\n")
        self.assertIn("BROKEN_LINK", self.codes())

    def test_tilde_fenced_links_are_examples(self):
        self.write(self.path, DOCUMENT + "\n~~~md\n[Example](missing.md)\n~~~\n")
        self.assertNotIn("BROKEN_LINK", self.codes())

    def test_non_utf8_target_is_a_diagnostic_not_a_crash(self):
        target = self.path.parent / "broken.md"
        target.write_bytes(b"\xff")
        self.write(self.path, DOCUMENT + "\n[Broken](broken.md#header)\n")
        self.assertIn("MARKDOWN_PARSE", self.codes())

    def test_missing_copy_root_is_reported(self):
        self.comprehensive.unlink()
        self.comprehensive.parent.rmdir()
        (self.root / "templates/comprehensive").rmdir()
        self.assertIn("SOURCE_ROOT", self.codes())

    def test_empty_copy_root_is_reported(self):
        self.comprehensive.unlink()
        self.assertIn("SOURCE_ROOT", self.codes())

    def test_non_utf8_sample_is_reported(self):
        self.path.write_bytes(b"\xff")
        self.assertIn("TEMPLATE_CONTENT", self.codes())

    def test_source_check_is_read_only(self):
        before = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*")
            if p.is_file()
        }
        self.issues()
        after = {
            p.relative_to(self.root): p.read_bytes()
            for p in self.root.rglob("*")
            if p.is_file()
        }
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
