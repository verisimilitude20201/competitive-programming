"""
Complexity:
---------
Time:O(N log N)
Space: O(N/log N)
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_difference = -math.inf
        for i in range(len(nums) - 1):
            max_difference = max(nums[i + 1] - nums[i], max_difference)
        
        return max_difference