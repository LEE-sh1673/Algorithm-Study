"""
boj_9093. 단어 뒤집기

measured: 88ms
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(' '.join(word[::-1] for word in input().rstrip().split()))
