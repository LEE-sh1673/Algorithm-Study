"""
1541. 잃어버린 괄호
"""
from functools import reduce
from sys import stdin
from re import split


s = stdin.readline().strip()
nums = [sum(map(int, s_i.split('+'))) for s_i in split('-', s)]
print(reduce(lambda x, y: x - y, nums))
