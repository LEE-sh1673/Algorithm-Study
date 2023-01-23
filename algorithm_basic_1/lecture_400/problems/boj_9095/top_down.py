"""
9095. 1, 2, 3 더하기 [top-down]
"""
from sys import stdin

d = {0: 1, 1: 1}


def sub(n: int) -> int:
    if n < 0:
        return 0
    elif n in d:
        return d[n]
    else:
        d[n] = sub(n - 1) + sub(n - 2) + sub(n - 3)
        return d[n]


def sol(nums) -> list:
    return [sub(num) for num in nums]


print('\n'.join(map(str, sol(map(int, stdin.readlines()[1:])))))
