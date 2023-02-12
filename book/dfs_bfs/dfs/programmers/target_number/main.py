"""
타겟 넘버
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""


def solution(numbers: list, target: int):
    answer = 0

    def dfs(r, index):
        if index == len(numbers):
            if r == target:
                nonlocal answer
                answer += 1
        else:
            dfs(r + numbers[index], index + 1)
            dfs(r - numbers[index], index + 1)

    dfs(0, 0)
    return answer


def solution_bfs(numbers: list, target: int):
    answer: int = 0
    que = [(numbers[0], 0), (-1 * numbers[0], 0)]
    n: int = len(numbers)

    while que:
        value, idx = que.pop(0)
        idx += 1

        if idx < n:
            que.append((value + numbers[idx], idx))
            que.append((value - numbers[idx], idx))
        else:
            if value == target:
                answer += 1

        print(que)

    return answer
