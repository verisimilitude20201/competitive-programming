"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentMax = 0
        currentMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = 0
        for num in nums:
            currentMax = max(currentMax, 0) + num
            maxSum = max(currentMax, maxSum)

            currentMin = min(currentMin, 0) + num
            minSum = min(minSum, currentMin)

            totalSum += num

        if totalSum == minSum:
            return maxSum

        return max(maxSum, totalSum - minSum)