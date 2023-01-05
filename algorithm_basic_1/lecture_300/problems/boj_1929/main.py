"""
1929. 소수 구하기
"""
from sys import stdin

M, N = map(int, stdin.readline().rstrip().split())
prime: list = [False] * (N + 1)
prime[2] = True

for i in range(3, N+1):
    prime[i] = i & 1

i = 3
while i * i <= N:
    if prime[i]:
        for j in range(i * i, N + 1, i << 1):
            prime[j] = False
    i += 2

for i in range(M, N + 1):
    if prime[i]:
        print(i)
