"""
Complexity:
----------
Time: O(N * 2^N)
Space: O(N)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(current, i):
            if i > len(nums):
                return
            ans.append(current[:])
            for j in range(i, len(nums)):
                current.append(nums[j])
                backtrack(current, j + 1)
                current.pop()

        backtrack([], 0)
        return ans