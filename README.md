# sudokuProject
Program for solving and generate sudoku puzzles

The program uses both backtracking and crooks algorithm in order to find a solution, in the following order:
* Run crooks algorithm until no more changes to board (can happen if a guess is needed)
* Run backtracking on the ramaining board until solution. 


Backtracking algorithm:
* For each cell, assign value from 0 to 9, and check if thier a solution in the new board.

Crooks algorithm:
* Find all valid values for each empty cell.
* Fill all the cells which are singletons.
* Find preemptive sets, and make reduction for the valid values of cells.

