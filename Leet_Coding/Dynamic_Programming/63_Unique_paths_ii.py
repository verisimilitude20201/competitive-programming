"""
Complexity:
----------
Time: O(M * N)
Space: O(1)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i in range(1, n):
            obstacleGrid[0][i] = int(obstacleGrid[0][i - 1] == 1 and obstacleGrid[0][i] == 0)

        for j in range(1, m):
            obstacleGrid[j][0] = int(obstacleGrid[j - 1][0] == 1 and obstacleGrid[j][0] == 0)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m - 1][n - 1]