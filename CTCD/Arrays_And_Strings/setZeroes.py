"""

Complexity:
---------
Time: O(M*N)
Space: O(max(M, N))

"""
def setZeroes(matrix):
    rows = [None] * len(matrix)
    cols = [None] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows[i] = 0
                cols[j] = 0

    for k in range(len(rows)):
        if rows[k] is not None:
            nullify_rows(matrix, k)

    for k in range(len(cols)):
        if cols[k] is not None:
            nullify_cols(matrix, k)


def nullify_rows(matrix, row_index):
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] = 0


def nullify_cols(matrix, col_index):
    for i in range(len(matrix)):
        matrix[i][col_index] = 0

matrix = [
    [0, 4, 1, 4, 4],
    [8, 10, 2, 3, 4],
    [9, 6, 3, 4, 4]]

setZeroes(matrix)
print(matrix)
