"""
Complexity for both top-down and bottom-up:
-------------------------------------------
Time: O(N)
Space: O(N)
"""
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[len(nums) - 1]

class Solution2:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return cache[i]
        
        return dp(len(nums) - 1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # To avoid out of bounds error from setting base case
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)

        # Base cases
        back_two = nums[0]
        back_one = max(nums[0], nums[1])
        
        for i in range(2, n):
            # back_two becomes back_one, and back_one gets updated
            back_one, back_two = max(back_one, back_two + nums[i]), back_one

        return back_one