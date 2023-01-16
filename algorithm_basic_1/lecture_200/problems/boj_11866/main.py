from sys import stdin


def sol(n: int, k: int) -> str:
    que: list = [i for i in range(1, n+1)]
    pos: int = 0
    ans: list = []

    for _ in range(n):
        pos = (pos + (k-1)) % len(que)
        ans.append(que.pop(pos))

    return f"<{', '.join(map(str, ans))}>"


N, K = map(int, stdin.readline().rstrip().split())
print(sol(N, K))

