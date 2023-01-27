"""
1697. 숨바꼭질
"""
from sys import stdin
from collections import deque


def bfs(x):
    q = deque([x])
    limit = min(max, k + 1)
    acc[x] = 0
    while q:
        v = q.popleft()
        for next_v in [v - 1, v + 1, v * 2]:
            if 0 <= next_v <= limit and acc[v] + 1 < acc[next_v]:
                acc[next_v] = acc[v] + 1

                if next_v == k:
                    print(acc[next_v])
                    exit()
                q.append(next_v)


n, k = map(int, stdin.readline().split())

if n < k:
    max = 100000
    acc = [max] * (max + 1)
    bfs(n)
elif n > k:
    print(n - k)
else:
    print(0)
