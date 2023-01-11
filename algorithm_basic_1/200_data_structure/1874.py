import sys
n = int(input())
a = [int(input()) for _ in range(n)]
stack = []
m = 0 #스택에 들어간 마지막 수!
ans = ''

for x in a:
    if x > m:
        while x > m:
            m += 1
            stack.append(m)
            ans += '+\n'
        stack.pop()
        ans += '-\n'

    else:
        if stack[-1] != x:
            print('No')
            sys.exit(0)
        stack.pop()
        ans += '-\n'
print(ans, end='')