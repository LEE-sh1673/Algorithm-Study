from unittest import TestCase

from book.dfs_bfs.dfs.programmers.target_number.refactoring.main import sol


class Test(TestCase):
    def test_sol(self):
        self.assertEqual(5, sol([1, 1, 1, 1, 1], 3))
        self.assertEqual(2, sol([4, 1, 2, 1], 4))
