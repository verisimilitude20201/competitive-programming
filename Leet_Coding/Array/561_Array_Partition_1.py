"""
Complexity:
----------
O(N * log N)
"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums.sort()
        i = 0
        while i < len(nums):
            total += nums[i]
            i += 2
        return total