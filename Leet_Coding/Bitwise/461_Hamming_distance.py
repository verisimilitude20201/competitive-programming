"""
Complexity:
----------
Time: O(1)
Space: O(1)
"""
class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        return bin(xor).count('1')


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            if xor & 1 != 0:
                distance += 1
            xor = xor >> 1
        
        return distance