"""
Problem
-------
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example:
-------
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Approach:
--------
Cyclic sort
1. Proceed the same as cyclic sort just ignore numbers less than 0 and greater than the length of the array.

Complexity:
----------
Time: O(N)
Space: O(1)

"""

import math


def find_first_smallest_missing_positive(nums):
    i, j, n = 0, 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    i = 0
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return -math.inf


def main():
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
