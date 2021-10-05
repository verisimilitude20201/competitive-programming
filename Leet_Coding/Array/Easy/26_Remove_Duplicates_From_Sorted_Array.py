"""
Complexity:
-----------
Time: O(N)
Space: O(1)

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
            nums[i] = nums[j]

        return i + 1


sol = Solution()
#nums = [1, 1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
