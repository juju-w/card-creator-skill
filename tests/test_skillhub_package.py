from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import json
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = REPOSITORY / "packaging" / "skillhub-zh-CN" / "build.py"
CANONICAL_SKILL = REPOSITORY / "skills" / "card-creator"


class SkillHubPackageTests(unittest.TestCase):
    def test_build_localizes_docs_and_preserves_runtime_assets(self) -> None:
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
            self.assertIn("只有 `status: ready`", skill_text)
            self.assertTrue(
                output.joinpath("references/sticker-research.md").is_file()
            )
            self.assertTrue(
                output.joinpath("references/reference-remix.md").is_file()
            )
            self.assertTrue(
                output.joinpath("references/bank-issuer-catalog.md").is_file()
            )
            self.assertEqual(
                (output / "scripts" / "prepare_card.py").read_bytes(),
                (CANONICAL_SKILL / "scripts" / "prepare_card.py").read_bytes(),
            )
            self.assertTrue(output.joinpath("assets/stickers/manifest.json").is_file())
            self.assertTrue(output.joinpath("assets/stickers/payment/mastercard.svg").is_file())
            self.assertTrue(
                output.joinpath(
                    "assets/stickers/payment/mastercard.png.base64.txt"
                ).is_file()
            )
            self.assertFalse(
                output.joinpath(
                    "assets/stickers/generic/contactless-material.png.base64.txt"
                ).exists()
            )
            self.assertFalse(any(output.rglob("*.png")))
            self.assertFalse(any(output.rglob(".DS_Store")))

            manifest = json.loads(
                output.joinpath("assets/stickers/manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            mastercard = next(
                item for item in manifest["items"] if item["id"] == "mastercard"
            )
            self.assertEqual(
                mastercard["file"],
                "payment/mastercard.png.base64.txt",
            )
            self.assertTrue(
                all("research_file" not in item for item in manifest["items"])
            )
            issuer_banks = [
                item for item in manifest["items"] if item["category"] == "issuer-bank"
            ]
            self.assertEqual(len(issuer_banks), 25)
            self.assertTrue(all(item["status"] == "blocked" for item in issuer_banks))
            self.assertFalse(any(item["status"] == "pending" for item in manifest["items"]))
            contactless = {
                item["id"]: item for item in manifest["items"] if "contactless" in item["id"]
            }
            self.assertEqual(
                contactless["generic-contactless-material"]["status"],
                "reference-only",
            )
            self.assertEqual(contactless["emv-contactless-indicator"]["status"], "blocked")
            self.assertIsNone(contactless["generic-contactless-material"]["file"])
            self.assertIn("conventional card-face variant", manifest["variant_policy"])


if __name__ == "__main__":
    unittest.main()
