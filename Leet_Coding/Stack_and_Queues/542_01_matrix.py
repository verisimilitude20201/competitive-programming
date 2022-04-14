"""
Explanation:
----------
 [  0 1 2
 0 [0,0,0],
 1 [0,1,0],
 2 [1,1,1]
]

distance = 

[  0  1   2
 
 0 0  0   0
 
 1 0  IN  0
 
 2 IN IN  IN
]

Q =[[2, 1]]

distance = [[1, 0], [-1, 0], [0, 1], [0, -1]]

r = 1  , c = 2; row = 1 , col = 1

Complexity:
----------
Time: O(M * N)
Space: O(M * N)
"""
import math
from collections import deque


class Solution:
    def __init__(self):
        self.Q = deque([])
        self.distance = None

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        if m == 0:
            return mat
        n = len(mat[0])
        self.distance = [[math.inf] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    self.distance[i][j] = 0
                    self.Q.append([i, j])

        self.calculate_distance_to_nearest_non_zero(m, n)

        return self.distance

    def calculate_distance_to_nearest_non_zero(self, m: int, n: int) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while len(self.Q):
            row, col = self.Q.popleft()
            for direction in directions:
                r = row + direction[0]
                c = col + direction[1]
                if 0 <= r < m and 0 <= c < n:
                    if self.distance[r][c] > self.distance[row][col] + 1:
                        self.distance[r][c] = self.distance[row][col] + 1
                        self.Q.append([r, c])