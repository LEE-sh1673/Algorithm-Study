"""
1260. DFS와 BFS
"""
from sys import stdin
from collections import deque


n, m, v = map(int, stdin.readline().split())
check = [False] * (n + 1)
g: list = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n + 1):
    g[i].sort()


def dfs(x):
    check[x] = True
    print(x, end=' ')

    for gx_i in g[x]:
        if not check[gx_i]:
            dfs(gx_i)


def bfs(x):
    global g
    check = [False] * (n + 1)
    check[x] = True
    q = deque([x])

    while q:
        x_i = q.popleft()
        print(x_i, end=' ')

        for gx_i in g[x_i]:
            if not check[gx_i]:
                check[gx_i] = True
                q.append(gx_i)


dfs(v)
print()
bfs(v)
