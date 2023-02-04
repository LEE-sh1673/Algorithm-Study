"""
곱하기 혹은 더하기
"""
s = input()
ans = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])

    if num <= 1 or ans <= 1:
        ans += num
    else:
        ans *= num

print(ans)
