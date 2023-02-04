"""
11726. 2×money 타일링

구현 아이디어:
결국 문제에 대한 점화식의 형태가 D[money] = D[money-1] + D[money-2] 이므로,
이는 피보나치 수열과 동일하다. 따라서 Top-down 방식 대신 Bottom-up 방식으로 간단하게 구현할 수 있다.
"""
from sys import stdin


def sol(n: int) -> int:
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a % 10007


print(sol(int(stdin.readline())))
