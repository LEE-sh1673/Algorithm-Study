"""
11726. 2×n 타일링
"""
from sys import stdin


d = {1: 1, 2: 2}


def sol(n: int) -> int:
    if n in d:
        return d[n]
    else:
        d[n] = sol(n - 1) + sol(n - 2)
        return d[n]


print(sol(int(stdin.readline())) % 10007)
