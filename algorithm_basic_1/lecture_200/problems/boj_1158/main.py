"""
1158. 조세퍼스 문제 [2004ms]
"""
from collections import deque
from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())
queue = deque([i + 1 for i in range(n)])
ans = []

while queue:
    for _ in range(k):
        queue.append(queue.popleft())
    ans.append(queue.pop())

print(f"<{', '.join(map(str, ans))}>")
