"""
14888. 연산자 끼워넣기
"""
from itertools import permutations
from sys import stdin


def cal(op1, op2, op):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    else:
        if op1 < 0:
            return abs(op1) // op2 * -1
        return op1 // op2


N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
operators = ['+', '-', '*', '//']

ops = []
for idx, val in enumerate(map(int, stdin.readline().split())):
    for _ in range(val):
        ops.append(operators[idx])

total = []
for op in permutations(ops, len(ops)):
    tmp = A[0]
    for i in range(len(op)):
        tmp = cal(tmp, A[i+1], op[i])
    total.append(tmp)

print(max(total))
print(min(total))
