"""
효율적인 화폐 구성

상향식 구현 TIP
- 먼저 점화식 d[i]가 무엇을 의미하는지 정의한다.
- 최소한의 d[0]이 무슨 값이지를 정한다.
- 최소한의 주어진 값을 시작으로 다음 문제를 어떻게 계산할지 구상한다.
- 점화식을 완성한다.
- 구현한다.
"""
from sys import stdin


def sol(x: int) -> int:
    dp = [10001] * (x + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, x + 1):
            if dp[i - coin] != 10001:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[x] == 10001:
        return -1
    return dp[x]


def sol_implementation(x: int) -> int:
    cnt = 0

    for coin in sorted(coins, reverse=True):
        while x != 0:
            cnt += x // coin
            x %= coin

    if cnt == 0:
        return -1
    return cnt


n, m = map(int, stdin.readline().strip().split())
coins = list(map(int, stdin.readlines()))
print(sol(m))
