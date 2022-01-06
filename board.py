class Board:
    board = [
        [0, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 0, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 0, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7]
    ]
    optional_values = [[]]
    dimension = 9

    def __init__(self, board, optional_values, dimension):
        self.board = board
        self.optional_values = optional_values
        self.dimension = dimension


# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]


# board = [
#     [0, 8, 5, 4, 3, 9, 1, 2, 6],
#     [6, 1, 2, 8, 7, 5, 3, 4, 9],
#     [4, 9, 3, 6, 2, 1, 0, 7, 8],
#     [8, 5, 7, 9, 4, 3, 2, 6, 1],
#     [2, 6, 1, 7, 5, 8, 9, 3, 4],
#     [9, 3, 4, 1, 6, 2, 7, 8, 5],
#     [5, 7, 8, 3, 0, 4, 6, 1, 2],
#     [1, 2, 6, 5, 8, 7, 4, 9, 3],
#     [3, 4, 9, 2, 1, 6, 8, 5, 7]
# ]
