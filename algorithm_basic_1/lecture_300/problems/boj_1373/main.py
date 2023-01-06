"""
1373. 2진수 8진수
"""
from sys import stdin

print(oct(int(stdin.readline().rstrip(), 2))[2:])
