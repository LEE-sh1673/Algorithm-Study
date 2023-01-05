from unittest import TestCase

from algorithm_basic_1.lecture_200.problems.boj_9012.main import is_valid_parens


class Test(TestCase):
    def test_is_valid_parens(self):
        self.assertEqual(is_valid_parens('()'), True)
        self.assertEqual(is_valid_parens('(())())'), False)
        self.assertEqual(is_valid_parens('(()())((()))'), False)
        self.assertEqual(is_valid_parens('((()()(()))(((())))()'), False)

