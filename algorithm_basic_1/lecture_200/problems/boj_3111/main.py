from sys import stdin


class CenzuraStack:
    def __init__(self, A: str):
        self.w = A
        self.x: list = [0] * 300001
        self.top: int = 0

    def add(self, item: int):
        self.x[self.top] = item
        self.top += 1

        if not self.censored():
            self.top -= len(self.w)
            return 1
        return 0

    def censored(self) -> bool:
        x, top, w = self.x, self.top, self.w
        n = len(w)
        censored: bool = True
        if top >= n:
            censored = any([x[top - i - 1] != w[i] for i in range(n)])
        return censored

    def pop(self):
        if not self.empty():
            item: int = self.x[self.top - 1]
            self.top -= 1
            return item
        return -1

    def empty(self):
        return self.top == 0

    def __str__(self):
        return f'A:{self.w}, x:{self.x[:self.top]}'


A, T = map(lambda s: s.rstrip(), stdin.readlines())
l_words = CenzuraStack(A[::-1])
r_words = CenzuraStack(A)

left: int = 0
right: int = len(T) - 1
turn: int = 0

while left <= right:
    if turn == 0:
        turn ^= l_words.add(T[left])
        left += 1
    else:
        turn ^= r_words.add(T[right])
        right -= 1

while not l_words.empty():
    r_words.add(l_words.pop())

while not r_words.empty():
    print(r_words.pop(), end='')
