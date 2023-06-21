class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def change_coins(balance):
            if balance < 0:
                return -1

            if balance == 0:
                return 0
            if balance in cache:
                return cache[balance]

            min_cost = math.inf
            for coin in coins:
                res = change_coins(balance - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)

            cache[balance] = min_cost if min_cost != math.inf else -1
            return cache[balance]

        return change_coins(amount)