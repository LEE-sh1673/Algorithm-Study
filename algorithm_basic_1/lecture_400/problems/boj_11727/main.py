"""
11727. 2×coins 타일링 2
"""
from sys import stdin


def sol(n: int) -> int:
    a = b = 1
    for _ in range(n):
        a, b = b, 2*a + b
    return a % 10007


print(sol(int(stdin.readline())))
