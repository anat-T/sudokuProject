from backtracking import *
from board import *


def findAllValidNumbersForCell(board, i, j):
    listValids = []
    for n in range(1, 10):
        if isValidCell(board, i, j, n):
            listValids.append(n)
    return listValids


def findAllValidNumbersForEachCellOnBoard(board):
    allValidNumbers = {}
    for i in range(0, 9):
        for j in range(0, 9):
            allValidNumbers[i, j] = list(range(0, 9))
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                print(findAllValidNumbersForCell(board, i, j))
                allValidNumbers[i][j] = findAllValidNumbersForCell(board, i, j)
            else:
                allValidNumbers[i][j] = []
    return allValidNumbers


def calculatePreemptiveSet():
    return


def findSingletonsInRows(candidates, solution_):
    for i in range(0, 9):
        row = solution_[i]
        for j in range(0, 9):
            # Find the missing values in a row, that can be put in each cell
            candidates[i, j] = [
                value for value in candidates[i, j] if value not in row]
        # Find all group of values that correspond to the row i
        optionalValues = [value for key, value in candidates.items()
                          if key[0] == i and len(value) > 0]
        # Remove duplicates
        uniqueValues = [x for y in optionalValues for x in y]
        if len(uniqueValues) > 0:
            for x in uniqueValues:
                for key, value in {key: value for key, value in candidates.items() if
                                   key[0] == i and len(value) > 0}.items():
                    if x in value:
                        solution_[key[0] - 1][key[1] - 1] = x
                        candidates[key] = []
    return 0


def findSingletonsInColumns(candidates, solution_):
    for j in range(0, 9):
        column = [x[j] for x in solution_]
        for i in range(0, 9):
            # Find the missing values in a column, that can be put in each cell
            candidates[i, j] = [
                value for value in candidates[i, j] if value not in column]
        # Find all group of values that correspond to the row i
        optionalValues = [value for key, value in candidates.items()
                          if key[1] == j and len(value) > 0]
        # Remove duplicates
        uniqueValues = [x for y in optionalValues for x in y]
        if len(uniqueValues) > 0:
            for x in uniqueValues:
                for key, value in {key: value for key, value in candidates.items() if
                                   key[1] == j and len(value) > 0}.items():
                    if x in value:
                        solution_[key[0] - 1][key[1] - 1] = x
                        candidates[key] = []
           # continue
    return 0


def findSingletonsInSquars(candidates, solution_):
    return 0


def crooks(board):
    candidates = findAllValidNumbersForEachCellOnBoard(board)
    print(candidates)


# crooks()
