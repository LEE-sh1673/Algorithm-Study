"""
17087. 숨바꼭질 6 [84ms]
"""
from math import gcd
from sys import stdin

input = stdin.readline


N, S = map(int, input().rstrip().split())
A = [abs(el - S) for el in map(int, input().rstrip().split())]
print(gcd(*A))
