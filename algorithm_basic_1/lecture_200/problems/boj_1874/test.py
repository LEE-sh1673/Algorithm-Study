from sys import stdin


def sol(nums: list) -> str:
    curr: int = 0
    stk: list = []
    ans: list = []

    for num in nums:
        if curr < num:
            while curr < num:
                stk.append(curr + 1)
                curr += 1
                ans.append('+')
            ans.append('-')
            stk.pop()
        else:
            if stk.pop() != num:
                return 'NO'
            else:
                ans.append('-')
    return '\n'.join(ans)


nums: list = list(map(int, stdin.readlines()[1:]))
print(sol(nums))

