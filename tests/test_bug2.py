import unittest


class TestBug2(unittest.TestCase):
    def test_greets_by_name(self):
        from greeting import greet
        self.assertEqual(greet("Sam"), "Hello, Sam!")

    def test_greets_without_name(self):
        from greeting import greet
        self.assertEqual(greet(""), "Hello, there!")


if __name__ == "__main__":
    unittest.main()
