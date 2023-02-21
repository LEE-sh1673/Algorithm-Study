"""
금광 문제

2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
from sys import stdin


def sol_iterative() -> int:
    """
    상향식 방법의 경우
    dp 테이블에 미리 금광의 정보를 저장해두고
    금광의 끝에서부터 순서대로 최적의 값을 계산해나가는 방식이다.
    """
    dt = []
    for i in range(n):
        dt.append(golds[i][:m])

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dt[i - 1][j - 1]

            if i == n - 1:
                left_down = 0
            else:
                left_down = dt[i + 1][j - 1]

            left = dt[i][j - 1]
            dt[i][j] = dt[i][j] + max(left_up, left_down, left)
    ans = 0
    for i in range(n):
        ans = max(ans, dt[i][m - 1])
    return ans


def sol(i: int, j: int) -> int:
    if j < 0 or j > m - 1 or i < 0 or i > n - 1:
        return 0

    if dp[i][j] != 0:
        return dp[i][j]

    dp[i][j] = golds[i][j] + max(
        sol(i - 1, j + 1),
        sol(i, j + 1),
        sol(i + 1, j + 1)
    )
    return dp[i][j]


#
# def sol(i: int, j: int) -> int:
#     if j == m - 1:
#         return golds[i][j]
#     else:
#         if dp[i][j] != 0:
#             return dp[i][j]
#         elif 0 < i < n - 1:
#             dp[i][j] = max(
#                 golds[i][j] + sol(i - 1, j + 1),
#                 golds[i][j] + sol(i, j + 1),
#                 golds[i][j] + sol(i + 1, j + 1)
#             )
#         elif i < n - 1:
#             dp[i][j] = max(
#                 golds[i][j] + sol(i + 1, j + 1),
#                 golds[i][j] + sol(i, j + 1)
#             )
#         elif i > 0:
#             dp[i][j] = max(
#                 golds[i][j] + sol(i - 1, j + 1),
#                 golds[i][j] + sol(i, j + 1)
#             )
#     return dp[i][j]


for _ in range(int(stdin.readline().strip())):
    n, m = map(int, stdin.readline().strip().split())
    golds = [[0] * m for _ in range(n)]
    dp = [[0] * m for _ in range(n)]

    for idx, val in enumerate(map(int, stdin.readline().strip().split())):
        golds[idx // m][idx % m] = val
    print(sol_iterative())
    #
    # ans = 0
    # for i in range(len(golds)):
    #     ans = max(ans, sol(i, 0))
    # print(ans)
