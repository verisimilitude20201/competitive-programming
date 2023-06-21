"""
Complexity:
----------
Time: O(1)
Space: O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n1 = n
        while n1:
            count += (n1 & 1)
            n1 >>= 1
        
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n1 = n
        while n1:
            count += 1
            n1 &= (n1 - 1)
        return count
        