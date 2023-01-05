"""
10845. 큐
"""
from sys import stdin

input = stdin.readline


def solution() -> None:
    queue: list = []

    for _ in range(int(input())):
        commands = input().rstrip().split()
        op = commands[0]
        arg = commands[-1]

        if op == 'push':
            queue.append(arg)
        elif op == 'pop':
            print(queue.pop(0) if queue else -1)
        elif op == 'size':
            print(len(queue))
        elif op == 'empty':
            print(0 if queue else 1)
        elif op == 'front':
            print(queue[0] if queue else -1)
        elif op == 'back':
            print(queue[-1] if queue else -1)


solution()
