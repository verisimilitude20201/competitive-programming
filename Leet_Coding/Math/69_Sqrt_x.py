"""
Complexity:
---------
Solution 1
---------
Time: O(log N)
Space: O(1)
"""

class Solution1:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 2
        right = x // 2
        while left <= right:
            pivot = left + ((right - left) // 2)
            num = pivot * pivot
            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot
        
        return right