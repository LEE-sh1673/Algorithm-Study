"""
boj_9012. 괄호

measured: 36ms
"""
import sys


def is_vps(ps) -> bool:
    if len(ps) % 2 != 0:
        return False

    while '()' in ps:
        ps = ps.replace('()', '')
    return not ps


for _ in range(int(sys.stdin.readline())):
    parens = sys.stdin.readline().rstrip()

    if is_vps(parens):
        print('YES')
    else:
        print('NO')
