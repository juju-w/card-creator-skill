"""Keep the one-file web entry synchronized with the installed Skill."""

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "packaging" / "build_web_md.py"
OUTPUT = ROOT / "web" / "card-creator.md"


class WebGuideTests(unittest.TestCase):
    def test_web_guide_is_current_and_self_contained(self) -> None:
        spec = importlib.util.spec_from_file_location("build_web_md", SCRIPT)
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        content = OUTPUT.read_text(encoding="utf-8")
        self.assertEqual(content, module.build_text())
        self.assertIn("## Card rules", content)
        self.assertIn("1.586:1", content)
        self.assertIn("[optional picture index]", content)
        self.assertNotIn("When a logo is named, find it", content)
        self.assertNotIn("(references/card-rules.md)", content)
        self.assertNotIn("(references/logo-reference-index.md)", content)


if __name__ == "__main__":
    unittest.main()
