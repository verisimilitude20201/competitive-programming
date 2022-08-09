"""
Complexity:
----------
Time: O(log(N))
Space: O(1)
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        low = 2
        high = num // 2
        while low <= high:
            mid = low + ((high - low) // 2)
            mid_squared = mid * mid
            if mid_squared == num:
                return True
            elif mid_squared < num:
                low = mid + 1
            else:
                high = mid - 1
        return False