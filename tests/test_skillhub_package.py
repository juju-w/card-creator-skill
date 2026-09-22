from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = REPOSITORY / "packaging" / "skillhub-zh-CN" / "build.py"
CANONICAL_SKILL = REPOSITORY / "skills" / "card-creator"


class SkillHubPackageTests(unittest.TestCase):
    def test_build_localizes_docs_and_omits_binary_references(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "card-creator"
            subprocess.run(
                [sys.executable, str(BUILD_SCRIPT), str(output)],
                check=True,
                capture_output=True,
                text=True,
            )

            skill_text = (output / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("displayName: 卡面生成器", skill_text)
            self.assertIn("首先调用 ImageGen", skill_text)
            self.assertIn("不得使用", skill_text)
            self.assertNotIn("精确贴纸模式", skill_text)
            self.assertTrue(
                output.joinpath("references/reference-remix.md").is_file()
            )
            self.assertFalse(
                output.joinpath("references/bank-issuer-catalog.md").exists()
            )
            self.assertEqual(
                (output / "scripts" / "prepare_card.py").read_bytes(),
                (CANONICAL_SKILL / "scripts" / "prepare_card.py").read_bytes(),
            )
            self.assertFalse(output.joinpath("assets/logo-references").exists())
            self.assertFalse(output.joinpath("references/logo-reference-index.md").exists())
            self.assertFalse(output.joinpath("references/sticker-catalog.md").exists())
            self.assertFalse(output.joinpath("references/sticker-research.md").exists())
            self.assertFalse(output.joinpath("scripts/render_stickers.py").exists())
            self.assertFalse(any(output.rglob("*.png")))
            self.assertFalse(any(output.rglob("*.svg")))
            self.assertFalse(any(output.rglob(".DS_Store")))


if __name__ == "__main__":
    unittest.main()
