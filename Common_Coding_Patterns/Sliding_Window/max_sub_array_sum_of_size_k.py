"""
Problem
-------
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]

Approach
-------
Brute Force - Take continuous sum of K elements starting from 0th element, calculate total at each step and current max
Fixed length Window of Size K. 

Complexity
---------

Brute Force: 
-----------
    Time: O(N * K) Also performs repeated computation of sum. For example for index 1-5, the sum of elements at index 1 to 4 is already computed
    Space: O(1)

Sliding Window:
-------------
    Time: O(N)
    Space: O(1)

"""

import math

def max_sub_array_sum_of_size_k1(K, arr):
    total = 0
    max_total = -math.inf
    for i in range(len(arr) - K + 1):
        total = 0
        for j in range(i, i + K):
            total += arr[j]
        max_total = max(max_total, total)

    return max_total


def max_sub_array_sum_of_size_k2(K, arr):
    max_total = -math.inf
    total = 0
    window_start = 0
    for window_end in range(len(arr)):
        total += arr[window_end]
        if window_end >= K - 1:
            max_total = max(max_total, total)
            total -= arr[window_start]
            window_start += 1

    return max_total


def main():
    print( str(max_sub_array_sum_of_size_k1(3, [2,1,5, 1,3, 2])))
    print(str(max_sub_array_sum_of_size_k2(3, [2, 1, 5, 1, 3, 2])))


main()