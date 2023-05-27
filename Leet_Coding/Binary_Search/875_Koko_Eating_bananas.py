"""
Complexity:
----------
Time: O(P log N) Where N = MAX(Piles), P is number of piles 
Space: O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in pile:
                hours += math.ceil(p / mid)
            if hours <= h:
                result = min(k, result)
                right = mid - 1
            else:
                left = mid + 1
        return result