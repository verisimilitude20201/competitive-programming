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

def solve_knapsack(profits, weights, capacity):
    cache = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return solve_knapsack_recursive(profits, weights, capacity, 0, cache)


def solve_knapsack_recursive(profits, weights, capacity, current_index, cache):
    if capacity <= 0 or current_index >= len(profits):
        return 0
    if cache[current_index][capacity] != -1:
        return cache[current_index][capacity]

    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + solve_knapsack_recursive(profits, weights, capacity - weights[current_index],
                                                                    current_index + 1, cache)

    profit2 = solve_knapsack_recursive(profits, weights, capacity, current_index + 1, cache)
    cache[current_index][capacity] = max(profit1, profit2)

    return cache[current_index][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
