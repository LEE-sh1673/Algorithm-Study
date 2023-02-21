from sys import stdin


def sol(n: int) -> int:
    if n in dp:
        return dp[n]
    elif (n % 3 == 0) and (n % 2 == 0):
        dp[n] = min(sol(n // 3) + 1, sol(n // 2) + 1)
    elif n % 2 == 0:
        dp[n] = min(sol(n // 2) + 1, sol(n - 1) + 1)
    elif n % 3 == 0:
        dp[n] = min(sol(n // 3) + 1, sol(n - 1) + 1)
    else:
        dp[n] = 1 + sol(n - 1)
    return dp[n]


n = int(stdin.readline().strip())
dp = {1: 0, 2: 1}
print(sol(n))
