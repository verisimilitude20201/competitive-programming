"""
Complexity:
----------
Solution 1
----------
Time: O(N)
Space: O(1)

"""

class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size  = math.inf
        window_start = 0
        window_end = 0
        min_size = math.inf
        running_sum = 0
        while window_end < len(nums):
            running_sum += nums[window_end]
            while running_sum >= target:
                min_size = min(min_size, window_end - window_start + 1)
                running_sum -= nums[window_start]
                window_start += 1
            window_end += 1

        if min_size == math.inf:
            return 0

        return min_size