"""
Complexity:
-----------
Solution 1: Brute force
Time: O(2^N)
Space: O(N)

Solution 2: Brute force with memoization
Time: O(N)
Space: O(N)


Solution 3: Dynamic programming
Time: O(N)
Space: O(N)
"""

class Solution1:
    def climbStairs(self, n: int) -> int:
        def climb(i, n):
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            return climb(i + 1, n) + climb(i + 2, n)
        
        return climb(0, n)
    

class Solution2:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(i, n):
            if i > n:
                return 0
            
            if i == n:
                return 1
            if i in cache:
                return cache[i]
            cache[i] = climb(i + 1, n) + climb(i + 2, n)
            return cache[i]
        
        return climb(0, n)

class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2]  = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]