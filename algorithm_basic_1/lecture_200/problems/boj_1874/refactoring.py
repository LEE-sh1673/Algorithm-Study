"""
1874. 스택 수열 [measured: 80ms]

- 스택에 push 되는 순서는 오름차 순.
- pop 되는 순서대로 수열이 만들어지기 때문에, A의 첫 수부터 순서 대로 만들어 보면 된다.
- m = 스택에 추가되어야 하는 수
- A[i] = 만들어야 하는 수열 A의 수
    - m < A[i]: A[i]를 pop해야 하기 때문에, m부터 A[i]까지의 모든 수를 순서대로 push해야 한다.
    - m > A[i]: 불가능한 경우, pop을 하면 A[i]가 아닌 다른 수가 A가 된다.
    - m == A[i]: pop을 해서 A[i]를 만들면 된다.

구현 아이디어:
- 스택에 push 되는 순서는 오름차 순임을 전제로 아래 로직을 수행: (처음 m = 1)
    - while (m <= A[i]):
        stack.push_all(m ~ A[i]) ; m += 1
    - if stack.peek() != A[i]:
        return 'NO'
    - stack.peek() == A[i]:
        stack.pop()
"""
import sys


def generate_char_sequence(seq) -> str:
    stk = []
    ans = []
    m = 1
    for num in seq:
        while m <= num:
            stk.append(m)
            ans.append('+')
            m += 1

        if stk.pop() != num:
            return 'NO'
        ans.append('-')
    return '\n'.join(ans)


sequence = [int(sys.stdin.readline()) for n in range(int(sys.stdin.readline()))]
print(generate_char_sequence(sequence))
