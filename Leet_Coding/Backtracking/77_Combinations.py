class Solution:
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
        