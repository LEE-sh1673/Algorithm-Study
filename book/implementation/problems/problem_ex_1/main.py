"""
상하좌우

N * N

+-------+-------+------+-------+
| (1,1) | (1,2) | .... | (1,N) |
+----------------------+-------+
| (2,1) | (2,2) | .... | (2,N) |
+-------+-------+------+-------+
| ....  | ....  | .... | .... |
+-------+------+-------+------+
| .... | ....  | .... | (N,N) |
+-----+--------+-----+--------+

L: 왼쪽 한칸 이동
R: 오른쪽 한칸 이동
U: 위로 한칸 이동
D: 아래로 한칸 이동
"""
from sys import stdin

N = int(stdin.readline().rstrip())
plans = stdin.readline().split()

# L, U, R, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1

for plan in plans:
    nx, ny = x, y
    for i in range(len(move_types)):
        if move_types[i] == plan:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny

print(x, y)
