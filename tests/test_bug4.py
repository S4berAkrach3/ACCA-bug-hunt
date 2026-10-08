import unittest


class TestBug4(unittest.TestCase):
    def test_normal_sentence(self):
        from words import count_words
        self.assertEqual(count_words("One two three"), 3)

    def test_double_spaces(self):
        from words import count_words
        self.assertEqual(count_words("Hello  world"), 2)

    def test_empty(self):
        from words import count_words
        self.assertEqual(count_words(""), 0)


if __name__ == "__main__":
    unittest.main()
