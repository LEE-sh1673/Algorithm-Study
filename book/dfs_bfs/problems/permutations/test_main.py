from unittest import TestCase

from book.dfs_bfs.problems.permutations.main import permute, combinate


class Test(TestCase):
    def test_permute(self):
        self.assertEqual(
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
            permute([1, 2, 3], 2)
        )
        self.assertEqual(
            [(3, 3), (3, 6), (3, 9), (6, 3), (6, 6), (6, 9), (9, 3), (9, 6), (9, 9)],
            permute([3, 6, 9], 2)
        )
        self.assertEqual(
            [(3, 3, 3), (3, 3, 6), (3, 3, 9),
             (3, 6, 3), (3, 6, 6), (3, 6, 9),
             (3, 9, 3), (3, 9, 6), (3, 9, 9),
             (6, 3, 3), (6, 3, 6), (6, 3, 9),
             (6, 6, 3), (6, 6, 6), (6, 6, 9),
             (6, 9, 3), (6, 9, 6), (6, 9, 9),
             (9, 3, 3), (9, 3, 6), (9, 3, 9),
             (9, 6, 3), (9, 6, 6), (9, 6, 9),
             (9, 9, 3), (9, 9, 6), (9, 9, 9)],
            permute([3, 6, 9], 3)
        )


class Test(TestCase):
    def test_combinate(self):
        self.assertEqual(
            [(3, 6), (3, 9), (6, 9)],
            combinate([3, 6, 9], 2)
        )
