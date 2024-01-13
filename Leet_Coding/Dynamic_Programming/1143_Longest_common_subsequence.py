"""
Complexity:
----------
Time: O(M * N^2)
Space: O(M * N)
"""

from functools import lru_cache

class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)
            
            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)
            
            # Return the best option.
            return max(option_1, option_2)
                
        return memo_solve(0, 0)
    
"""
Complexity:
----------
Time: O(M * N)
Space: O(M * N)
"""
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        cache = dict()
        
        def lcs(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if(p1, p2) in cache:
                return cache[(p1, p2)]
            
            if text1[p1] == text2[p2]:
                cache[(p1, p2)] = 1 + lcs(p1 + 1, p2 + 1)
                return cache[(p1, p2)]
            
            cache[(p1, p2)] = max(lcs(p1 + 1, p2), lcs(p1, p2 + 1))
            return cache[(p1, p2)]
        
        return lcs(0, 0)
    

"""
Complexity:
----------
Time: O(M * N)
Space: O(M * N)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                char1 = text1[i]
                char2 = text2[j]
                if char1 == char2:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]