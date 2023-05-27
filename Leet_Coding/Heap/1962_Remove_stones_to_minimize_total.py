"""
Complexity:
----------
Time: O(N log N + K log N)
Space: O(N)
"""
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k > 0:
            num = -heapq.heappop(piles)
            num -= floor(num/2)
            heapq.heappush(piles, -num)
            k -= 1
        piles = [-pile for pile in piles]
        return sum(piles)