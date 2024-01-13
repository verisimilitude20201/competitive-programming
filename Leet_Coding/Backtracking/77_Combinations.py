"""
Complexity:
---------
Time: O(n! / (k - 1)! * (n - k)! )
Space: O(k)
"""

class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(current, i):
            if len(current) == k:
                ans.append(current[:])
                return
            
            for num in range(i, n + 1):
                current.append(num)
                backtrack(current, num + 1)
                current.pop()
        
        backtrack([], 1)
        return ans




class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(current, num):
            if len(current) == k:
                ans.append(current[:])
                return

            need = k - len(current)
            remain = n - num + 1
            availaible = remain - need

            for i in range(num, availaible + 1 + num):
                current.append(i)
                backtrack(current, i + 1)
                current.pop()

        backtrack([], 1)
        return ans
        