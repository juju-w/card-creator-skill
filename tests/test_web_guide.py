"""Keep the one-file web entry synchronized with the installed Skill."""

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


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
        self.assertIn("[picture index](https://raw.githubusercontent.com/", content)
        self.assertNotIn("(references/card-rules.md)", content)
        self.assertNotIn("(references/logo-reference-index.md)", content)

        # Changing shared behavior must reach Web without a second rewrite table.
        with patch.object(module, "workflow", return_value=module.workflow() + "\n\nA new shared decision."), patch.object(module, "card_rules", return_value=module.card_rules() + "\n\nA new canvas rule."):
            rebuilt = module.build_text()
        self.assertEqual(rebuilt.count("A new shared decision."), 1)
        self.assertEqual(rebuilt.count("A new canvas rule."), 1)


if __name__ == "__main__":
    unittest.main()
