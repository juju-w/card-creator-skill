"""Static checks for card faces offered as direct downloads on GitHub Pages."""

import re
import unittest
from datetime import datetime
from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


class GalleryAssetTests(unittest.TestCase):
    def test_gallery_and_skill_share_a_real_brand_icon(self):
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="./favicon.png"', homepage)
        self.assertIn('src="./brand/icon.png"', homepage)
        for filename in ("favicon.png", "brand/icon.png"):
            with self.subTest(filename=filename):
                data = (ROOT / filename).read_bytes()
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                self.assertIn(data[25], (0, 2))

    def test_readmes_show_project_and_directory_badges(self):
        for filename in ("README.md", "README_EN.md"):
            readme = (ROOT / filename).read_text(encoding="utf-8")
            with self.subTest(filename=filename):
                self.assertIn("img.shields.io/github/stars/juju-w/card-creator-skill", readme)
                self.assertIn("img.shields.io/github/forks/juju-w/card-creator-skill", readme)
                self.assertIn("aiagentslisting.com/mcp/card-creator-skill", readme)

    def test_all_site_card_surfaces_share_rounded_corners(self):
        css = (ROOT / "site.css").read_text(encoding="utf-8")
        self.assertIn(
            ".hero-preview,.work-preview,.artwork-dialog>img{border-radius:3.7% / 5.9%}",
            css,
        )
        self.assertIn(".artwork-dialog>img{width:auto;max-width:100%;margin-inline:auto}", css)

    def test_dialog_hides_old_image_until_replacement_decodes(self):
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "site.js").read_text(encoding="utf-8")
        self.assertIn('id="dialog-image-status"', homepage)
        self.assertIn('image.hidden = true;', script)
        self.assertIn('await nextImage.decode();', script)
        self.assertIn('image.replaceWith(nextImage);', script)
        self.assertIn('requestId !== imageRequestId', script)

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
            showcase = re.findall(r'<img src="examples/([^"]+)" width="320"', content)
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
                with Image.open(path) as image:
                    # RGBA is valid if every alpha pixel is opaque. Color type
                    # alone misses palette transparency and rejects opaque RGBA.
                    self.assertEqual(image.convert("RGBA").getchannel("A").getextrema(), (255, 255))

    def test_newest_sort_uses_dated_gallery_entries(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        rows = re.findall(r'^\s*\{ id: "[^"]+".*image: "[^"]+".*$', gallery, re.M)
        self.assertTrue(rows)
        for row in rows:
            with self.subTest(row=row[:80]):
                match = re.search(r'publishedAt: "([^"]+)"', row)
                self.assertIsNotNone(match)
                self.assertIsNotNone(datetime.fromisoformat(match.group(1)).tzinfo)

        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "site.js").read_text(encoding="utf-8")
        self.assertIn('<option value="newest">最新发布</option>', homepage)
        self.assertIn('Date.parse(b.publishedAt) - Date.parse(a.publishedAt)', script)
        self.assertNotIn('visible.reverse()', script)

    def test_overseas_city_selection_uses_new_london_and_centered_niu_lai(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        for filename in (
            "london-oyster-impasto-v2.png",
            "new-york-omny-graphic.png",
            "sydney-opal-jacaranda.png",
            "venice-venezia-unica-marble-lion.png",
            "niu-lai-amex-parody.png",
        ):
            with self.subTest(filename=filename):
                self.assertIn(f'image: "{filename}"', gallery)
        self.assertNotIn("london-oyster-rainy-night.png", gallery)

    def test_sports_series_contains_five_traceable_unofficial_cards(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        records = (ROOT / "examples/SPORTS.md").read_text(encoding="utf-8")
        sources = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
        self.assertIn('sports: "体育系列"', gallery)
        self.assertIn('data-series="sports"', homepage)
        rows = [row for row in gallery.splitlines() if 'series: "sports"' in row]
        self.assertEqual(len(rows), 5)
        for row in rows:
            filename = re.search(r'image: "([^"]+)"', row).group(1)
            with self.subTest(filename=filename):
                self.assertIn(filename, records)
                self.assertIn(filename, sources)
                self.assertIn('非官方 AI 球迷艺术', row)
                self.assertIn('brief:', row)
                self.assertIn('prompt:', row)
        self.assertNotIn('messi', gallery.lower())

    def test_rights_notice_reaches_grid_footer_and_download(self):
        homepage = (ROOT / "index.html").read_text(encoding="utf-8")
        disclaimer = (ROOT / "DISCLAIMER.md").read_text(encoding="utf-8")
        self.assertIn('class="rights-notice gallery-rights"', homepage)
        self.assertIn('aria-describedby="download-rights"', homepage)
        self.assertIn('id="download-rights"', homepage)
        self.assertIn('权利反馈 / 申请移除', homepage)
        self.assertIn('不代表授权、联名、赞助或代言', homepage)
        self.assertIn('不是自动免责的依据', disclaimer)
        self.assertIn('Issue 是公开渠道', disclaimer)
        self.assertIn('likeness', disclaimer)

    def test_portrait_cards_are_not_cropped_into_landscape_previews(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        script = (ROOT / "site.js").read_text(encoding="utf-8")
        css = (ROOT / "site.css").read_text(encoding="utf-8")
        for name in ("manjushri-mineral-landscape", "yellow-jambhala-mineral-unionpay"):
            row = next(row for row in gallery.splitlines() if f'id: "{name}"' in row)
            self.assertIn('orientation: "portrait"', row)
            with Image.open(ROOT / "examples" / (name + ".png")) as image:
                self.assertGreater(image.height, image.width)
        self.assertIn('preview.classList.toggle("is-portrait", work.orientation === "portrait")', script)
        self.assertIn('.work-preview.is-portrait img{width:auto;height:100%;aspect-ratio:auto;object-fit:contain;', css)

    def test_restored_contours_have_navigation_limits_and_provenance(self):
        gallery = (ROOT / "gallery-data.js").read_text(encoding="utf-8")
        records = (ROOT / "examples/HIMALAYAN-SACRED.md").read_text(encoding="utf-8")
        for name in ("everest-lhotse-contours", "machhapuchhre-mbc-abc-contours"):
            row = next(row for row in gallery.splitlines() if f'id: "{name}"' in row)
            self.assertIn('series: "nature"', row)
            self.assertIn('导航', row)
            self.assertIn(name + ".png", records)
        self.assertIn('Esri', records)
        self.assertIn('OpenStreetMap', records)


if __name__ == "__main__":
    unittest.main()
