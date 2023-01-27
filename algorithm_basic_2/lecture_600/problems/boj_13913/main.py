"""
13913. 숨바꼭질 4
"""
from sys import stdin, setrecursionlimit
from collections import deque

MAX = 200000
setrecursionlimit(MAX)
visited = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)
via = [-1] * (MAX + 1)

n, k = map(int, stdin.readline().split())
visited[n] = True
dist[n] = 0
q = deque([n])

while q:
    v = q.popleft()
    for next_v in [v - 1, v + 1, v * 2]:
        if 0 <= next_v <= MAX and not visited[next_v]:
            visited[next_v] = True
            dist[next_v] = dist[v] + 1
            via[next_v] = v
            q.append(next_v)


def go(n, m):
    if n != m:
        go(n, via[m])
    print(m, end=' ')


print(dist[k])
go(n, k)
