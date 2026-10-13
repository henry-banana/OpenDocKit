from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


@unittest.skipUnless(
    shutil.which("git"), "Git is required for isolated ignore-policy tests."
)
class StorageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(
            ["git", "init", "-q", str(self.root)], check=True, capture_output=True
        )
        (self.root / ".gitignore").write_bytes(
            (
                Path(__file__).resolve().parents[1]
                / "templates/comprehensive/.gitignore.example"
            ).read_bytes()
        )

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.root), *args], capture_output=True, text=True
        )

    def make(self, rel):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("fixture")
        return p

    def test_new_raw_ignored(self):
        self.make(".agents/artifacts/log.txt")
        self.assertEqual(
            self.git("check-ignore", ".agents/artifacts/log.txt").returncode, 0
        )

    def test_tracked_raw_stays_tracked(self):
        self.make(".agents/artifacts/log.txt")
        self.assertEqual(
            self.git("add", "-f", ".agents/artifacts/log.txt").returncode, 0
        )
        self.assertEqual(
            self.git("ls-files", ".agents/artifacts/log.txt").stdout.strip(),
            ".agents/artifacts/log.txt",
        )

    def test_private_handoff_ignored(self):
        self.make(".agents/handoffs/HANDOFF.md")
        self.assertEqual(
            self.git("check-ignore", ".agents/handoffs/HANDOFF.md").returncode, 0
        )

    def test_shared_settings_not_ignored(self):
        self.make(".claude/settings.json")
        self.assertEqual(
            self.git("check-ignore", ".claude/settings.json").returncode, 1
        )

    def test_shared_skill_is_not_ignored(self):
        self.make(".agents/skills/review/SKILL.md")
        self.assertEqual(
            self.git("check-ignore", ".agents/skills/review/SKILL.md").returncode, 1
        )

    def test_personal_settings_are_ignored(self):
        self.make(".claude/settings.local.json")
        self.assertEqual(
            self.git("check-ignore", ".claude/settings.local.json").returncode, 0
        )

    def test_shared_team_records_are_not_ignored(self):
        for path in ["docs/plans/plan-id.md", "docs/tasks/task-id.md"]:
            with self.subTest(path=path):
                self.make(path)
                self.assertEqual(self.git("check-ignore", path).returncode, 1)

    def test_info_exclude_is_local(self):
        self.make("personal.md")
        (self.root / ".git/info/exclude").write_text("/personal.md\n")
        self.assertEqual(self.git("check-ignore", "personal.md").returncode, 0)
        self.assertNotIn("personal.md", (self.root / ".gitignore").read_text())

    def test_sibling_notes_are_under_ancestor_git(self):
        code = self.root / "backend"
        code.mkdir()
        subprocess.run(
            ["git", "init", "-q", str(code)], check=True, capture_output=True
        )
        notes = self.root / "notes"
        notes.mkdir()
        result = subprocess.check_output(
            ["git", "-C", str(notes), "rev-parse", "--show-toplevel"], text=True
        )
        self.assertEqual(Path(result.strip()).resolve(), self.root.resolve())

    def test_source_samples_not_hidden_by_recipient_ignore(self):
        self.make("templates/comprehensive/.agents/handoffs/HANDOFF.md")
        self.assertEqual(
            self.git(
                "check-ignore", "templates/comprehensive/.agents/handoffs/HANDOFF.md"
            ).returncode,
            1,
        )

    def test_personal_tasks_are_ignored(self):
        self.make(".agents/tasks/task-id.md")
        self.assertEqual(
            self.git("check-ignore", ".agents/tasks/task-id.md").returncode, 0
        )


if __name__ == "__main__":
    unittest.main()
