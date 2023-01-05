"""
1158. 조세퍼스 문제 [40ms]
"""
from sys import stdin

input = stdin.readline

n, k = map(int, input().rstrip().split())
queue = [i + 1 for i in range(n)]
ans = []
pos = 0

for _ in range(n):
    pos = (pos + k-1) % len(queue)
    ans.append(str(queue.pop(pos)))

print(f"<{', '.join(map(str, ans))}>")
