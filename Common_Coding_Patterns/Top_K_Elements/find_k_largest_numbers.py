"""
Problem:
--------
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example:
-------
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

Approach:
--------
0) [3, 1, 5, 12, 2, 11], Output = [11, 5, 12]



1) min_heap = [3], K = 0
2) min_heap = [3, 1], K = 1
   min_heap = [1, 3], K = 1

3) min_heap = [1, 3, 5], K = 2

4) 12 > 1 ? True. Add 12 and remove 1
   min_heap = [12, 3, 5]
   min_heap = [3, 5, 12]

5) 2 > 3? False so skip

6) 11  > 3 ? True so remove 3 and add 11
	min_heap = [11, 5, 12]
	min_heap = [5, 11, 12]


Complexity:
----------
Time: O(K * log K + (N - K) * log(N - K))
Space: O(N)

"""

from heapq import *


def find_k_largest_numbers(num, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, num[i])

    for i in range(k, len(num)):
        if num[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, num[i])

    return list(min_heap)


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
