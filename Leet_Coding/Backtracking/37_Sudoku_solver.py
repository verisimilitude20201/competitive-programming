"""
Complexity:
----------
Time: O(9!)^9
Space: O(81)

Complexity here can't be expressed in terms of N because the board is given to be N * N
"""
class Solution:
    def __init__(self):
        self.N = 9
        self.rows = [defaultdict(int) for _ in range(self.N)]
        self.cols = [defaultdict(int) for _ in range(self.N)]
        self.boxes = [defaultdict(int) for _ in range(self.N)]
        self.is_sudoku_solved = False
        self.board = []

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        for i in range(self.N):
            for j in range(self.N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    self.place_numbers(d, i, j)
        self.backtrack()

    def backtrack(self, row=0, col=0):
        if self.board[row][col] == ".":
            for d in range(1, 10):
                if self.could_place(d, row, col):
                    self.place_numbers(d, row, col)
                    self.place_next_numbers(row, col)
                    if not self.is_sudoku_solved:
                        self.remove_numbers(d, row, col)

        else:
            self.place_next_numbers(row, col)

    def could_place(self, d, row, col):
        return not (d in self.rows[row] or d in self.cols[col] or d in self.boxes[self.get_box_index(row, col)])

    def place_next_numbers(self, row, col):
        if row == self.N - 1 and col == self.N - 1:
            self.is_sudoku_solved = True
        else:
            if col == self.N - 1:
                self.backtrack(row + 1, 0)
            else:
                self.backtrack(row, col + 1)

    def place_numbers(self, d, row, col):
        self.rows[row][d] += 1
        self.cols[col][d] += 1
        box_index = self.get_box_index(row, col)
        self.boxes[box_index][d] += 1
        self.board[row][col] = str(d)

    def remove_numbers(self, d, row, col):
        del self.rows[row][d]
        del self.cols[col][d]
        box_index = self.get_box_index(row, col)
        del self.boxes[box_index][d]
        self.board[row][col] = "."

    def get_box_index(self, row, col):
        return (row // 3) * 3 + (col // 3)