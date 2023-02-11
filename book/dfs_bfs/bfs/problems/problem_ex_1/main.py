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
visited = [[0] * N for _ in range(M)]
ans = 0


def bfs(i, j):
    visited[i][j] = True
    dirs = [(0, 1), (1, 0)]
    q = [(i, j)]

    while q:
        x, y = q.pop(0)

        for dir_x, dir_y in dirs:
            dx = x + dir_x
            dy = y + dir_y

            if 0 <= dx <= M - 1 and 0 <= dy <= N - 1:
                if graph[dx][dy] == 0 and not visited[dx][dy]:
                    visited[dx][dy] = True
                    q.append((dx, dy))


for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            ans += 1
            bfs(i, j)

print(ans)
