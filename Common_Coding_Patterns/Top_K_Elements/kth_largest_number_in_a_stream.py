"""
Problem:
-------
Design a class to efficiently find the Kth largest element in a stream of numbers.

Example:
-------
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.

Approach:
--------
Keep on adding elements to a min-heap and delete on-by-one if the length of min_heap exceeds k

0) [3, 1, 5, 12, 2, 11], min_heap = [], K = 4

1) Add first 5 elements to min_heap
   min_heap = [1, 2, 3, 5, 12]


2) len(min_heap) > 4
    Remove 1
    min_heap = [2, 3, 5, 12]

3) Add 11
   min_heap = [2, 3, 5, 11, 12]

4) Remove 2 
min_heap = [3, 5, 11, 12]

5) Add 6

min_heap = [3, 5, 6, 11, 12]

6) Remove 3
min_heap = [5, 6, 11, 12]


7) Add 13
min_heap = [5, 6, 11, 12, 13]

8) Remove 5
min_heap = [6, 11, 12, 13]

Complexity:
----------
Time: O(N log K + log K)
Space: O(K)
"""

from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, num):
        heappush(self.min_heap, num)

        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
