"""
Problem:
-------
Here after calculating max profit we find the selected items

Approach:
--------
                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|0 |1 |2 |5 |5 |6 |7 |7 |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|0 |1 |2 |5 |6 |6 |7 |8 |
                  +--+--+--+--+--+--+--+--+--+

1) Consider max profit, it's included in 4th row. We got 8 only because we considered 4th row so include 8.


2) Now the remaining profit is 8 - 6 = 2. Check if 2 is included in the 3rd row. Yes, but it's value has not changed from the 2nd row. So skip it.

3) Consider 2nd row. Check if 2 is present, yes it is. So Consider the 2nd object. Now remaining capacity is  2 - 2 = 0

4) Consider 1st object. But now since remaining capacity is 0, we cannot include any more objects

So we include just 2nd and 4th object.



"""

def solve_knapsack(profits, weight, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weight) != n:
        return 0

    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if weight[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            if weight[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weight[i]]
            profit2 = dp[i - 1][c]
            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weight, profits, capacity)

    return dp[n - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    n = len(profits)
    total_profit = dp[n - 1][capacity]
    for i in range(n - 1, 0, -1):
        if total_profit != dp[i - 1][capacity]:
            print(str(weights[i]), end=" ")
            capacity -= weights[i]
            total_profit -= profits[i]

    if total_profit != 0:
        print(str(weights[0]), end=" ")

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
