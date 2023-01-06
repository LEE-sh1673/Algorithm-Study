"""
17087. 숨바꼭질 6 [132ms]
"""
from functools import reduce
from sys import stdin

input = stdin.readline


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


N, S = map(int, input().rstrip().split())
A = [abs(el - S) for el in map(int, input().rstrip().split())]
print(reduce(gcd, A))
