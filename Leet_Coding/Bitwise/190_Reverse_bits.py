"""
Complexity:
----------
Time: O(1)
Space: O(1)
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += ((n & 1) << power)
            n >>= 1
            power -= 1
        return ret