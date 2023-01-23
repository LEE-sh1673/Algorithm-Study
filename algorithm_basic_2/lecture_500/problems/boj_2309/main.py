"""
2309. 일곱 난쟁이
"""
from sys import stdin


def sol(A: list):
    total = sum(A)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if total - A[i] - A[j] == 100:
                for k in range(len(A)):
                    if i == k or j == k:
                        continue
                    print(A[k])
                return


sol(list(sorted(map(int, stdin.readlines()))))
