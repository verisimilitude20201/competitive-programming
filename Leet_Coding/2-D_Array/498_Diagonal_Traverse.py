"""
Complexity:
----------
Solution 2:
----------
Time: O(M * N)
Space: O(1)
"""

class Solution1:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []

        index_sum = defaultdict(list)
        diagonals = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                num = mat[i][j]
                index_sum[i + j].append(num)

        for i_sum, elements in index_sum.items():
            if i_sum % 2 == 0:
                [diagonals.append(x) for x in elements[::-1]]
            else:
                [diagonals.append(x) for x in elements]

        return diagonals

class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0 or len(mat[0]) == 0:
            return []
        direction = 1
        result = []
        M = len(mat)
        N = len(mat[0])
        row, col = 0, 0
        while row < M and col < N:
            result.append(mat[row][col])
            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)
            if new_row < 0 or new_row == M or new_col == N or new_col < 0:
                if direction == 1:
                    row += (col == N - 1)
                    col += (col < N - 1)
                else:
                    col += (row == M - 1)
                    row += (row < M - 1)

                direction = 1 - direction
            else:
                row = new_row
                col = new_col

        return result