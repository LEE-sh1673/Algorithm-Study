"""
2475. 검증수
"""
import sys


print(sum([int(number) ** 2 for number in sys.stdin.readline().split()]) % 10)
