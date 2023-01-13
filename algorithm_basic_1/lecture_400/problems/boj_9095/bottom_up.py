"""
9095. 1, 2, 3 더하기 [top-down]
"""
from sys import stdin


def sub(n: int) -> int:
    a = b = 0
    c = 1
    for _ in range(n):
        a, b, c = b, c, a + b + c
    return c


def sol(nums) -> list:
    return [sub(num) for num in nums]


print('\n'.join(map(str, sol(map(int, stdin.readlines()[1:])))))
