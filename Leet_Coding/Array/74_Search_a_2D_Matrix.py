"""
Explanation:
-----------
According to row major format
Index in 1-D array of an equivalent 2-D array = row_index * number of columns + col_index

[      0 1 2 3 
    0 [1,3,5,7],
    1 [10,11,16,20],
    2 [23,30,34,60]
]

matrix[1][1] (15) = 1 * 4 + 1 = 5

0 1 2 3  4  5  6  7  8   9 10 11
[1,3,5,7,10,11,16,20,23,30,34,60]
            |

Hence if we are given 5th index of a 1-D array

row_index = index // nCols
col_index = index % nCols

Complexity:
----------
Time: O(M*N)
Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row_count = len(matrix)
        col_count = len(matrix[0])
        low = 0
        high = (row_count * col_count) - 1

        while low <= high:

            pivot_idx = low + ((high - low) // 2)
            pivot_element = matrix[pivot_idx // col_count][pivot_idx % col_count]
            if pivot_element == target:
                return True
            elif pivot_element < target:
                low = pivot_idx + 1
            else:
                high = pivot_idx - 1

        return False