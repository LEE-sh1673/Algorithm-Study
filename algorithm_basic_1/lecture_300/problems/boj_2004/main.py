"""
2004. 조합 0의 개수
해설: https://st-lab.tistory.com/166
"""
from sys import stdin


def get_digit_power(digit: int, number: int) -> int:
    count: int = 0

    while number != 0:
        number = number // digit
        count += number
    return count


def solution(n: int, m: int) -> int:
    two_count = get_digit_power(2, n) - get_digit_power(2, n - m) - get_digit_power(2, m)
    five_count = get_digit_power(5, n) - get_digit_power(5, n - m) - get_digit_power(5, m)
    return min(two_count, five_count)


N, M = map(int, stdin.readline().rstrip().split())
print(solution(N, M))
