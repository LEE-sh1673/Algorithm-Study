"""
왕실의 나이트
"""
from sys import stdin

knight_pos = stdin.readline().rstrip()
row = int(knight_pos[1])
column = int(ord(knight_pos[0]) - int(ord('a'))) + 1

# Knight가 이동할 수 있는 8가지 방향 정의
steps = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

ans = 0
for dx, dy in steps:
    next_row, next_column = row + dx, column + dy

    if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8:
        continue
    ans += 1

print(ans)
