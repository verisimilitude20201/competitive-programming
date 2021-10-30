"""
Complexity:
----------
maxProfit1
----------
Time: O(N^2)
Space: O(1)

maxProfit2
----------
Time: O(N^2)
Space: O(1)


"""
from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_buy_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_buy_price = min(min_buy_price, prices[i])
            profit = prices[i] - min_buy_price
            max_profit = max(profit, max_profit)

        return max_profit

solution = Solution()
print(solution.maxProfit1([7,1,5,3,6,4]))
print(solution.maxProfit1([7,6,4,3,1]))

print(solution.maxProfit2([7,1,5,3,6,4]))
print(solution.maxProfit2([7,6,4,3,1]))