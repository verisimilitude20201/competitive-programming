"""
Complexity:
----------
Time: O(M * N * log K) Where K is the effort
Space: O(M * N)

"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
            
        def check(effort):
            stack = [(0, 0)]
            seen = set()
            seen.add((0, 0))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if valid(new_row, new_col) and (new_row, new_col) not in seen and abs(heights[new_row][new_col] - heights[row][col]) <= effort:
                        seen.add((new_row, new_col))
                        stack.append((new_row, new_col))
                        
            
            return False
        
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            
    
    