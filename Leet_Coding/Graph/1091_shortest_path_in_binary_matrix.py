"""
Complexity:
---------
Time: O(N)
Space: O(N)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        seen = set((0, 0))
        Q = deque([(0, 0, 0)])
        n = len(grid)
        while len(Q):
            row, col, steps = Q.popleft()
            if row == n - 1 and col == n - 1:
                return steps + 1
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if self.is_valid(grid, new_row, new_col, n) and (new_row, new_col) not in seen:
                    Q.append((new_row, new_col, steps + 1))
                    seen.add((new_row, new_col))
        
        return -1
    
    def is_valid(self, grid, row, col, n) -> bool:
        return 0 <= row < n and 0 <= col < n and grid[row][col] == 0