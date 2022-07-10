"""
Complexity:
----------

Solution1
---------
Time: O(2^N)
Space: O(N)

Solution 2
----------
Time: O(N)
Space: O(N)

"""
class Solution1:
    def climbStairs(self, n: int) -> int:
        def helper(i, n):
            if i == n:
                return 1
            if i > n:
                return 0
            return helper(i + 1, n) + helper(i + 2, n)

        return helper(0, n)


class Solution2:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(i, n):
            nonlocal cache
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = helper(i + 1, n) + helper(i + 2, n)
            return cache[i]

        return helper(0, n)