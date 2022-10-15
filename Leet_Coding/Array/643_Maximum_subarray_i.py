"""
Complexity:
----------
Time: O(N)
Space: O(1)

"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        max_sum = 0
        for i in range(k):
            current_sum += nums[i]
        
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum -= nums[i - k] 
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k