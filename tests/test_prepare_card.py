from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


REPOSITORY = Path(__file__).resolve().parents[1]
SCRIPT = REPOSITORY / "skills" / "card-creator" / "scripts" / "prepare_card.py"


class PrepareCardTests(unittest.TestCase):
    def test_compact_unionpay_foil_gold_with_explicit_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            background = root / "background.png"
            output = root / "output"
            Image.new("RGB", (1586, 1000), "#f4efe3").save(background)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(background),
                    "--output-dir",
                    str(output),
                    "--name",
                    "styled",
                    "--sticker",
                    "unionpay-compact@bottom-right",
                    "--sticker-style",
                    "unionpay-compact=foil-gold",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            result = json.loads(completed.stdout)
            self.assertEqual(result["dimensions"]["trim"], [1011, 638])
            self.assertEqual(
                result["sticker_placements"],
                [
                    {
                        "id": "unionpay-compact",
                        "anchor": "bottom-right",
                        "style": "foil-gold",
                        "width": "default",
                    }
                ],
            )
            with Image.open(output / "styled-trim.png") as image:
                self.assertEqual(image.size, (1011, 638))
            self.assertEqual(image.mode, "RGB")

    def test_explicit_large_sticker_width_may_cross_advisory_safe_area(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            background = root / "background.png"
            output = root / "output"
            Image.new("RGB", (1586, 1000), "white").save(background)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(background),
                    "--output-dir",
                    str(output),
                    "--sticker",
                    "unionpay-compact@bottom-right",
                    "--sticker-width",
                    "unionpay-compact=420",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            result = json.loads(completed.stdout)
            self.assertEqual(result["sticker_placements"][0]["width"], 420)
            with Image.open(output / "card-face-trim.png") as image:
                self.assertEqual(image.size, (1011, 638))

    def test_center_column_anchor_supports_collage_layouts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            background = root / "background.png"
            output = root / "output"
            Image.new("RGB", (1586, 1000), "#77b72b").save(background)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(background),
                    "--output-dir",
                    str(output),
                    "--sticker",
                    "mastercard@top-center",
                    "--sticker",
                    "unionpay-compact@center-center",
                    "--sticker",
                    "suica@bottom-center",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            placements = json.loads(completed.stdout)["sticker_placements"]
            self.assertEqual(
                [placement["anchor"] for placement in placements],
                ["top-center", "center-center", "bottom-center"],
            )
            with Image.open(output / "card-face-trim.png") as image:
                self.assertEqual(image.size, (1011, 638))

    def test_non_ready_sticker_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            background = root / "background.png"
            Image.new("RGB", (1586, 1000), "white").save(background)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(background),
                    "--output-dir",
                    str(root / "output"),
                    "--sticker",
                    "generic-contactless-material@center-right",
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("not approved/ready", completed.stderr)

    def test_contain_mode_preserves_edge_content_with_inset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            background = root / "background.png"
            output = root / "output"
            source = Image.new("RGB", (1500, 1000), "#f6f0e6")
            source.putpixel((0, 0), (180, 20, 20))
            source.putpixel((1499, 999), (20, 20, 180))
            source.save(background)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(background),
                    "--output-dir",
                    str(output),
                    "--name",
                    "contained",
                    "--fit-mode",
                    "contain",
                    "--contain-inset",
                    "20",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            result = json.loads(completed.stdout)
            self.assertEqual(result["fit"], {"mode": "contain", "contain_inset": 20})
            with Image.open(output / "contained-trim.png") as image:
                self.assertEqual(image.size, (1011, 638))
                self.assertNotEqual(image.getpixel((0, 0)), (180, 20, 20))


if __name__ == "__main__":
    unittest.main()
