"""
Complexity:
----------

findTargetSumWays1
------------------
Time: O(2^N)
Space: O(N)
"""
class Solution:
    def __init__(self) -> None:
        self.count = 0
    
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        self.calculate(nums, 0, 0, target)
        return self.count
    
    def calculate(self, nums: List[int], i: int, total: int, target: int) -> None:
       if i == len(nums):
           if total == target:
               self.count += 1
           return
       self.calculate(nums, i + 1, total + nums[i], target)
       self.calculate(nums, i - 1, total - nums[i], target)