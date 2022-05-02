"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_index = 0
        max_num = nums[0]
        for i, x in enumerate(nums):
            if x > max_num:
                max_num = x
                max_index = i

        for i, x in enumerate(nums):
            if i != max_index and max_num < 2 * x:
                return -1

        return max_index