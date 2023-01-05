"""
10828. 스택
"""
from sys import stdin

input = stdin.readline

s: list = []

for _ in range(int(input())):
    commands = input().rstrip().split()
    op = commands[0]
    arg = commands[-1]

    if op == 'push':
        s.append(arg)
    elif op == 'pop':
        print(s.pop() if s else -1)
    elif op == 'size':
        print(len(s))
    elif op == 'empty':
        print(0 if s else 1)
    elif op == 'top':
        print(s[-1] if s else -1)
