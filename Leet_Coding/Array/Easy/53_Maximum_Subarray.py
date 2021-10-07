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



sol = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray2(nums))
