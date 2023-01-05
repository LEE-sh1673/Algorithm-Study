"""
17299. 오등큰수
"""
"""
17298. 오큰수
"""
from sys import stdin, stdout
from collections import Counter

input = stdin.readline
print = stdout.write


def solution(n: int, seq: list) -> str:
    ans: list = [0] * n
    stk: list = [0]
    freq = Counter(seq)

    for seq_i in seq:
        try:
            freq[seq_i] += 1
        except:
            freq[seq_i] = 0

    for i in range(1, n):
        if not stk:
            stk.append(i)

        while stk and freq.get(seq[stk[-1]]) < freq.get(seq[i]):
            ans[stk.pop()] = seq[i]
        stk.append(i)

    while stk:
        ans[stk.pop()] = -1
    return ' '.join(map(str, ans))


N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
print(solution(N, A))
