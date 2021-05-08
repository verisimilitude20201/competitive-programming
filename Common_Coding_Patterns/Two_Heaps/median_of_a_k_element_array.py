"""
Problem
-------
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example:
-------
Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

    [1, 2, -1, 3, 5] -> median is 1.5
    [1, 2, -1, 3, 5] -> median is 0.5
    [1, 2, -1, 3, 5] -> median is 1.0
    [1, 2, -1, 3, 5] -> median is 4.0



Approach
-------
Two heaps & Sliding window combined

1. Rebalance both heaps after adding and removing elements.
2. We need to maintain the heap order property after removing any element.
3. Once Kth element in the current sliding window is reached, we compute the median and remove it from the heap.
4. The remove method is trickier to write. 

Complexity:
----------
Time: O(N * K * log(K)). For N element of each array we are going to add them to the heap/delete them till K'th index in the current time window.
Space: O(K) At a time, there can be only K-elements in total in both heaps.

"""

import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.medians = []

    def find_sliding_window_median(self, nums, k):
        window_start = 0
        self.medians = [None] * (len(nums) - k + 1)
        for window_end in range(len(nums)):
            self.add_to_heap(nums[window_end])
            self.rebalance_heap()
            if window_end >= k - 1:
                self.medians[window_start] = self.calculate_median()
                if nums[window_start] <= -self.max_heap[0]:
                    self.remove(self.max_heap, -nums[window_start])
                else:
                    self.remove(self.min_heap, nums[window_start])
                self.rebalance_heap()
                window_start += 1

        return self.medians

    def add_to_heap(self, num):
        if len(self.max_heap) and num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

    def rebalance_heap(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def calculate_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return self.min_heap[0] / 1.0

    def remove(self, heap, element):
        ind = heap.index(element)  
        heap[ind] = heap[-1]
        del heap[-1]
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))


main()
