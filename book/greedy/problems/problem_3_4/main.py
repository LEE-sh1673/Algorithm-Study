"""
1로 만들기
"""
n, k = map(int, input().split())
ans: int = 0

while True:
    target = (n // k) * k
    ans += (n - target)
    n = target

    if n < k:  # 더 이상 나눌 수 없을 때
        break

    ans += 1  # K로 나누기
    n //= k

# 마지막으로 남은 수에 대해 1씩 빼기
ans += (n - 1)
print(ans)
