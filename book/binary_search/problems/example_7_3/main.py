from sys import stdin

n = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().rstrip().split()))
nums.sort()
m = int(stdin.readline().rstrip())
targets = list(map(int, stdin.readline().rstrip().split()))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


for target in targets:
    if binary_search(nums, target, 0, n - 1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
