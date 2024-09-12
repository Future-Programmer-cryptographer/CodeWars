import random
from random import randint
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

    def getBlockIndex(self):
        

    # Cost function using collisions (similar to Andrew's fitness for hillClimb)
    # collisions = 0 = sudoku is solved
    def evaluate(self):
        collisions = 0

        # column collisions
        for col in range(9):
            col_encountered = set()
            for row in range(9):
                if self.board[row][col] in col_encountered:
                    collisions += 1
                else:
                    col_encountered.add(self.board[row][col])

        # chunk collisions
        for chunk_n_row in range(0, 9, 3):
            for chunk_w_col in range(0, 9, 3):
                chunk_encountered = set()
                for chunk_row in range(3):
                    for chunk_col in range(3):
                        row = chunk_n_row + chunk_row
                        col = chunk_w_col + chunk_col

                        if self.board[row][col] in chunk_encountered:
                            collisions += 1
                        else:
                            chunk_encountered.add(self.board[row][col])

        return collisions


    # fill in all empty spaces by brute force:
    # values in rows will always be non repeating to ensure row shuffle does not produce collisions
    def fill_randomly(self):
        for i in range(9):
            row_vals = []
            for j in range(9):
                if self.fixed[i][j]:
                    row_vals.append(self.board[i][j])

            missing_vals = []
            for n in range(1, 10):  # 1-9
                if not (n in row_vals):
                    missing_vals.append(n)
            random.shuffle(missing_vals)

            for j in range(9):
                if not self.fixed[i][j]:
                    self.board[i][j] = missing_vals.pop()

    def generateCandidateKey(self):
        newKey = deepcopy(self.data)
        block = randint(0,8)
        numInBlock = len(self.)

    def annealing(self):
        start = time()
        temp = 0.99
        count = 0

        while (count<40000):
            try:
                if count%1000 == 0:


        end = time()

        print("Sudoku solved:")
        print("Time taken:", end-start)
        print("Iterations taken:", iterations)
        self.print_board()


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

    shc = SudokuHillClimber(board)
    shc.hillClimb()

