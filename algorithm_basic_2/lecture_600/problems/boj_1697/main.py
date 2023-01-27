"""
1697. 숨바꼭질
"""
from sys import stdin
from collections import deque

MAX = 200000
visited = [False] * (MAX + 1)
dist = [-1] * (MAX + 1)

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
            q.append(next_v)

print(dist[k])
