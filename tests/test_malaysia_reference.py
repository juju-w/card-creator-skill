"""The default Malaysia reference is the transit mark, not the eWallet icon."""
import hashlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MalaysiaReferenceTests(unittest.TestCase):
    def test_official_downloads_and_index_are_preserved(self):
        expected = {
            "touch-n-go.png": "3c85821db31a6a5f2aa2d35d53ccad56e4234e094fff1268963f0c999e0e2bf0",
            "touch-n-go-card-reference.png": "c05c68105e87a739a4bd778628bf31fd08495a5025c29ca2ceaa1de8c8b5d7ce",
        }
        index = (ROOT / "skills/card-creator/references/logo-reference-index.md").read_text()
        sources = (ROOT / "SOURCES.md").read_text()
        for filename, digest in expected.items():
            relative = "overseas/malaysia/" + filename
            path = ROOT / "skills/card-creator/assets/logo-references" / relative
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)
            self.assertIn(relative, index)
            self.assertIn(relative, sources)
        self.assertIn("not the eWallet variant", index)


if __name__ == "__main__":
    unittest.main()
