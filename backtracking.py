
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
    for t in range(i-1, i+2):
        for w in range(j-1, j+2):
            if board[t][w] == n:
                return False

    return True


# print(isValidCell(1, 1, 9))


def backtrackingSol(board):
    # global board
    oldBoard = board
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if isValidCell(i, j, n):
                        board[i][j] = n
                        backtrackingSol()
                        board[i][j] = 0
                return
    if oldBoard == board:
        return
