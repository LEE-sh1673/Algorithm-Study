"""
9613. GCD 합
"""
from sys import stdin
from itertools import combinations

input = stdin.readline


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    N = list(map(int, input().rstrip().split()[1:]))
    print(sum([gcd(a, b) for a, b in combinations(N, 2)]))
