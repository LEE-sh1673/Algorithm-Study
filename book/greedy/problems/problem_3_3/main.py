"""
3. 숫자 카드 게임
"""
from sys import stdin

N, M = map(int, stdin.readline().split())
nums = [sorted(map(int, stdin.readline().split())) for _ in range(N)]
print(max([num[0] for num in nums]))
