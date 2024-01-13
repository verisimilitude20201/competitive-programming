"""
Complexity:
---------
Time: O(N)
Space: O(N)
"""
class Solution1:
    def numWays(self, n: int, k: int) -> int:

        @lru_cache(None)
        def dp(n):
            if n == 1:
                return k
            if n == 2:
                return k * k

            return (k - 1) * (dp(n - 1) + dp(n - 2))

        return dp(n)

class Solution2:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n + 1):
            dp[i] = (k - 1) * (dp[i - 2] + dp[i - 1])
        
        return dp[n]
        