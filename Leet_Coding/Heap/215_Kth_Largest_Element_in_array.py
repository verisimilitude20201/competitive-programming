"""
Complexity:
---------
Time: O(N Log K)
Space: O(K)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap, nums[i])
        
        for j in range(k, len(nums)):
            if min_heap[0] <= nums[j]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[j])
        
        return min_heap[0]