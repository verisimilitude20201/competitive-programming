"""
Complexity:
-----------
Time: O(log N)
Space: O(1)~
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + ((high - low) // 2)
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1