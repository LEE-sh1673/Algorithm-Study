"""
13023.ABCDE

간선 리스트, 간접 행렬, 인접 리스트로 구현.
"""
from sys import stdin


def sol(m: int) -> int:
    edges: list = []  # 간선 리스트
    a: list = [[False] * 2000 for i in range(2000)]  # 인접 행렬
    g: list = [[] for i in range(2000)]  # 인접 리스트

    for _ in range(m):
        start, end = map(int, stdin.readline().split())
        edges.append((start, end))
        edges.append((end, start))
        a[start][end] = a[end][start] = True
        g[start].append(end)
        g[end].append(start)

    m *= 2  # 친구 관계는 그래프에서 양방향 그래프로 표현되기 때문에 2배로 계산
    for i in range(m):
        for j in range(m):
            # A -> B
            A, B = edges[i]

            # C-> D
            C, D = edges[j]

            if A == B or A == C or A == D or B == C or B == D or C == D:
                continue

            # B -> C
            if not a[B][C]:
                continue

            # D -> E
            for E in g[D]:
                if A == E or B == E or C == E or D == E:
                    continue
                return 1
    return 0


_, m = map(int, stdin.readline().split())
print(sol(m))
