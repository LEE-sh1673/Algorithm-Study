from sys import stdin

d = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def sol(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return sol(20, 20, 20)
    elif d[a][b][c]:
        return d[a][b][c]
    elif a < b < c:
        d[a][b][c] = sol(a, b, c - 1) + sol(a, b - 1, c - 1) - sol(a, b - 1, c)
        return d[a][b][c]
    else:
        d[a][b][c] = sol(a - 1, b, c) + sol(a - 1, b - 1, c) \
                     + sol(a - 1, b, c - 1) - sol(a - 1, b - 1, c - 1)
        return d[a][b][c]


for num in stdin.readlines():
    a, b, c = map(int, num.rstrip().split())

    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {sol(a, b, c)}')
