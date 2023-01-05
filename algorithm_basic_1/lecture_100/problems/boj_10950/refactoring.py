"""
boj_10950. A+B - 3

Measured: 36ms
"""
import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
