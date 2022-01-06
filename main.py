from backtracking import *
from crooks import *
import time
from board import *


def main():
    sudoku = Board([
        [0, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 0, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 0, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7]
    ], [[]], 9)
    #     start_time = time.time()
    solution = backtrackingSol(sudoku.board)
    print(solution)
#     print("--- %s seconds ---" % (time.time() - start_time))


main()
