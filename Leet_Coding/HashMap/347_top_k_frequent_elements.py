"""
Complexity:
----------
Solution 1
----------
Time: O(N log K) --> 
    O(N) for creating hashmap of frequencies
    O(K) for adding first K elements to heap.
    O((N - K) log K) for pushing and popping N - K elements from the Heap
    O(K log K) for populating the list with nLargest

This is average case, can be K = N for worst case and so O(N log N) When K = N

Space: O(log K + N) ---> 
   K = Heap size
   N = Number of elements in list.
"""
import heapq
from collections import Counter

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        num_freq = Counter(nums)
        return heapq.nlargest(k, num_freq.keys(), key=num_freq.get)