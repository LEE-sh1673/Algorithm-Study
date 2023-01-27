"""
11724. 연결 요소의 개수
"""
from sys import stdin, setrecursionlimit

setrecursionlimit(100000)
n, m = map(int, stdin.readline().split())
g = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
components = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    g[a].append(b)
    g[b].append(a)


def dfs(x):
    visited[x] = True
    for v in g[x]:
        if not visited[v]:
            dfs(v)


for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        components += 1

print(components)
