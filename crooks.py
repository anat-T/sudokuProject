from backtracking import *
from board import *


def findAllValidNumbersForCell(i, j):
    listValids = []
    for n in range(1, 10):
        if isValidCell(i, j, n):
            listValids.append(n)
    return listValids


def findAllValidNumbersForEachCellOnBoard():
    allValidNumbers = {}
    for i in range(0, 9):
        for j in range(0, 9):
            allValidNumbers[i, j] = list(range(0, 9))
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                print(findAllValidNumbersForCell(i, j))
                allValidNumbers[i][j] = findAllValidNumbersForCell(i, j)
            else:
                allValidNumbers[i][j] = []
    return allValidNumbers


def calculatePreemptiveSet():
    return


def crooks():
    possible_values = findAllValidNumbersForEachCellOnBoard()
    print(possible_values)


crooks()
