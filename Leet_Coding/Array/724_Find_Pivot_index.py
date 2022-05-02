class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)
        for i, x in enumerate(nums):
            if left_sum == total - nums[i] - left_sum:
                return i
            left_sum += x
        return -1