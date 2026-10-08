import pathlib
import unittest

LINES = [l.strip() for l in pathlib.Path("profile.md").read_text(encoding="utf-8").splitlines() if l.strip()]


class TestBug1(unittest.TestCase):
    def test_heading(self):
        self.assertTrue(LINES[0].startswith("# "), "The first line should be a heading: a # then a space.")

    def test_list_item(self):
        self.assertIn(LINES[1][:2], ("- ", "* "), "'Learn Git' should be a list item: start it with '- '.")

    def test_bold(self):
        self.assertIn("**Learn pull requests**", LINES[2], "'Learn pull requests' should be bold.")
        self.assertIn(LINES[2][:2], ("- ", "* "), "'Learn pull requests' should also be a list item.")

    def test_link(self):
        self.assertIn("[ACCA website](http", LINES[3], "The link isn't written correctly yet.")


if __name__ == "__main__":
    unittest.main()
