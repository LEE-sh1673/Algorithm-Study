"""
1로 만들기

이래를 순서대로 진행한다.

1. 5로 나눌 수 있을 때까지 계속 나눈다.
2. 3으로 나눌 수 있을 때까지 계속 나눈다.
3. 2로 나눌 수 있을 때까지 계속 나눈다.
4. 1을 뺀다.
"""
from sys import stdin

dp = {1: 0, 2: 1}


def sol_iterative(n) -> int:
    d = [0] * (n + 1)
    d[2] = 1

    for i in range(2, n + 1):
        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i // 2] + 1, d[i])
        if i % 3 == 0:
            d[i] = min(d[i // 3] + 1, d[i])
        if i % 5 == 0:
            d[i] = min(d[i // 5] + 1, d[i])
    return d[n]


def sol_recursive(n) -> int:
    if n in dp:
        return dp[n]

    elif n % 5 == 0:
        dp[n] = 1 + min(sol_recursive(n // 5), sol_recursive(n - 1))
    elif n % 3 == 0:
        dp[n] = 1 + min(sol_recursive(n // 3), sol_recursive(n - 1))
    elif n % 2 == 0:
        dp[n] = 1 + min(sol_recursive(n // 2), sol_recursive(n - 1))
    else:
        dp[n] = 1 + sol_recursive(n - 1)
    return dp[n]


print(sol_recursive(int(stdin.readline().strip())))
