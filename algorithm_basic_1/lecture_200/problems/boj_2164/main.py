from sys import stdin
from collections import deque


def sol(n: int) -> int:
    cards: deque = deque([i for i in range(1, n + 1)])

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())
    return cards.popleft()


print(sol(int(stdin.readline())))
