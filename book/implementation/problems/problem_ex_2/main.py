"""
시각
"""
from sys import stdin

ans = 0
for h in range(int(stdin.readline().rstrip()) + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                ans += 1

print(ans)
