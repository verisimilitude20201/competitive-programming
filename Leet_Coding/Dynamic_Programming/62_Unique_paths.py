"""
Complexity:
----------
Time: O(M * N)
Space: O(M * N)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def dep(i, j):
            if i >= m or j >= n:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            if (i, j) in cache:
                return cache[(i, j)]
                
            cache[(i, j)] = dep(i + 1, j) + dep(i, j + 1)
            
            return cache[(i, j)]
        
        return dep(0, 0)