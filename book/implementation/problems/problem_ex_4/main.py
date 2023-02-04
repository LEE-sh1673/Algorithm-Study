"""
문자열 재정렬
"""
from sys import stdin

s = stdin.readline().rstrip()
alphabets = sorted(filter(lambda ch: not ch.isdigit(), s))
numbers = sum(map(int, filter(lambda ch: ch.isdigit(), s)))
print(''.join(alphabets) + str(numbers))
