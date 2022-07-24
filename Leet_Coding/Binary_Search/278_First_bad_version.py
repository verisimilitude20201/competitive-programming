"""
Explanation
-----------
n = 9

1 2 3 4 5 6 7 8 9
G G G G G B B B B
          L M   
            R 
Complexity:
----------
Time: O(log N)
Space: O(1)

"""

def isBadVersion(version: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            mid = left + ((right - left) // 2)
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        
        return left