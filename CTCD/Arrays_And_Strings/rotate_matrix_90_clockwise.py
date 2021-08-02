"""
Explanation:
-----------
[      0  1  2
	0 [7, 4, 1],
	1 [8, 5, 2],
	2 [9, 6, 3]

]
temp = matrix[0][0]

matrix[0][0] = matrix[2][0]
matrix[2][0] = matrix[2][2]
matrix[2][2] = matrix[0][2]
matrix[0][2] = top

Complexity:
----------
Time: O(N^2)
Space: O(1)
"""
def rotate_matrix_90_clockwise(matrix):
    n = len(matrix[0])
    if len(matrix) != len(matrix[0]):
        return False

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            # Save top left
            temp = matrix[i][j]
            # Copy bottom left to top left
            matrix[i][j] = matrix[n - 1 - j][i]
            # Copy bottom right to bottom left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            # Copy top right to bottom right
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            # Copy old top left to top right
            matrix[j][n - 1 - i] = temp


A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

rotate_matrix_90_clockwise(A)
print(A)
