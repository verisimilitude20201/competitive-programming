"""
Complexity:
----------
Time: O(n * amount)
Space: O(n * amount) # cache will take that much space.
 Recursion stack will take O(n + amount), we either increase the coins 
 or decrease the amount.
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        n = len(coins)

        def number_of_ways(i, amount):
            if i == n or amount < 0:
                return 0
            if amount == 0:
                return 1

            if (i, amount) in cache:
                return cache[(i, amount)]

            cache[(i, amount)] = number_of_ways(i, amount - coins[i]) + number_of_ways(i + 1, amount)

            return cache[(i, amount)]

        return number_of_ways(0, amount)