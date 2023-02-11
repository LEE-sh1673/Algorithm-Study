"""
bfs 구현

ex.
8
1 2
1 3
1 8
2 7
3 4
3 5
4 5
6 7
7 8
"""
from sys import stdin

n = int(stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
nums = [map(int, vertex.split()) for vertex in stdin.readlines()]

for v1, v2 in nums:
    graph[v1].append(v2)
    graph[v2].append(v1)


def bfs(x):
    q = [x]
    visited[x] = True

    while q:
        qx = q.pop(0)
        print(qx, end=' ')

        for v in graph[qx]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


bfs(1)
