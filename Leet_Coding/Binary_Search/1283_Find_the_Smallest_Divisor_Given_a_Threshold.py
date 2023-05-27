"""
Complexity:
----------
Time: O(N log K)
Space: O(N)
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            divisor = (left + right) // 2
            if self.is_divisor_total_less_than_threshold(divisor, nums, threshold):
                right = divisor - 1
            else:
                left = divisor + 1
        
        return left 
        
    def is_divisor_total_less_than_threshold(self, divisor, nums, threshold):
        total = 0
        for num in nums:
            total += (ceil(num / divisor))
        
        return total <= threshold