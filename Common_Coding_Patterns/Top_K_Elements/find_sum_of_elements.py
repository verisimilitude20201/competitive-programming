"""
Problem
-------
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Example:
-------
Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).

Approach:
--------
1. Add all elements between min_heap
2. Continue to pop the elements from min_heap and maintain a counter
3. Once that counter passes k1 and is less than k2, take the total of elements (between k1 and k2)

Complexity:
----------
Time: O(N log N)
Space: O(N)
"""

from heapq import *


def find_sum_of_elements(nums, k1, k2):
    sum_of_elements = 0
    min_heap = []
    for num in nums:
        heappush(min_heap, num)

    k = 1
    while min_heap:
        num1 = heappop(min_heap)
        if k1 < k < k2:
            sum_of_elements += num1
        k += 1

    return sum_of_elements


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
