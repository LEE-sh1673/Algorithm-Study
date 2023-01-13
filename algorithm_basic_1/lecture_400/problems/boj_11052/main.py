"""
카드 구매하기 1 ~ 2 (11051 ~ 11052)
"""
from sys import stdin

input = stdin.readline


def sol(n: int, p: list) -> int:
    """
    11051 -> max()
    11052 -> min()
    """
    d: list = [0] + p
    for i in range(2, n + 1):
        d[i] = min([a + b for a, b in zip(d[:i // 2 + 1], d[i:(i - 1) // 2:-1])])
    return d[n]


N = int(input())
P = list(map(int, input().rstrip().split()))
print(sol(N, P))

# if i = 2
# d[0], d[1] -> d[0:2]
# d[2], d[1] -> d[2:0:-1]

# if i = 3
# d[0], d[1] -> d[0:2]
# d[3], d[2] -> d[3:1:-1]

# if i = 4
# d[0], d[1], d[2] -> d[0:3]
# d[4], d[3], d[2] -> d[4:1:-1]

# d[0:2], d[0:2], d[0:3] ... -> d[:i//2+1]
# d[2:0:-1], d[3:1:-1], d[4:1:-1], ... -> d[i:(i-1)//2:-1]
