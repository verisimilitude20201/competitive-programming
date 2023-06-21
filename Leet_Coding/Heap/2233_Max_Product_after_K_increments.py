"""
Complexity:
----------
Time: O(N log N)
Space: O(N)

"""
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap = []
        j = 10**9 + 7
        for num in nums:
            heapq.heappush(heap, num)

        while k > 0:
            num = heapq.heappop(heap)
            heapq.heappush(heap, num + 1)
            k -= 1
        
        max_product = 1
        while heap:
            max_product = (max_product * heapq.heappop(heap)) % j
        
        return max_product