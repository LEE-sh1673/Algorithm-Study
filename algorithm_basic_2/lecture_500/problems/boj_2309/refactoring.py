from sys import stdin
from itertools import combinations


def sol(A: list):
    for comb in combinations(A, 7):
        if sum(comb) == 100:
            print('\n'.join(map(str, sorted(comb))))
            break


sol(list(sorted(map(int, stdin.readlines()))))
