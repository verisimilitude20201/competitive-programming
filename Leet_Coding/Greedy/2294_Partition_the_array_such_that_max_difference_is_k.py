"""
Complexity:
----------
Time: O(N log N)
Space: O(N) for Timsort in Python for Quicksort it's O(log N)
"""
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        x = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - x > k:
                x = nums[i]
                ans += 1
        return ans