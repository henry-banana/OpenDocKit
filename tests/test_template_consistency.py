"""Shared boilerplate should not diverge between the two representations.

This check is source consistency, not an adoption or effectiveness trial.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TemplateConsistencyTests(unittest.TestCase):
    def test_shared_root_boilerplate_stays_in_sync(self):
        for name in (
            "CHANGELOG.md",
            "CODE_OF_CONDUCT.md",
            "CONTRIBUTING.md",
            "GOVERNANCE.md",
            "SECURITY.md",
            "SUPPORT.md",
            "LICENSE-MIT",
            "LICENSE-APACHE",
        ):
            with self.subTest(path=name):
                bodies = []
                for mode in ("minimal", "comprehensive"):
                    text = (ROOT / "templates" / mode / name).read_text(
                        encoding="utf-8"
                    )
                    bodies.append(
                        re.sub(
                            r"^<!-- OpenDocKit author guidance\n.*?-->\s*",
                            "",
                            text,
                            flags=re.S,
                        )
                    )
                self.assertEqual(*bodies, name)


if __name__ == "__main__":
    unittest.main()
