"""
18428. 감시 피하기
"""
from sys import stdin


def dfs(r):
    x, y = r
    visited[x][y] = True

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        row = x + dx
        col = y + dy

        if row < 0 or row > N-1 or col < 0 or col > N-1:
            continue






N = int(stdin.readline().rstrip())
graph = [line.rstrip().split() for line in stdin.readlines()]
visited = [[False] * N for _ in range(N)]
isSecure = True
numsMark = 3
dfs((0, 0))

for k1 in range(N):
    for k2 in range(N):
        print(graph[k1][k2], end=' ')
    print()
print()

if isSecure:
    print("YES")
else:
    print("NO")
