"""
Complexity:
----------
Time: O(N^2)
Space: O(N)

"""
class Solution:
    def __init__(self):
        self._cache = {}

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        minimum_path_sum = math.inf
        rows = len(matrix)
        cols = len(matrix[0])
        for col in range(cols):
            minimum_path_sum = min(minimum_path_sum, self.minimum_sum(matrix, 0, col))

        return minimum_path_sum

    def minimum_sum(self, matrix, row, col):
        if col < 0 or col >= len(matrix[0]):
            return math.inf

        if row == len(matrix) - 1:
            return matrix[row][col]

        if (row, col) in self._cache:
            return self._cache[(row, col)]

        left_diagonal = self.minimum_sum(matrix, row + 1, col - 1)
        right_diagonal = self.minimum_sum(matrix, row + 1, col + 1)
        down = self.minimum_sum(matrix, row + 1, col)

        self._cache[(row, col)] = matrix[row][col] + min(left_diagonal, right_diagonal, down)

        return self._cache[(row, col)]