"""
Complexity:
----------
Time: O(N^(T/M)) Where M = min(candidates), N = len(candidates), T = target
Space: O(T/M)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(path, start_index, current_sum):
            if current_sum == target:
                ans.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                num = candidates[i]
                if num + current_sum <= target:
                    path.append(num)
                    backtrack(path, i, num + current_sum)
                    path.pop()
        backtrack([], 0, 0)
        return ans