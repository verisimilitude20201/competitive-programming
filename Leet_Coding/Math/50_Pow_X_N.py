"""
Complexity:
----------
Time: O(N)
Space: O(1)

"""
class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        if n == 0:
            return ans
        if n < 0:
            x = 1 / x
            n = -n
        for i in range(n):
            ans *= x
        return ans