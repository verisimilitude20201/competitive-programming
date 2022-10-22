"""
Complexity:
----------
Time: O(M + N)
Space: O(M + N)
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic1 = defaultdict(int)
        for row in grid:
            dic1[tuple(row)] += 1
        
        dic2 = defaultdict(int)
        
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            dic2[tuple(current_col)] += 1
        ans = 0
        for key in dic1:
            ans += (dic1[key] * dic2[key])
        
        return ans 