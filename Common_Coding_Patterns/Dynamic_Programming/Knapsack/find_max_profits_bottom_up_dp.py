"""
Problem:
-------
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ 
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

Approach:
-----------

Bottom up Dynamic Programming
0) Capacity = 8, Number of items = 4, Profits = [1, 2, 5, 6], Weights = [2, 3, 4, 5]

   All objects cannot be filled in bag.

  Find maximum profit by adding objects that don't exceed the capacity 8.

                  
                   Capacity --> 

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  |  |  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
1      2       1  |  |  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
2      3       2  |  |  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
5      4       3  |  |  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  |  |  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+


1) When no objects are included, there won't be any profit gained. Also when the capacity is 0, no objects can be included 

                   Capacity --> 

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+


2) Consider 1st object. while considering objects, if you are in ith row, consider objects in (i-1)th rows as well. It's weight is 2, it can only be picked up if bag capacity = 2

                   Capacity --> 

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

3) Consider 2nd object. We also include the first object. 

 i) 2nd object can be filled only in 3rd column cause it's capacity is 3

                       Capacity --> 

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0|  |  | 3|  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

ii) For second object, we cannot fill anything for columns 1 and 2 so we fill in the same values

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 3|  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

iii) If now we consider objects 1 and 2, their total weight is 5, so they can be filled in 5th column.

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

3) We now consider 3rd object.

  i) 3rd object can be included only if the capacity is 4. So we add it in 4th column

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|0 |1 |2 |5 |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

 
  ii) We can now consider all the 3 objects. So, objects 1 and 3 can be filled in column 6 because their total capacity = 6. And total profit = 6

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|0 |1 |2 |5 |  |6 |  |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

iii) Considering object 2 and 3, total weight is 7 and profit is also 7. Add in column 7
                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|0 |1 |2 |5 |  |6 |7 |  |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

iv) Beyond column 7 it will be 7 only and before column 6 it will be 6 only

                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|0 |1 |2 |5 |6 |6 |7 |7 |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|  |  |  |  |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

4) Now there is a formula to fill this table

If this table is T, 

T[i, c] = max(T[i-1][c], T[i-1, c - c[i]])


i) V[4, 1] = max(V[3,1], V[3, 1 - 5] + 6). Since there is no such location V[3, -4], that value is undefined

   We will in the value of V[3, 1] i.e. 0. Now till 5th weight, we should fill in previous values only


                   0   1  2  3  4  5  6  7  8
                  +--+--+--+--+--+--+--+--+--+
P      W       0  | 0| 0| 0| 0| 0| 0| 0| 0| 0|
                  +--+--+--+--+--+--+--+--+--+
1      2       1  | 0| 0| 1| 1| 1| 1| 1| 1| 1|
                  +--+--+--+--+--+--+--+--+--+
2      3       2  | 0| 0| 1| 2|2 | 3| 3| 3| 3|
                  +--+--+--+--+--+--+--+--+--+
5      4       3  | 0|0 |1 |2 |5 |6 |6 |7 |7 |
                  +--+--+--+--+--+--+--+--+--+
6      5       4  | 0|0 |1 |2 |5 |  |  |  |  |
                  +--+--+--+--+--+--+--+--+--+


ii) Now V[4, 5] = max(V[3, 5], V[3, 5 - 5] + 6)
                = max(5, 6) = 6
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
6      5       4  | 0|0 |1 |2 |5 |6 |  |  |  |
                  +--+--+--+--+--+--+--+--+--+

iii) V[4, 6] = max(V[3, 6], V[3, 6 - 5] + 6)
             = max(6, 6)
             = 6

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
6      5       4  | 0|0 |1 |2 |5 |6 |6 |  |  |
                  +--+--+--+--+--+--+--+--+--+

iv) V[4, 7] = max(V[3, 7], V[3, 7 - 5] + 6)
            = max(7, 7)
            = 7

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
6      5       4  | 0|0 |1 |2 |5 |6 |6 |7 |  |
                  +--+--+--+--+--+--+--+--+--+

v) V[4, 8] = max(V[3, 8], V[3, 8 - 5] + 6)
           = max(7, 2 + 6)
           = 8

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


So maximum profit = V[4][8] = 8

Complexity:
---------
Time: O(N * C)
Space: O(N * C)

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

    return dp[n - 1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
