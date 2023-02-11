from sys import stdin

N, M, K = map(int, stdin.readline().split())
nums = sorted(map(int, stdin.readline().split()), reverse=True)

cnt = (M//K) * K
a = nums[0] * cnt
b = nums[1] * (M - cnt)
print(a + b)
