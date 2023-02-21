from sys import stdin

n = int(stdin.readline().rstrip())
arr = set(map(int, stdin.readline().split()))

m = int(stdin.readline().rstrip())
targets = list(map(int, stdin.readline().rstrip().split()))

for target in targets:
    if target in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')
