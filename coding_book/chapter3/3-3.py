n, m = map(int, input().split())
data = []
min_list = []

for i in range(n):
    data.append(input().split())
    min_list.append(min(data[i]))

print(max(min_list))
