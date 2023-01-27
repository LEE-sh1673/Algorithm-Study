"""
2178. 미로 탐색
"""
from sys import stdin
from collections import deque


def bfs(maze: list, directions: list, n: int, m: int):
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    q = deque()

    visited[0][0] = True
    dist[0][0] = 1
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist[n - 1][m - 1]


def main():
    n, m = map(int, stdin.readline().split())
    maze = [[int(x) for x in list(input().strip())] for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    print(bfs(maze, directions, n, m))


main()
