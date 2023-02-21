
def binary_search(arr, target, start, end):
    while start <= end:
        height = start + (end - start) // 2
        total = sum([num for num in map(lambda x: x - height, arr) if num > 0])

        if total == target:
            return height
        elif total > target:
            start = height + 1
        else:
            end = height - 1
    return None



n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(arr, m, 0, max(arr)))
