from random import shuffle, random, sample, randint
from math import exp
from time import time
from copy import deepcopy

class SudokuAnnealing:

    def __init__(self, board):
        self.board = board
        self.row = 0
        self.col = 0
        self.square = 0

    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def fillRandomly(self):
        # go through array, replace 0 with random numbers
        for num in range(9):
            index = self.getSquareIndex(num)
            square = self.board[index]
            missingVals = [] 
            for i, idx in enumerate(index):
                if square[i] == 0: 
                    missingVals.append(idx)
            toFill = [] 
            for i in range(1,10):
                if i not in square: 
                    toFill.append(i)
            shuffle(toFill)
            for idx, value in zip(missingVals, toFill):
                self.board[idx] = value
    
    def getSquareIndex(self, n):
        row



    # Cost function using collisions (similar to Andrew's fitness for hillClimb)
    # collisions = 0 = sudoku is solved
    


if __name__ == "__main__":
    board = [
        [0, 7, 0, 0, 0, 5, 4, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],

        [4, 0, 0, 0, 0, 7, 0, 3, 0],
        [0, 6, 0, 3, 0, 0, 0, 1, 0],
        [9, 0, 0, 1, 0, 2, 7, 4, 0],

        [0, 0, 2, 0, 8, 6, 0, 0, 0],
        [0, 4, 0, 7, 3, 0, 0, 6, 0],
        [3, 0, 6, 9, 2, 0, 0, 0, 1]
    ]

   

