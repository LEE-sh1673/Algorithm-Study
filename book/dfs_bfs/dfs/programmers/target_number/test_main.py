from unittest import TestCase

from book.dfs_bfs.dfs.programmers.target_number.main import solution, solution_bfs


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(5, solution([1, 1, 1, 1, 1], 3))
        self.assertEqual(2, solution([4, 1, 2, 1], 4))


class Test_BFS(TestCase):
    def test_solution_bfs(self):
        self.assertEqual(5, solution_bfs([1, 1, 1, 1, 1], 3))
        self.assertEqual(2, solution_bfs([4, 1, 2, 1], 4))
