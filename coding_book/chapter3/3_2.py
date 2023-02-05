N, M, K = map(int, input().split())
data = list(map(int, input().split()))
def max(a):
    largest = a[0]
    for i in a:
        if i > largest:
            largest = i
    return largest

def max_2(a):
    second = largest = -float('inf')

    for i in a:
        if i > largest:
            second = largest
            largest = i
        elif second < i < largest:
            second = i
    return second

def max_num(a):
    def max(a):
        largest = a[0]
        for i in a:
            if i > largest:
                largest = i
        return largest
    sum = 0
    for i in a:
        if i == max(a):
            sum += 1
    return sum

if max_num(data) == 1:
    print(max(data) * ((M % K) * K) + max_2(data) * (M - ((M % K) * K)))
else:
    print(max(data) * M)

