from backtracking import *


def findAllValidNumbersForCell(i, j):
    listValids = []
    for n in range(1, 10):
        if isValidCell(i, j, n):
            listValids.append(n)
    return listValids


def findAllValidNumbersForEachCellOnBoard():
    allValidNumbers = [[]]
    for i in range(0, 9):
        for j in range(0, 9):
            allValidNumbers[i][j] = findAllValidNumbersForCell(i, j)
    return findAllValidNumbersForCell


def calculatePreemptiveSet():
    return
