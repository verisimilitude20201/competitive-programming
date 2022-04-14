"""
Complexity:
----------
findTargetSumWays1
------------------
Time: O(2^N)
Space: O(N)

"""
from typing import List

class Solution:
    def __init__(self):
        self.count = 0
        self.complexity = 0

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        self.calculate(nums, 0, 0, target)

        return self.count

    def calculate(self, nums: List[int], i: int, total: int, target: int) -> int:
        self.complexity += 1
        if i == len(nums):
            if total == target:
                self.count += 1
        else:
            self.calculate(nums, i + 1, total + nums[i], target)
            self.calculate(nums, i + 1, total - nums[i], target)


solution = Solution()
print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(solution.complexity)