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
            self.assertIn("图片生成工具", skill_text)
            self.assertIn("不得用代码绘制卡面", skill_text)
            self.assertIn("version: 0.3.1", skill_text)
            self.assertIn("没有图片生成工具就说明情况", skill_text)
            self.assertNotIn("精确贴纸模式", skill_text)
            self.assertFalse(output.joinpath("references/reference-remix.md").exists())
            self.assertFalse(output.joinpath("references/prompt-guide.md").exists())
            self.assertFalse(
                output.joinpath("references/bank-issuer-catalog.md").exists()
            )
            self.assertFalse(any(output.rglob("*.py")))
            self.assertFalse(any(output.rglob("requirements.txt")))
            self.assertFalse(output.joinpath("assets/logo-references").exists())
            index = output.joinpath("references/logo-reference-index.md").read_text(encoding="utf-8")
            self.assertIn("https://raw.githubusercontent.com/juju-w/card-creator-skill/main/", index)
            self.assertNotIn("../assets/logo-references/", index)
            for reference in ("banks/china/cmb.png", "banks/usa/chase.png", "overseas/japan/suica.png", "overseas/canada/presto.png", "overseas/usa/ventra.png", "overseas/south-korea/tmoney-card.jpg"):
                self.assertIn(reference, index)
            self.assertFalse(any(output.rglob("SOURCES.md")))
            self.assertFalse(output.joinpath("references/sticker-catalog.md").exists())
            self.assertFalse(output.joinpath("references/sticker-research.md").exists())
            self.assertFalse(output.joinpath("scripts/render_stickers.py").exists())
            self.assertFalse(any(output.rglob("*.png")))
            self.assertFalse(any(output.rglob("*.svg")))
            self.assertFalse(any(output.rglob(".DS_Store")))


if __name__ == "__main__":
    unittest.main()
