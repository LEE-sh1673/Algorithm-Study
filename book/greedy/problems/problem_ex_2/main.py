"""
문제 조건
"""
n = int(input())
risks = list(map(int, input().split()))
risks.sort()

groups: int = 0  # 총 그룹의 수
nums_adventurer: int = 0  # 현재 그룹에 포함된 모험가의 수

for risk in risks:
    nums_adventurer += 1

    if nums_adventurer >= risk:
        groups += 1
        nums_adventurer = 0

print(groups)
