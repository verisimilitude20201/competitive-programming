"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start = 0
        window_end = 0
        max_ones = 0
        zeroes = 0
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[window_start] == 0:
                    zeroes -= 1
                window_start += 1
            max_ones = max(window_end - window_start + 1, max_ones)

        return max_ones