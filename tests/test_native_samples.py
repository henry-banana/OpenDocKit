from pathlib import Path
import tempfile
import unittest


class NativeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def check(self, path, text, client="claude"):
        from tools.validate_native_samples import validate_native_samples

        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        row = dict(
            path=path,
            kind="native-config",
            client=client,
            surface="repo",
            reference_url="https://code.claude.com/docs/en/settings",
            checked_on="2026-10-14",
            client_version="not installed",
            syntax_check="static",
            loading_check="NOT RUN",
        )
        return {
            i.code for i in validate_native_samples(self.root, {"templates": [row]})
        }

    def test_valid_settings(self):
        self.assertEqual(
            self.check(
                "sample/.claude/settings.json",
                '{"enabledPlugins":{"review@team":false}}',
            ),
            set(),
        )

    def test_malformed_settings(self):
        self.assertIn(
            "NATIVE_PARSE", self.check("sample/.claude/settings.json", "{bad")
        )

    def test_remote_plugin_is_not_enabled(self):
        self.assertIn(
            "NATIVE_ACTIVATION",
            self.check(
                "sample/.claude/settings.json",
                '{"enabledPlugins":{"review@remote":true}}',
            ),
        )

    def test_executable_hook_is_not_enabled(self):
        self.assertIn(
            "NATIVE_ACTIVATION",
            self.check(
                "sample/.claude/settings.json",
                '{"hooks":{"SessionStart":[{"hooks":[{"type":"command","command":"curl remote"}]}]}}',
            ),
        )

    def test_skill_needs_native_metadata(self):
        self.assertIn(
            "NATIVE_METADATA",
            self.check("sample/.agents/skills/review/SKILL.md", "# Only text", "codex"),
        )

    def test_unknown_client(self):
        self.assertIn(
            "NATIVE_METADATA", self.check("sample/GEMINI.md", "# Context", "invented")
        )

    def test_malformed_client_is_diagnostic(self):
        self.assertIn(
            "NATIVE_METADATA", self.check("sample/GEMINI.md", "# Context", [])
        )

    def test_toml_parse(self):
        self.assertIn(
            "NATIVE_PARSE", self.check("sample/.codex/config.toml", "bad = [", "codex")
        )

    def test_cursor_metadata(self):
        self.assertIn(
            "NATIVE_METADATA",
            self.check(
                "sample/.cursor/rules/project.mdc",
                "---\nalwaysApply: 123\n---\nRead sources",
                "cursor",
            ),
        )


if __name__ == "__main__":
    unittest.main()
