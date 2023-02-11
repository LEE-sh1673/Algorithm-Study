"""
18428. 감시 피하기
"""
from itertools import combinations
from sys import stdin

N = int(stdin.readline().rstrip())
graph = []
teachers = []
spaces = []

for i in range(N):
    graph.append(list(stdin.readline().rstrip().split()))

    for j in range(N):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'X':
            spaces.append((i, j))


def seek_student_by(x, y, direction):
    while True:
        x += direction[0]
        y += direction[1]

        # 경계 검사
        if 0 > x or x > N - 1 or 0 > y or y > N - 1:
            break

        # 장애물을 만날 경우
        if graph[x][y] == 'O' or graph[x][y] == 'T':
            break

        # 학생을 찾을 경우
        if graph[x][y] == 'S':
            return True

    return False


def seek_students():
    for x, y in teachers:
        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if seek_student_by(x, y, direction):
                return True
    return False


def sol():
    for obstacles in combinations(spaces, 3):
        # 장애물 배치
        for x, y in obstacles:
            graph[x][y] = 'O'

        # 검사 수행
        if not seek_students():
            return 'YES'

        # 맵 초기화
        for x, y in obstacles:
            graph[x][y] = 'X'

    return 'NO'


print(sol())
