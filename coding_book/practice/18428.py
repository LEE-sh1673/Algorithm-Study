n = int(input())
graph = []
teacher = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append([i, j])

def obs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in teacher:
        for j in range(4):
            nx, ny = i

            while 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "O":
                    break

                if graph[nx][ny] == "S":
                    return False

                nx += dx[j]
                ny += dy[j]

    return True
