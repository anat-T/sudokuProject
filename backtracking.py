from board import *

''' Function for checking if a value n is valid for the cell in position (i,j)'''


def isValidCell(i, j, n):
    global board
    # checking row
    for t in range(0, 9):
        if board[i][t] == n:
            return False

    # checking column
    for t in range(0, 9):
        if board[t][j] == n:
            return False

    # checking square
    rowStart = (i//3)*3
    colStart = (j//3)*3
    for t in range(0, 3):
        for w in range(0, 3):
            if board[rowStart+t][colStart+w] == n:
                return False

    return True


''' Function for checking if all cells on a board are not empty'''


def isBoardComplete(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return False
    return True


'''The main function'''


def backtrackingSol(board):
    # global board
    while (not isBoardComplete(board)):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == 0:
                    for n in range(1, 10):
                        if isValidCell(i, j, n):
                            board[i][j] = n
                            oldBoard = board
                            backtrackingSol(board)
                            if oldBoard == board:
                                return board
                            board[i][j] = 0
