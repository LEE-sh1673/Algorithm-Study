"""
1707. 이분 그래프
"""
from sys import stdin, exit


def is_bipartite(nodes, graph, colors) -> bool:
    stack = []
    for node in range(nodes):
        if colors[node] == 0:
            colors[node] = 1
            stack.append(node)

        while stack:
            u = stack.pop()

            for v in graph[u]:
                if colors[v] == 0:
                    colors[v] = 3 - colors[u]
                    stack.append(v)
                elif colors[v] == colors[u]:
                    return False
    return True


def main() -> None:
    input = stdin.readline

    for _ in range(int(input().rstrip())):
        nodes, edges = map(int, input().split())
        graph = [[] for _ in range(nodes + 1)]
        colors = [0] * (nodes + 1)

        for _ in range(edges):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        print("YES" if is_bipartite(nodes, graph, colors) else "NO")


if __name__ == "__main__":
    exit(main())
