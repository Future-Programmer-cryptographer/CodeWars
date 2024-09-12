import random
from time import time


class SudokuHillClimber:
    def __init__(self, board):
        self.board = board

        self.row_pointer = 0
        self.col1_pointer = 0
        self.col2_pointer = 0

    def print_board(self):
        for row in self.board:
            print(row)
        print()

        # using collisions as a fitness funciton, the lower the score the better

    # rows don't need to be checked since they are always collisionless
    # (collisions = 0 means sudoku is solved)
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

    # decided to keep rows fixed since logic is the easiest to deal with
    def randomise_element_pair(self):
        self.row_pointer = random.randint(0, 8)
        self.col1_pointer = random.randint(0, 8)

        while True:
            self.col2_pointer = random.randint(0, 8)

            if not (self.col1_pointer == self.col2_pointer):
                break

    # swaps two elements indicated by self
    def shuffle(self):
        self.board[self.row_pointer][self.col1_pointer], self.board[self.row_pointer][self.col2_pointer] = \
        self.board[self.row_pointer][self.col2_pointer], self.board[self.row_pointer][self.col1_pointer]

    # swaps 5 times to get out of local minima
    def shake(self):
        for _ in range(5):
            self.randomise_element_pair()
            self.shuffle()

    def hillClimb(self):
        self.fixed = [[(board[i][j] != 0) for j in range(9)] for i in range(9)]

        self.fill_randomly()
        fitness = self.evaluate()

        iterations = 0
        withoutClimbing = 0

        start_t = time()

        while fitness > 0:
            self.randomise_element_pair()
            self.shuffle()
            new_fitness = self.evaluate()

            if new_fitness < fitness:
                fitness = new_fitness
                withoutClimbing = 0
                print(f"Best fitness: {fitness}")
                self.print_board()
            else:
                # undo shuffle
                self.shuffle()

                # to prevent getting stuck on local minima
                if withoutClimbing > 5000:
                    self.shake()
                    fitness = self.evaluate()
                    withoutClimbing = 0
                else:
                    withoutClimbing += 1

            iterations += 1

        end_t = time()

        print("Sudoku solved:")
        print("Time taken:", end_t - start_t)
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

