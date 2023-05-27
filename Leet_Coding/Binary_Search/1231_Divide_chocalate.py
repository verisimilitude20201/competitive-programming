"""
Complexity:
---------------
Time: O(N * (S/(K + 1)))
Space: O(1)
"""
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        while left < right:
            mid = (left + right + 1) // 2
            current_sweetness = 0
            pieces = 0
            for s in sweetness:
                current_sweetness += s
                if current_sweetness >= mid:
                    current_sweetness = 0
                    pieces += 1
            if pieces >= k + 1:
                left = mid
            else:
                right = mid - 1
                
        return left