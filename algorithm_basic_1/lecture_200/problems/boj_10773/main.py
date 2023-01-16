from sys import stdin


def sol(nums: list) -> int:
    stk: list = []

    for num in nums:
        if num == 0:
            stk.pop()
        else:
            stk.append(num)

    return sum(stk)


print(sol(list(map(int, stdin.readlines()[1:]))))
