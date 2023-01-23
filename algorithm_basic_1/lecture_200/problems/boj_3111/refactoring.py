from sys import stdin


def sol(A: list, T: list) -> str:
    rev_A = A[::-1]
    A_len = len(A)
    front, back = [], []
    left, right = 0, len(T) - 1
    flag = True

    while left <= right:
        if flag:
            front.append(T[left])
            left += 1
            if front[-A_len:] == A:
                front[-A_len:] = []
                flag = False
        else:
            back.append(T[right])
            right -= 1
            if back[-A_len:] == rev_A:
                back[-A_len:] = []
                flag = True

    while back:
        front.append(back.pop())
        if front[-A_len:] == A:
            front[-A_len:] = []

    return "".join(front)


A, T = map(lambda s: list(s.rstrip()), stdin.readlines())
print(sol(A, T))
