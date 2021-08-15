"""
Problem:
-------
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ 
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

Example:
-------
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5


Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.

Complexity:
----------
Time: O(N * C)
Space: O(N * C)

"""

def solve_knapsack_max_profits_memoized(profits, weights, capacity):
    dp = [[-1 for y in range(capacity + 1)] for x in range(len(profits))]

    return solve_knapsack_recursive(profits, weights, capacity, len(profits) - 1, dp)


def solve_knapsack_recursive(profits, weights, capacity, currentIndex, dp):
    if currentIndex < 0 or capacity == 0:
        return 0

    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    profit_excluding_item = solve_knapsack_recursive(profits, weights, capacity, currentIndex - 1, dp)
    profits_including_item = 0
    if weights[currentIndex] <= capacity:
        profits_including_item = profits[currentIndex] + solve_knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex - 1, dp)

    dp[currentIndex][capacity] = max(profit_excluding_item, profits_including_item)

    return dp[currentIndex][capacity]


def main():
    print(solve_knapsack_max_profits_memoized([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_max_profits_memoized([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
