"""
1929. 소수 구하기
"""
from sys import stdin

M, N = map(int, stdin.readline().rstrip().split())
prime = [False] + [True] * ((N - 1) // 2)

for x in range(1, int(N ** .5 / 2 + 1)):
    if prime[x]:
        prime[2 * x * (x + 1)::x * 2 + 1] = [False] * ((((N + 1) // 2) - x * x * 2) // (x * 2 + 1))
if M <= 2:
    print(2)

print('\n'.join([f'{x}' for x, val in zip(range(M + (M & 1 == 0), N + 1, 2), prime[M // 2:]) if val]))
