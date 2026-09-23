"""Static checks for card faces offered as direct downloads on GitHub Pages."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GalleryAssetTests(unittest.TestCase):
    def test_all_site_card_surfaces_share_rounded_corners(self):
        css = (ROOT / "site.css").read_text(encoding="utf-8")
        self.assertIn(
            ".hero-preview,.work-preview,.artwork-dialog>img{border-radius:3.7% / 5.9%}",
            css,
        )
        self.assertIn(".artwork-dialog>img{width:auto;max-width:100%;margin-inline:auto}", css)

    def test_site_brand_matches_skill_and_gallery(self):
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("<title>Card Creator · 卡面画廊</title>", homepage)
        self.assertIn('content="Card Creator · 卡面画廊"', homepage)
        self.assertIn('aria-label="Card Creator 卡面画廊首页"', homepage)
        self.assertEqual(homepage.count("CARD CREATOR"), 2)
        self.assertNotIn("Make Your Card", homepage)

    def test_homepage_showcase_matches_curated_lead(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        featured = re.findall(r'image: "([^"]+)"', gallery)[:6]
        self.assertEqual(len(featured), 6)
        for readme in ("README.md", "README_EN.md"):
            content = (ROOT / readme).read_text(encoding="utf-8")
            showcase = re.findall(r'<img src="examples/([^"]+)" width="420"', content)
            with self.subTest(readme=readme):
                self.assertEqual(showcase, featured)
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(f'<img src="./examples/{featured[0]}"', homepage)

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
