"""
프렌즈 4블록
https://school.programmers.co.kr/learn/courses/30/lessons/17679
"""


def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    spaces = set()

    def matchBlocks(i, j):
        return board[i][j] == board[i][j + 1] \
            and board[i][j] == board[i + 1][j] \
            and board[i][j] == board[i + 1][j + 1]

    def cleanUpBoard():
        nonlocal answer, spaces
        answer += len(spaces)
        for i, j in spaces:
            board[i][j] = []
        spaces.clear()

    def arrangeBoard():
        while True:
            arranged = True
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                        arranged = False
            if arranged:
                break

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == []:
                    continue

                if matchBlocks(i, j):
                    spaces.add((i, j))
                    spaces.add((i, j + 1))
                    spaces.add((i + 1, j))
                    spaces.add((i + 1, j + 1))

        if spaces:
            cleanUpBoard()
        else:
            return answer

        print('--before--')
        for k in range(m):
            for t in range(n):
                print(board[k][t], end=' ')
            print()
        print()

        arrangeBoard()
        print('--after')
        for k in range(m):
            for t in range(n):
                print(board[k][t], end=' ')
            print()
        print()
