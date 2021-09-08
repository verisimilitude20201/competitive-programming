"""

Complexity:
---------

setZeroes --> 
Time: O(M*N)
Space: O(M + N)

set_zeroes2 -->
Time: O(M*N)
Space: O(1)

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


def set_zeroes2(matrix):

    row_has_zero = False
    col_has_zero = False

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            row_has_zero = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            col_has_zero = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)
    if row_has_zero:
        nullify_row(matrix, 0)
    if col_has_zero:
        nullify_column(matrix, 0)

matrix = [
    [0, 4, 1, 4, 4],
    [8, 10, 2, 3, 4],
    [9, 6, 3, 4, 4]]

setZeroes(matrix)
print(matrix)
