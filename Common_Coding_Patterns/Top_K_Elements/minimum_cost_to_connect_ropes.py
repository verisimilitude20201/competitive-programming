"""
Problem
-------
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
The cost of connecting two ropes is equal to the sum of their lengths.

Example:
-------
Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

Input: [3, 4, 5, 6]
Output: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

Approach:
--------

1. Take a min_heap and insert all values in it
2. While there is more than one value in the heap, continue popping off 2 elements from the heap, summing them and pushing their result back onto the heap.

Tricky:
------
If we just take the running sum of all elements, example 2 will give

(3 + 4) = 7
(7 + 5) = 12
(12 + 6) = 18
-------------
37 when the expected output is 36

Complexity:
----------
Time: O(N * log N)
Space: O(N)
"""

from heapq import *


def minimum_cost_to_connect_ropes(rope_lengths):
    total_cost = 0
    min_heap = []
    for rope_length in rope_lengths:
        heappush(min_heap, rope_length)

    min_cost = 0
    current_cost = 0
    while len(min_heap) > 1:
        current_cost = heappop(min_heap) + heappop(min_heap)
        min_cost += current_cost
        heappush(min_heap, current_cost)

    return min_cost


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
