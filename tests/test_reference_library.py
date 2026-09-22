"""Repository checks, never part of the installed image-generation skill."""
import re
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/card-creator"
PICTURES = SKILL / "assets/logo-references"


class ReferenceLibraryTests(unittest.TestCase):
    def test_every_picture_has_an_index_entry_and_external_source(self):
        index = (SKILL / "references/logo-reference-index.md").read_text()
        sources = (ROOT / "SOURCES.md").read_text()
        files = {str(p.relative_to(PICTURES)) for p in PICTURES.rglob("*.png")}
        linked = set(re.findall(r"\]\(../assets/logo-references/([^\s)]+\.png)\)", index))
        self.assertEqual(files, linked)
        for file in files:
            self.assertIn("`" + file + "`", sources, file)
            data = (PICTURES / file).read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n", file)
            width, height = struct.unpack(">II", data[16:24])
            self.assertGreater(width, 0, file)
            self.assertGreater(height, 0, file)

    def test_required_banks_and_countries_are_present(self):
        for bank in ("icbc", "abc", "boc", "ccb", "bocom", "psbc", "cmb", "citic", "everbright", "minsheng", "industrial", "spdb", "pingan", "guangfa"):
            self.assertTrue((PICTURES / f"banks/china/{bank}.png").is_file(), bank)
        for region in ("japan", "hong-kong", "usa", "uk", "germany", "australia"):
            self.assertTrue(list((PICTURES / "overseas" / region).glob("*.png")), region)
        for file in ("chase", "citi", "bank-of-america", "wells-fargo"):
            self.assertTrue((PICTURES / f"banks/usa/{file}.png").is_file())
        for file in ("barclays", "lloyds", "natwest"):
            self.assertTrue((PICTURES / f"banks/uk/{file}.png").is_file())
        self.assertTrue((PICTURES / "overseas/japan/suica.png").is_file())
        self.assertFalse((PICTURES / "overseas/suica.png").exists())

    def test_fintech_references_are_present(self):
        for name in ("wise", "bybit", "apple-cash", "x-money-symbol", "x-money-card"):
            self.assertTrue((PICTURES / f"fintech/{name}.png").is_file(), name)

    def test_installed_skill_stays_small_and_script_free(self):
        self.assertFalse(any(SKILL.rglob("*.py")))
        self.assertFalse(any(SKILL.rglob("*.svg")))
        self.assertFalse(any(SKILL.rglob("SOURCES.md")))
        self.assertEqual({p.name for p in (SKILL / "references").glob("*.md")}, {"card-rules.md", "logo-reference-index.md"})
        self.assertLess(len((SKILL / "SKILL.md").read_text().split()), 450)
        self.assertLess(len((SKILL / "references/card-rules.md").read_text().split()), 150)
        self.assertIn(b"Dzyuzin", (PICTURES / "payment/mir.png").read_bytes())


if __name__ == "__main__":
    unittest.main()
