"""
17413. 단어 뒤집기 2 [36ms]
"""
from sys import stdin

input = stdin.readline


def sol(seq: str) -> str:
    seq: list = seq.replace('>', '<').split('<')
    ans: str = ''

    for i in range(len(seq)):
        if i % 2 == 1:
            ans += f'<{seq[i]}>'
        else:
            ans += reverse_words(seq[i])
    return ans


def reverse_words(words: str) -> str:
    return ' '.join(word[::-1] for word in words.split())


print(sol(input().rstrip()))
