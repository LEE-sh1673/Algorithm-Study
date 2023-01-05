"""
6588. 골든바흐의 추측
"""
from sys import stdin

N = 1000000
checked: list = [False] * (N + 1)
prime: list = [0] * N
pn = 0

for i in range(2, N+1):
    if not checked[i]:
        prime[pn] = i
        pn += 1
        for j in range(i * i, N + 1, i):
            checked[j] = True

while True:
    num: int = int(stdin.readline().rstrip())

    if num == 0:
        break

    for i in range(1, pn):
        if not checked[num - prime[i]]:
            print(f'{num} = {prime[i]} + {num-prime[i]}')
            break
