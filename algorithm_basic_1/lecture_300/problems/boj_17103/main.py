"""
17103. 골드바흐 파티션
참고: https://pirateturtle.tistory.com/194

문제의 핵심은 골드바흐의 추측이 성립하는 경우를 어떻게 간추릴 것인가이다.
"""
from sys import stdin


def get_primes(size: int) -> list:
    primes: list = [True] * (size + 1)
    primes[0] = primes[1] = False

    for n in range(2, int(size ** 0.5) + 1):
        if primes[n]:
            for j in range(n * n, size + 1, n):
                primes[j] = False
    return primes


def solution(nums: list) -> None:
    is_prime = get_primes(1000000)

    for num in nums:
        cnt: int = 0
        for i in range(2, num // 2 + 1):
            if is_prime[i] and is_prime[num - i]:
                cnt += 1
        print(cnt)


solution(list(map(int, stdin.readlines()[1:])))
