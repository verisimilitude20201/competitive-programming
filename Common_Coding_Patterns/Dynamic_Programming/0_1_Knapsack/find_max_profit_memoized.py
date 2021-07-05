"""
Problem:
-------
Given, capacity of Knapsack = 7, Weight = [1, 3, 4, 5] and Value = [1, 4, 5, 7]. Find the max profit by adding items such that the total weight is less than or 
equal to its capacity.

Explanation:
-----------
1. Just cache the profit for the ith item and capacity in a 2-D array will save duplicate computations from happening.

Complexity:
----------
Time: O(N*C)
Space: O(N*C)

"""

def get_max_profit_memoized(weight, value, capacity):
    dp = [[-1 for i in range(capacity + 1)] for j in range(len(weight))]

    return get_max_profit_knapsack(weight, value, capacity, len(weight) - 1, dp)


def get_max_profit_knapsack(weight, value, capacity, index_of_item, dp):
    if index_of_item < 0 or capacity == 0:
        return 0
    if dp[index_of_item][capacity] != -1:
        return dp[index_of_item][capacity]
    profit_of_included_item = 0
    if weight[index_of_item] <= capacity:
        profit_of_included_item = value[index_of_item] + get_max_profit_knapsack(weight, value,
                                                                                 capacity - weight[index_of_item],
                                                                                 index_of_item - 1, dp)
    profit_of_excluded_item = get_max_profit_knapsack(weight, value, capacity, index_of_item - 1, dp)
    dp[index_of_item][capacity] = max(profit_of_included_item, profit_of_excluded_item)

    return dp[index_of_item][capacity]


print(get_max_profit_memoized([1, 3, 4, 5], [1, 4, 5, 7], 7))