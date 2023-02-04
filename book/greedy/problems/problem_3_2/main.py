"""
큰 수의 법칙

- 다양한 수로 이루어진 배열이 있을 때 주어진 수를 M번 더해서 가장 큰 수를 만드는 방법
- 이때 배열의 특정한 인덱스에 해당하는 수는 연속해서 K번을 초과하여 더할 수 없다.
- 서로 다른 인덱스의 수가 같은 경우에도 서로 다른 것으로 간주한다.

e.g. M = 8 / K = 3, N = [2, 4, 5, 4, 6]

=> 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46
"""
from sys import stdin

N, M, K = map(int, stdin.readline().split())
nums = [num for num in sorted(map(int, stdin.readline().split()), reverse=True)]
count = M // K * K
ans = count * nums[0]
ans += (M - count) * nums[1]
print(ans)
