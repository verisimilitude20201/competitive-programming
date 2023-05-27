"""
Complexity:
---------
Time: O(R * C)
Space: O(R * C)
"""
class Solution:
    def __init__(self):
        self._directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self._seen = set()
        self.max_area = 0
        self.m = 0
        self.n = 0
        self.grid = []
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1 and (i, j) not in self._seen:
                    area = self.cal_area(i, j)
                    self.max_area = max(area, self.max_area)
                    self._seen.add((i, j))
                    
        return self.max_area
    
    def cal_area(self, row, col) -> int:
        if (row, col) in self._seen or not self.valid(row, col) or self.grid[row][col] == 0:
            return 0
        self._seen.add((row, col))
        return 1 + self.cal_area(row + 1, col) + self.cal_area(row - 1, col) + self.cal_area(row, col + 1) + self.cal_area(row, col - 1)
    
    def valid(self, row, col):
        return 0 <= row < self.m and 0 <= col < self.n