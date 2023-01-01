from unittest import TestCase

from test.count_word import count_words


class Test(TestCase):
    def test_count_words(self):
        words = "1,2,3,4,5"
        expected = 5
        self.assertEqual(count_words(words), expected)
        self.assertEqual(count_words("1,2,3"), 3)
