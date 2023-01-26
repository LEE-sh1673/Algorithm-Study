"""
2085. 사탕 게임

# left_check
- row: compare A[i][0] ~ A[i][lcm]
- column:
	compare A[0][j] ~ A[lcm][j]
        compare A[0][j+1] ~ A[lcm][j+1]
"""
from sys import stdin


def check(A: list) -> int:
    n = len(A)
    ans = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):  # visited with i-row
            if A[i][j] == A[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

        cnt = 1
        for j in range(1, n):  # visited with i-column
            if A[j][i] == A[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    return ans


def left_check(A: list, i: int, j: int) -> int:
    n = len(A)
    ans = 1

    # visited with i-row
    cnt = 1
    for k in range(1, n):
        if A[i][k] == A[i][k - 1]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)

    # visited with j-column
    cnt = 1
    for k in range(1, n):
        if A[k][j] == A[k - 1][j]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)

    # visited with (j+1)-column
    if j + 1 < n:
        cnt = 1
        for k in range(1, n):
            if A[k][j + 1] == A[k - 1][j + 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
    return ans


def bottom_check(A: list, i: int, j: int) -> int:
    n = len(A)
    ans = 1

    # visited with i-row
    cnt = 1
    for k in range(1, n):
        if A[i][k] == A[i][k - 1]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)

    # visited with (i+1)-row
    if i + 1 < n:
        cnt = 1
        for k in range(1, n):
            if A[i + 1][k] == A[i + 1][k - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

    # visited with j-column
    cnt = 1
    for k in range(1, n):
        if A[k][j] == A[k - 1][j]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)

    return ans


def sol(N, A):
    ans = 0
    for i in range(N):
        for j in range(N):
            if j + 1 < N:  # compare with right-side
                A[i][j], A[i][j + 1] = A[i][j + 1], A[i][j]
                ans = max(ans, left_check(A, i, j))
                A[i][j], A[i][j + 1] = A[i][j + 1], A[i][j]

            if i + 1 < N:  # compare with bottom-side
                A[i][j], A[i + 1][j] = A[i + 1][j], A[i][j]
                ans = max(ans, bottom_check(A, i, j))
                A[i][j], A[i + 1][j] = A[i + 1][j], A[i][j]
    return ans


N = int(stdin.readline().rstrip())
A = list(map(lambda x: list(x.rstrip()), stdin.readlines()))
print(sol(N, A))
