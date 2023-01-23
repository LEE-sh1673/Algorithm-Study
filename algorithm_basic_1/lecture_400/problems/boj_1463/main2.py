"""
1463. 1로 만들기 [Bottom-up 방식 + Memoization]

D[N] = N을 1로 만드는 최소 연산 횟수
"""
from sys import stdin


def sol(n: int) -> int:
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
    return d[n]


print(sol(int(stdin.readline())))
