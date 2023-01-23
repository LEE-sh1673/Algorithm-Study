"""
1463. 1로 만들기 [Top-down 방식 + Memoization -> 메모리 초과]

D[lcm] = N을 1로 만드는 최소 연산 횟수
"""
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6 + 2)
N = int(stdin.readline())
d = [0] * (N + 1)


def sol(n: int) -> int:
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]

    d[n] = sol(n - 1) + 1

    if n % 2 == 0:
        d[n] = min(d[n], sol(n // 2) + 1)

    if n % 3 == 0:
        d[n] = min(d[n], sol(n // 3) + 1)

    return d[n]


print(sol(N))
