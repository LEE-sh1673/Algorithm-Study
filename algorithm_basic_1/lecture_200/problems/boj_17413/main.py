"""
17413. 단어 뒤집기 2 [52ms]
"""
from sys import stdin

input = stdin.readline


def sol(seq: str) -> str:
    is_tag: bool = False
    stk: list = []
    ans: list = []

    for ch in seq:
        if ch == '<':
            while stk:
                ans.append(stk.pop())
            is_tag = True
            ans.append(ch)
        elif ch == '>':
            is_tag = False
            ans.append(ch)
        elif is_tag:
            ans.append(ch)
        else:
            if ch == ' ':
                while stk:
                    ans.append(stk.pop())
                ans.append(ch)
            else:
                stk.append(ch)
    while stk:
        ans.append(stk.pop())
    return ''.join(ans)


print(sol(input().rstrip()))
