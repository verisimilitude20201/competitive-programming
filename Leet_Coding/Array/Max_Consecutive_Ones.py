"""
Explanation:
-----------
Use two pointers. 

Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_end = window_start = 0
        max_number_of_ones = 0
        while window_end < len(nums):
            while window_end < len(nums) and nums[window_end] == 1:
                window_end += 1
            max_number_of_ones = max(max_number_of_ones, window_end - window_start)
            window_end += 1
            window_start = window_end
        return max_number_of_ones