n, r = map(int, input().split())
graph = list(map(int, input().split()))

def perm(arr, r):
    result = []

    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for j in perm(ans, r-1):
                result.append([arr[i]] + j)

    return result

print(perm(graph, r))