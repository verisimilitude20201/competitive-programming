"""
Problem:
--------

Given a sorted number array and two integers ‘K’ and ‘X’, 
find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example:
--------
Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]

Approach:
--------
1. Store a tuple of absolute difference between arr[i] - K on a min_heap i.e (abs(arr[i] - K, arr[i]))
2. Pop first K entries and add to output

Complexity:
----------
Time: O(N Log N + K log K)
Space: O(K)

"""

from heapq import *


def find_closest_numbers(arr, K, X):

    minHeap = []
    for i in range(len(arr)):
        heappush(minHeap, (abs(arr[i] - X), arr[i]))

    result = []
    for _ in range(K):
        result.append(heappop(minHeap)[1])

    result.sort()
    return result


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_numbers([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_numbers([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_numbers([2, 4, 5, 6, 9], 3, 10)))


main()
