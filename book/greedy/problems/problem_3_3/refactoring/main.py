"""
3. 숫자 카드 게임
"""
from sys import stdin

N, M = map(int, stdin.readline().split())
ans = 0

for _ in range(N):
    ans = max(ans, min(*map(int, stdin.readline().split())))

print(ans)
