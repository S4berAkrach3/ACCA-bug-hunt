import unittest


class TestBug5(unittest.TestCase):
    def test_whole_pounds(self):
        from prices import format_price
        self.assertEqual(format_price(5), "£5.00")

    def test_pence(self):
        from prices import format_price
        self.assertEqual(format_price(4.5), "£4.50")

    def test_rounds(self):
        from prices import format_price
        self.assertEqual(format_price(3.999), "£4.00")


if __name__ == "__main__":
    unittest.main()
