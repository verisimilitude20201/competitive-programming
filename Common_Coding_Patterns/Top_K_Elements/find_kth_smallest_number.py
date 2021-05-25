"""
Problem:
-------
Given an unsorted array of numbers, find Kth smallest number in it.

Example:
-------
[1, 5, 12, 2, 11, 5], Output = [5]

Approach:
--------
0) [1, 5, 12, 2, 11, 5], Output = [5]



1) max_heap = [1], K = 0
2) max_heap = [5, 1], K = 1
3) max_heap = [12, 1, 5], K = 2

4) Add 2. 2 < 12

   max_heap = [2, 1, 5]
   max_heap = [5, 1, 2]

5) Add 11, 11 > 5 so don't add

6) Add 5, 5 > 5 so don't add

Complexity:
----------
Time: O(K * log K + (N - K) * log(N - K))
Space: O(N)
"""


from heapq import *


def find_kth_smallest_number(nums, k):
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
