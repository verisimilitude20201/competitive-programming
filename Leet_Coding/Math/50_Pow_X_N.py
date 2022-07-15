"""
Complexity:
----------
Solution 1
---------
Time: O(N)
Space: O(1)

Solution2
---------
Time: O(log2N)
Space: O(log2N)
"""
class Solution1(object):
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

class Solution2:
    def fast_pow(self, x: int, n: int) -> int:
        if n == 0:
            return 1.0
        half = self.fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x  = 1 / x
            n = -n
        return fast_pow(x, n)