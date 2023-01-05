"""
17298. 오큰수
"""
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def solution(n: int, seq: list) -> str:
    ans: list = [0] * n
    stk: list = [0]

    for i in range(1, n):
        if not stk:
            stk.append(i)

        while stk and seq[stk[-1]] < seq[i]:
            ans[stk.pop()] = seq[i]
        stk.append(i)

    while stk:
        ans[stk.pop()] = -1
    return ' '.join(map(str, ans))


N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
print(solution(N, A))
