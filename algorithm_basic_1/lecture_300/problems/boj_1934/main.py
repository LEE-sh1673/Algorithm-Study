"""
1934. 최소공배수
"""
from sys import stdin

input = stdin.readline


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


for _ in range(int(input())):
    t1, t2 = map(int, input().strip().split())
    print(lcm(t1, t2))
