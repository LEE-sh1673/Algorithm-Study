from unittest import TestCase

from book.dfs_bfs.dfs.programmers.friends4blocks.main import solution


# class Test(TestCase):
#     def test_find_all_matching_blocks(self):
#         self.assertEqual(2, findAllMatchingBlocks(
#             1, 0,
#             6, 6,
#             ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
#         ))
#         self.assertEqual(1, findAllMatchingBlocks(
#             1, 4,
#             6, 6,
#             ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
#         ))
#         self.assertEqual(2, findAllMatchingBlocks(
#             1, 0,
#             4, 5,
#             ["CCBDE", "AAADE", "AAABF", "CCBBF"]
#         ))


class TestSolution(TestCase):
    def test_solution(self):
        self.assertEqual(14, solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
        self.assertEqual(15, solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

