"""
Problem:
-------
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it

Example:
-------
Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

Approach:
--------
0) [1, 3, 5, 12, 11, 12, 11],
Output = [11, 12]


1) num_frequency = {1: 1, 3: 1, 5: 1, 12: 2, 11: 2}


2) min_heap = [], Add 1

   min_heap = [(1, 1)]

3) Add 3
   min_heap = [(1, 1), (1, 3)]

4) Add 5

   min_heap = [(1, 1), (1, 3), (1, 5)]
   len(min_heap) > K

   Remove (1, 1)
   min_heap = [(1, 3), (1, 5)]


 5) Add 12
 	min_heap = [(1, 3), (1, 5)]
   len(min_heap) > K

   Remove (1, 3)
   min_heap = [(1, 5), (2, 12)]

 6) Add 11 
 min_heap = [(1, 3), (1, 5)]
   len(min_heap) > K

   Remove (1, 5)
   min_heap = [(2, 11), (2, 12)]

Complexity:
----------
Time: O((N * log N) + N)
Space: O(N + K) 
"""

from heapq import *


def find_k_frequent_nums(nums, k):
    top_k_nums = []
    num_frequency = {}
    for num in nums:
        num_frequency[num] = num_frequency.get(num, 0) + 1

    min_heap = []
    for num, freq in num_frequency.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)

    while min_heap:
        num = heappop(min_heap)[1]
        top_k_nums.append(num)

    return top_k_nums


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_nums([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_nums([5, 12, 11, 3, 11], 2)))


main()