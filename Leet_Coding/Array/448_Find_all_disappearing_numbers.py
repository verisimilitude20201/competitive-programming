"""
Complexity:
----------
findDisappearedNumbers1
----------------------
Time: O(N)
Space: O(N)

findDisappearedNumbers2
-----------------------
Time: O(N)
Space: O(1) excluding the space for output list
"""
from typing import List

class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = {i for i in range(1, n + 1)}
        for num in nums:
            if num in num_set:
                num_set.remove(num)

        return list(num_set)
    
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        for num in nums:
            new_index = abs(num) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        disappearing_nums = []
        for i in range(len(nums)):
            if nums[i] > 0:
                disappearing_nums.append(i + 1)
        return disappearing_nums


solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(solution.findDisappearedNumbers([1, 1]))



