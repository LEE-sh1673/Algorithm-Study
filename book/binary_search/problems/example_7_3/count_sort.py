from sys import stdin

n = int(stdin.readline().rstrip())
arr = [0] * 1000001

for num in stdin.readline().split():
    arr[int(num)] = 1

m = int(stdin.readline().rstrip())
targets = list(map(int, stdin.readline().rstrip().split()))

for target in targets:
    if arr[target] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
