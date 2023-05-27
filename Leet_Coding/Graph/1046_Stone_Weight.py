"""
Complexity:
----------
Time: O(N log N)
Space: O(N)
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first_max = abs(heapq.heappop(stones))
            second_max = abs(heapq.heappop(stones))
            if first_max != second_max:
                heapq.heappush(stones, -abs(first_max - second_max))
        
        return abs(stones[0]) if stones else 0

        