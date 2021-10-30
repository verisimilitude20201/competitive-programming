from typing import List
from queue import Queue


"""
Complexity:
----------
matrixReshape1
--------------
Time: O(M * N)
Space: O(M * N)

matrixReshape2
--------------
Time: O(M * N)
Space: O(M * N)

"""
class Solution:
    def matrixReshape1(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0 or r * c != len(mat) * len(mat[0]):
            return mat

        result = [[None] * c for _ in range(r)]
        queue1 = Queue(maxsize=r * c)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                queue1.put(mat[i][j])

        for i in range(r):
            for j in range(c):
                result[i][j] = queue1.get()

        return result

    def matrixReshape2(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == 0 or r * c != len(mat) * len(mat[0]):
            return mat

        result = [[None] * c for _ in range(r)]
        row, col = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                result[row][col] = mat[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        return result


solution = Solution()
print(solution.matrixReshape1([[1, 2], [3, 4]], 1, 4))
print(solution.matrixReshape1([[1, 2], [3, 4]], 2, 4))


