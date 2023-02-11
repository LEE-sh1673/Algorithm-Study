"""
dfs 구현

ex.
8
1 2
1 3
1 8
2 1
2 7
3 1
3 4
3 5
4 3
4 5
5 3
5 4
6 7
7 2
7 6
7 8
8 1
8 7
"""
from sys import stdin

n = int(stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
nums = [map(int, vertex.split()) for vertex in stdin.readlines()]

for v1, v2 in nums:
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for x in graph[v]:
        if not visited[x]:
            dfs(x)


dfs(1)
