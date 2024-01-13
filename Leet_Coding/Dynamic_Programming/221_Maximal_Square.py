"""
Complexity:
-----------
Time: O(M * N)
Space: O(M * N)
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {}
        rows = len(matrix)
        cols = len(matrix[0])
        max_length = 0

        def helper(row, col):
            nonlocal max_length
            if row >= rows or col >= cols:
                return 0

            if (row, col) not in cache:
                cache[(row, col)] = 0
                down = helper(row + 1, col)
                right = helper(row, col + 1)
                diag = helper(row + 1, col + 1)
                if matrix[row][col] == "1":
                    cache[(row, col)] = 1 + min(down, right, diag)
                    max_length = max(cache[(row, col)], max_length)
            
            return cache[(row, col)]

        helper(0, 0)
        return  max_length * max_length