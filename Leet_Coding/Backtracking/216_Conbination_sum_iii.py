"""
Complexity:
----------
Time: O(9!* K / (9 - K) !)
Space: O(K)
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(remaining_sum, comb, start_from):
            if len(comb) == k and remaining_sum == 0:
                result.append(comb[:])
                return
            
            if len(comb) == k:
                return
            
            for i in range(start_from, 9):
                comb.append(i + 1)
                backtrack(remaining_sum - i - 1, comb, i + 1)
                comb.pop()
        backtrack(n, [], 0)
        
        return result