"""
1463. 1로 만들기 [Bottom-up 방식 + Memoization]
[해설: https://myjamong.tistory.com/301]

핵심로직:
d[i] = 1 + min(d[i/3] + (i/3일 때의 d[i-1]의 개수), d[i/2] + (i/3일 때의 d[i-1]의 개수))
"""
from sys import stdin

d = {1: 0, 2: 1}


def sol(n: int) -> int:
    if n in d:
        return d[n]
    t = 1 + min(sol(n // 3) + n % 3, sol(n // 2) + n % 2)
    d[n] = t
    return t


print(sol(int(stdin.readline())))
