"""
Complexity:
----------
Time: O(S) Where N is the size of stones
Space: O(J) Where J is the size of Jewels.
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count