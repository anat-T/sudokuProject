class Sudoku:
    # Complete sudoku board, from which we will get sudoku puzzle
    completeBoard = [[]]
    # integer which will determine the difficulty of the puzzle. 1 to 4?
    level = 1


def __init__(self, completeBoard, level):
    self.completeBoard = completeBoard
    self.level = level
