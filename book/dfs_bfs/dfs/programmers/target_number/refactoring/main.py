"""
타겟 넘버
"""


def sol(number, target):
    if not number and target == 0:
        return 1
    elif not number:
        return 0
    else:
        return sol(number[1:], target - number[0]) + sol(number[1:], target + number[0])
록