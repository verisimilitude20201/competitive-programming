"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, buy):
            if i >= n:
                return 0

            if buy:
                return max(-prices[i] + dp(i + 1, 0), dp(i + 1, 1))
            else:
                return max(prices[i] + dp(i + 2, 1), dp(i + 1, 0))

        return dp(0, 1)