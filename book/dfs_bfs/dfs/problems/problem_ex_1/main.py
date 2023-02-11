"""
1. 음료수 얼려 먹기

4 5
00110
00011
11111
00000
5 5

10100
11011
01001
00110
11111
"""
from sys import stdin

M, N = map(int, stdin.readline().split())
graph = [list(map(int, col.strip())) for col in stdin.readlines()]
ans = 0


def dfs(i, j):
    if 0 > i or i > M - 1 or 0 > j or j > N - 1:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i, j + 1)
        dfs(i+1, j)
        return True
    return False


for i in range(M):
    for j in range(N):
        if dfs(i, j):
            ans += 1

print(ans)
