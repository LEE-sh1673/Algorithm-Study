"""
DFS로 중복순열 만들기
"""
from itertools import combinations
n, r = map(int, input().split())
graph = list(map(int, input().split()))

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
    tmp = [0] * m

    def dfs(s, r):
        """
        :param r: nCr에서 r을 나타냄.
        :return:  조합을 리스트에 담아 반환
        """
        if s == m:
            ans.append(tuple(tmp))
        else:
            for i in range(r, len(n)):
                tmp[s] = n[i]
                dfs(s + 1, i + 1)

    dfs(0, 0)
    return ans


if __name__ == '__main__':
    pass

print(permute(graph, r))


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