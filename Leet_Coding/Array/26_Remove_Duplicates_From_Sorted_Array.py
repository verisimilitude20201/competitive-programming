"""
Complexity:
-----------
Time: O(N)
Space: O(1)

"""
from typing import List


class Solution:
    def removeDuplicates1(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
            nums[i] = nums[j]

        return i + 1
    
    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums)  and nums[i] == nums[j]:
                j += 1
            if j  == len(nums):
                break
            nums[i + 1] = nums[j]
            i += 1

        return i + 1


sol = Solution()
#nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
