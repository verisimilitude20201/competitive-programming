"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        running_sums = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            running_sums.append(total)

        return running_sums