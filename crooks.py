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


def check_row(possible_value_, solution_):
    """
    :param possible_value_: the dict of storing all possible numbers of each cell
    :param solution_: the list of existing solution
    Based on Sudoku rule, check for each row and see if there is an unique possible number across a row.
    If so, update the possible_value_ and solution_.
    """
    for i in range(1, 10):
        exist = solution_[i - 1]
        print("exist:", exist)
        for j in range(1, 10):
            print("possible_value[i][j] before:",  possible_value_[i, j])
            possible_value_[i, j] = [
                x for x in possible_value_[i, j] if x not in exist]
            print("after:",  possible_value_[i, j])

        possible_element = [x for y in [value for key, value in possible_value_.items()
                                        if key[0] == i and len(value) > 0] for x in y]
        print("possible_element:",  possible_element)
        unique = [
            x for x in possible_element if possible_element.count(x) == 1]
        print("unique:", unique)
        if len(unique) > 0:
            for x in unique:
                for key, value in {key: value for key, value in possible_value_.items() if
                                   key[0] == i and len(value) > 0}.items():
                    if x in value:
                        solution_[key[0] - 1][key[1] - 1] = x
                        possible_value_[key] = []
    return
