"""
boj_9093. 단어 뒤집기

measured: 748ms
"""
import sys

input = sys.stdin.readline
stack = []


def pop_all():
    while stack:
        print(stack.pop(), end='')
    print(' ', end='')


for _ in range(int(input())):
    for ch in input().rstrip():
        if ch == ' ':
            pop_all()
        else:
            stack.append(ch)
    pop_all()
    print()
