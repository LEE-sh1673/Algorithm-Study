"""
10866. 덱
"""
from sys import stdin

input = stdin.readline


def solution() -> None:
    deque: list = []

    for _ in range(int(input())):
        commands = input().rstrip().split()
        op = commands[0]
        arg = commands[-1]

        if op == 'push_front':
            deque.insert(0, arg)
        elif op == 'push_back':
            deque.append(arg)
        elif op == 'pop_front':
            print(deque.pop(0) if deque else -1)
        elif op == 'pop_back':
            print(deque.pop() if deque else -1)
        elif op == 'size':
            print(len(deque))
        elif op == 'empty':
            print(0 if deque else 1)
        elif op == 'front':
            print(deque[0] if deque else -1)
        elif op == 'back':
            print(deque[-1] if deque else -1)


solution()
