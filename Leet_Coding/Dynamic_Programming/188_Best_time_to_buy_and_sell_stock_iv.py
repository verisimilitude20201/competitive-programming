"""
Complexity:
----------
Time: O(N * k)
Space: O(N)
"""
from functools import lru_cache

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, transactions_remaining, holding):
            if transactions_remaining == 0 or i == len(prices):
                return 0

            do_nothing = dp(i + 1, transactions_remaining, holding)
            do_something = 0
            if holding:
                do_something = prices[i] + dp(i + 1, transactions_remaining - 1, 0)
            else:
                do_something = -prices[i] + dp(i + 1, transactions_remaining, 1)

            return max(do_something, do_nothing)

        return dp(0, k, 0)