"""
boj_9012. 괄호

measured: 44ms
"""
import sys


def is_valid_parens(parens) -> bool:
    cnt = 0
    for paren in parens:
        if paren == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break

    return cnt == 0


for _ in range(int(sys.stdin.readline())):
    if is_valid_parens(input()):
        print('YES')
    else:
        print('NO')
