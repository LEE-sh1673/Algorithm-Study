from sys import stdin

input = stdin.readline
limit: int = 100000
d = [0, 0, 0] * (limit + 1)

d[0] = [1, 0, 0]
d[1] = [1, 1, 0]
d[2] = [1, 1, 1]

for i in range(3, limit + 1):
    d[i] = [
        (d[i - 1][0]),
        (d[i - 2][0] + d[i - 2][1]),
        (d[i - 3][0] + d[i - 3][1] + d[i - 3][2])
    ]

for _ in range(int(input())):
    print(sum(d[int(input())-1]))
