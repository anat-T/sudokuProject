
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


print(isValidCell(1, 1, 9))
