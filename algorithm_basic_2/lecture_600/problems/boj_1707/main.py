"""
1707. 이분 그래프
"""
from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)
input = stdin.readline


def dfs(x, c):
    color[x] = c
    for v in g[x]:
        if color[v] == 0:
            dfs(v, 3 - c)


for _ in range(int(input().rstrip())):
    n, m = map(int, input().split())
    color = [0] * (n+1)
    g = [[] for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    for i in range(1, n + 1):
        if color[i] == 0:
            dfs(i, 1)

    ok = True
    for i in range(1, n + 1):
        for v in g[i]:
            if color[i] == color[v]:
                ok = False

    print("YES" if ok else "NO")
