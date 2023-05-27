"""
Complexity:
----------
Time: O(M * N * K)
Space: O(M * N * K)
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def is_valid(new_row, new_col) -> bool:
            return 0 <= new_row < m and 0 <= new_col < n
            
        seen = set()
        Q = deque([(0, 0, 0, k)])
        seen.add((0, 0, k))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        
        while len(Q):
            row, col, steps, remains = Q.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if is_valid(new_row, new_col):
                        if grid[new_row][new_col] == 0 and (new_row, new_col, remains) not in seen:
                            seen.add((new_row, new_col, remains))
                            Q.append((new_row, new_col, steps + 1, remains))
                        elif remains > 0 and (new_row, new_col, remains - 1) not in seen:
                            seen.add((new_row, new_col, remains - 1))
                            Q.append((new_row, new_col, steps + 1, remains - 1))
                    
        
        return -1