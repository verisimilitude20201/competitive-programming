"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        product = 1
        count = 0
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            count += (right - left + 1)
        
        return count