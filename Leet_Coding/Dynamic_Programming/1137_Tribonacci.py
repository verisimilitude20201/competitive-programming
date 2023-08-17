"""
Complexity:
----------
Solution 1
----------
Time: O(N)
Space: O(N)

Solution 2
----------
Time: O(N)
Space: O(N)


"""
class Solution1:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def dp(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            
            if i in cache:
                return cache[i]
            
            ans = dp(i - 3) + dp(i - 1) + dp(i - 2)
            cache[i] = ans
            
            return cache[i]
        
        return dp(n)

class Solution2:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        ans = [0] * (n + 1)
        ans[1] = ans[2] = 1
        for i in range(3, n + 1):
            ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]
        
        return ans[n]


class Solution3:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            tmp = a + b + c
            a = b 
            b = c
            c = tmp
        return c
        
        