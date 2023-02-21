"""
가장 긴 증가하는 부분 수열 문제
(Long Increasing Sub Sequence, LIS)

어떠한 수열에 대해 오름차 순으로 정렬된 부분 수열들을 말한다.

E.g. 수열 { 3, 2, 5, 2, 3, 1, 4} 에서 LIS의 예시로는
{2, 3}, {2, 3, 4} 등을 들 수 있다.

점화식:
D[i] = 수열 arr에서 arr[i]의 원소를 마지막으로 하는 LIS의 길이

D[i] = max(D[i], D[j-1] + 1)
"""
from sys import stdin

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().strip().split()))
dp = [1] * n
dp[0] = 1

nums.reverse()

print(nums)

"""
문제 주의:
아마 문제에서 전투력이 높은 병사가 내림차 순으로 정렬되어야 하므로,
문제의 입력으로 부분적으로 입력된 전투력 수열이 들어온다.

따라서 이를 단순히 뒤집어 주어 LIS 문제로 만들고, 이때 LIS 길이 중 최대값에서
전체 길이를 빼면 내림차순으로 정렬되지 않은 요소의 개수, 즉 순서 상 열외시켜야 하는 병사의 수를 구할 수 있다.
    
[4, 2, 5, 8, 4, 11, 15]
1, 1, 2, 3, 2, 4, 5

[15 11 4 8 5 2 4]
"""

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)