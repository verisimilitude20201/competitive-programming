"""
Problem:
-------
Given, capacity of Knapsack = 7, Weight = [1, 3, 4, 5] and Value = [1, 4, 5, 7]. Find the max profit by adding items such that the total weight is less than or 
equal to its capacity.

Explanation:
-----------
1. Find the base condition by taking the smallest valid value. 
2. Start from n-1th item. Compute
    i. Profit of including that item: Capacity of the Knapsack will be reduced and index_of_item would also be reduced.
    ii. Profit of excluding that item: Just the index_of_item would be reduced.
3. If the (n-1)th item cannot be included, just do as 2.ii

Complexity:
----------
Time: O(2^N)
Space: O(2^N)

"""

def get_max_profit_knapsack(weight, value, capacity, index_of_item):
    if index_of_item < 0 or capacity == 0:
        return 0

    if weight[index_of_item] <= capacity:
        profit_of_included_item = value[index_of_item] + get_max_profit_knapsack(weight, value, capacity - weight[index_of_item], index_of_item - 1)
        profit_of_excluded_item = get_max_profit_knapsack(weight, value, capacity, index_of_item - 1)
        return max(profit_of_included_item, profit_of_excluded_item)
    else:
        return get_max_profit_knapsack(weight, value, capacity, index_of_item - 1)


print(get_max_profit_knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7, 3))