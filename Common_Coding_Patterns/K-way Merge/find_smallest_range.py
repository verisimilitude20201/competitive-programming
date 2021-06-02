"""
Problem:
-------
Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

Example:
-------
Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
Output: [4, 7]
Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

Approach:
--------

Complexity:
----------
Space: O(M) Heap will contain one element from M-input arrays
Time: O(N * log M) Where N is the length of each sub-array and M is the total number of sub-arrays in matrix

"""
from heapq import *
import math


def find_smallest_range(matrix):
    range_start = 0
    range_end = math.inf
    min_heap = []
    current_max_number = matrix[0][0]
    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))
        current_max_number = max(current_max_number, matrix[i][0])

    while len(matrix) == len(min_heap):
        num, i, arr = heappop(min_heap)
        if range_end - range_start > current_max_number - num:
            range_end = current_max_number
            range_start = num

        if len(arr) > i + 1:
            heappush(min_heap, (arr[i + 1], i + 1, arr))
            current_max_number = max(current_max_number, arr[i + 1])

    if range_start == 0 and range_end == math.inf:
        return [-1, -1]

    return [range_start, range_end]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()