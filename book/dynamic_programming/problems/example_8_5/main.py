"""
병사 배치하기

가장 긴 부분 수열(lls)를 응용하여 풀 수 있다.
"""
from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))
arr.reverse()

# dp 테이블 초기화 (dp[n] = arr[i]를 마지막 원소로 가지는 부분 수열의 쵀대 길이
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        # 가장 긴 증가하는 부분 수열(lls) 알고리즘 사용
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외 시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))
