from backtracking import *

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def algorithm():
    oldBoard = board
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if isValidCell(i, j, n):
                        board[i][j] = n
                        algorithm()
                        board[i][j] = 0
                return
    if oldBoard == board:
        return
