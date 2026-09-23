"""Static checks for card faces offered as direct downloads on GitHub Pages."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GalleryAssetTests(unittest.TestCase):
    def test_featured_png_downloads_are_opaque(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        for filename in re.findall(r'image: "([^"]+)"', gallery):
            with self.subTest(filename=filename):
                path = ROOT / "examples" / filename
                self.assertTrue(path.is_file())
                if path.suffix.lower() != ".png":
                    continue
                data = path.read_bytes()
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                # PNG color types 0 and 2 have no alpha channel. A transparent
                # gallery PNG can look fine on Pages but wash out when saved.
                self.assertIn(data[25], (0, 2))


if __name__ == "__main__":
    unittest.main()
