def prime(n):
    if n < 2:
        return False

    for i in range (2, n):
        if n % i == 0:
            return False

    return True

n = int(input())
num_list = list(map(int, input().split()))
sum = 0

for i in num_list:
    if prime(i):
        sum += 1

print(sum)











