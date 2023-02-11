"""
DFS로 중복순열 만들기
"""
from itertools import combinations


def permute(n, m):
    ans = []
    permutes = [0] * m

    def dfs(r):
        if r == m:
            ans.append(tuple(permutes))
        else:
            for num in n:
                permutes[r] = num
                dfs(r + 1)
    dfs(0)
    return ans


def combinate(n, m):
    ans = []
    combinates = [0] * m
    check = [0] * len(n)

    def dfs(r):
        """
        :param r: nCr에서 r을 나타냄.
        :return:  조합을 리스트에 담아 반환
        """
        if r == m:
            ans.append(tuple(combinates))
        else:
            for i in range(len(n)):
                if check[i]:
                    continue

                check[i] = 1
                combinates[r] = n[i]
                dfs(r + 1)
                check[i] = 0
    dfs(0)
    return ans


if __name__ == '__main__':
    pass


"""
중복 순열 - DFS (combinations, permutations, products)

> 입력:
3 -> N
2 -> M
1 2 3 -> [1, 2, 3]

> 출력:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3

"""
