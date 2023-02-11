"""
14888. 연산자 끼워넣기
"""
from sys import stdin


def dfs(r, index, add, sub, mul, div):
    if index == len(A):
        total.append(r)
        return

    if add:
        dfs(r + A[index], index + 1, add - 1, sub, mul, div)

    if sub:
        dfs(r - A[index], index + 1, add, sub - 1, mul, div)

    if mul:
        dfs(r * A[index], index + 1, add, sub, mul - 1, div)

    if div:
        if r < 0:
            dfs(abs(r) // A[index] * (-1), index + 1, add, sub, mul, div - 1)
        else:
            dfs(r // A[index], index + 1, add, sub, mul, div - 1)


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
ops = list(map(int, stdin.readline().split()))
total = []
dfs(A[0], 1, ops[0], ops[1], ops[2], ops[3])
print(max(total))
print(min(total))
