"""
Problem:
-------
Given an unsorted array of numbers, find Kth smallest number in it.

Example:
-------
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Complexity:
---------
Time: O(N * K)
Space: O(1)

"""

import math


def find_kth_smallest_num_in_array(nums, k):
    current_smallest_num, current_smallest_index = math.inf, -1
    prev_smallest_num, prev_smallest_index = -math.inf, -1

    for i in range(k):
        for j in range(len(nums)):
            if prev_smallest_num < nums[j] < current_smallest_num:
                current_smallest_num = nums[j]
                current_smallest_index = j
            elif prev_smallest_num == nums[j] and j > prev_smallest_index:
                current_smallest_num = nums[j]
                current_smallest_index = j
                break
        prev_smallest_num = current_smallest_num
        prev_smallest_index = current_smallest_index
        current_smallest_num = math.inf

    return prev_smallest_num


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest_num_in_array([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_kth_smallest_num_in_array([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_kth_smallest_num_in_array([5, 12, 11, -1, 12], 3)))


main()
