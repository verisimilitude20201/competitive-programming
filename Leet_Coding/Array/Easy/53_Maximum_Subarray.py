"""
Explanation:
-----------
maxSubArray1 --> Not feasible for larger arrays. 
maxSubArray2 --> We keep track of current_sum only if its greater than the current sum

Complexity:
----------
maxSubArray1 -->
    Time: O(N^2)
    Space: O(1)

maxSubArray2 -->
    Time: O(N)
    Space: O(1)

maxSubArray3 --> Divide and conquer
    Time: O(N log N)
    Space: O(N)

maxSubArray4 -> Dynamic Programming

"""
from typing import List
import math

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        max_sub_array_sum = -math.inf
        for i in range(len(nums)):
            current_sub_array_sum = 0
            for j in range(i, len(nums)):
                current_sub_array_sum += nums[j]
                max_sub_array_sum = max(max_sub_array_sum, current_sub_array_sum)

        return max_sub_array_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        current_sub_array_sum = nums[0]
        max_sub_array_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            current_sub_array_sum = max(num, current_sub_array_sum + num)
            max_sub_array_sum = max(max_sub_array_sum, current_sub_array_sum)

        return max_sub_array_sum
    
    def maxSubArray3(self, nums: List[int]) -> int:
        def max_sub_array_recursive(self, nums: List, left, right):
            if left > right:
                return -math.inf

            left_sum = right_sum = current_sum = 0
            mid = left + ((right - left) // 2)
            for i in range(left, mid):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)

            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)

            best_combined_sum = nums[mid] + right_sum + left_sum

            left_half = self.max_sub_array_recursive(nums, left, mid - 1)
            right_half = self.max_sub_array_recursive(nums, mid + 1, right)

            return max(best_combined_sum, left_half, right_half)
        return max_sub_array_recursive(nums, 0, len(nums) - 1)
    
    def maxSubArray4(self, arr: List) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]
        max_sum = dp[0]

        for i in range(1, n):
            dp[i] = arr[i] + (0 if dp[i - 1] <= 0 else dp[i - 1])
            max_sum = max(max_sum, dp[i])

        return max_sum



sol = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray2(nums))
