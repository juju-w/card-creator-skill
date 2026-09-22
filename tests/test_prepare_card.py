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
    def test_cover_exports_three_300_dpi_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            artwork = root / "artwork.png"
            output = root / "output"
            Image.new("RGB", (1586, 1000), "#f4efe3").save(artwork)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(artwork),
                    "--output-dir",
                    str(output),
                    "--name",
                    "generated",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            result = json.loads(completed.stdout)
            self.assertEqual(result["dimensions"]["trim"], [1011, 638])
            self.assertEqual(result["dimensions"]["bleed"], [1081, 708])
            self.assertNotIn("stickers", result)
            for suffix, expected_size in (
                ("trim", (1011, 638)),
                ("bleed", (1081, 708)),
                ("guides", (1081, 708)),
            ):
                with Image.open(output / f"generated-{suffix}.png") as image:
                    self.assertEqual(image.size, expected_size)
                    self.assertEqual(image.mode, "RGB")
                    self.assertAlmostEqual(image.info["dpi"][0], 300, delta=1)

    def test_contain_mode_preserves_edge_content_with_inset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            artwork = root / "artwork.png"
            output = root / "output"
            source = Image.new("RGB", (1500, 1000), "#f6f0e6")
            source.putpixel((0, 0), (180, 20, 20))
            source.putpixel((1499, 999), (20, 20, 180))
            source.save(artwork)

            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(artwork),
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
