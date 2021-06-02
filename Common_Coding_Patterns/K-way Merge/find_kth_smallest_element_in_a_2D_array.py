"""
Problem:
-------
Given an N∗NN * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example:
-------
Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.

Approach:
-------

Complexity
----------
Space: O(N)
Time: O(min(K, N) + K log N) 
       min(K, N) because we insert the 0th element in the heap from min(K, N) rows of the matrix
"""

from heapq import *


def find_kth_smallest_element(matrix, k):
    number = -1
    min_heap = []
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    number_count = 0
    while min_heap:
        number, i, row = heappop(min_heap)
        if number_count == k - 1:
            return number
        if i < len(row):
            i += 1
            heappush(min_heap, (row[i], i, row))
        number_count += 1


    return -1

def main():
  print("Kth smallest number is: " +
        str(find_kth_smallest_element([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()