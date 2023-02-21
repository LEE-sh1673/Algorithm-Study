"""
개미 전사

점화식:
d[i] = i번째 식량 창고까지의 최적의 해 (얻을 수 있는 식량의 최대값)
ar[i] = i번째 식량창고에 있는 식량의 양

d[i] = max(d[i-1], d[i-2] + ar[i])
"""
from sys import stdin

N = int(stdin.readline().strip())
foods = list(map(int, stdin.readline().strip().split()))
d = [0] * 100
d[0] = foods[0]
d[1] = max(foods[0], foods[1])

for i in range(2, len(foods)):
    d[i] = max(d[i-1], d[i-2] + foods[i])

print(d[N-1])
