"""
1406. 에디터

- 커서: 문장의 맨 앞, 맨 뒤, 문장 중간 중간 임의의 곳에 위치할 수 있다.
- 명령어:
    - L: 커서를 왼쪽으로 한 칸 옮김. (커서가 문장의 맨 앞이면 무시)
    - D: 커서를 오른쪽으로 한 칸 옮김. (커서가 문장의 맨 뒤이면 무시)
    - B: 커서 왼쪽에 있는 문자를 삭제함. (커서가 문장의 맨 앞이면 무시)
    - P $: $라는 문자를 커서의 왼쪽에 추가함.
- 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있음.

구현 아이디어:
- 이 문제는 '스택' 또는 '연결 리스트'로 구현할 수 있다.
- 스택의 경우 다음을 따른다.
    - 커서를 기준으로 존재하는 각 문자열을 두 개의 스택에 담는다.
    - 이후 명령어에 따라 다음을 수행한다.
        - L -> right_stack.push(left_stack.pop())
        - D -> left_stack.push(right_stack.pop())
        - B -> left_stack.pop()
        - P $ -> left_stack.push($)

시간 복잡도:
스택을 이용하면 명령어 하나를 수행하는데 O(1) 시간이 소요되므로, 명령어의 개수를 M개라고 하면 시간 복잡도는 O(M)이 된다.
"""
from sys import stdin

input = stdin.readline

left_seq = list(input().rstrip())
right_seq = []

for _ in range(int(input())):
    commands = input()

    if commands[0] == 'L':
        if left_seq:
            right_seq.append(left_seq.pop())
    elif commands[0] == 'D':
        if right_seq:
            left_seq.append(right_seq.pop())
    elif commands[0] == 'B':
        if left_seq:
            left_seq.pop()
    elif commands[0] == 'P':
        left_seq.append(commands[2])

right_seq.reverse()
print(''.join(left_seq+right_seq))
