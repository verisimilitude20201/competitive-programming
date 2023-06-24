"""
Complexity:
----------
Time: O(1)
Space: O(1)
"""
class Solution1:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        m, n = left, right
        while m < n:
            m >>= 1
            n >>= 1
            shift += 1
        
        return m << shift

class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        m, n = left, right
        while m < n:
            n = (n & ( n - 1))
        
        return m & n