import unittest


class TestBug3(unittest.TestCase):
    def test_counts_items(self):
        from shopping import total_items
        self.assertEqual(total_items(["bread", "milk"]), 2)

    def test_empty_list(self):
        from shopping import total_items
        self.assertEqual(total_items([]), 0)


if __name__ == "__main__":
    unittest.main()
