"""
Explanation:
-----------
Two pointers, i tracks the odd elements in the first part of the array, j tracks the event elements in the later half of the array.

Complexity:
----------
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        i = 0
        while i < len(nums):
            if nums[i] % 2 != 0:
                j = i + 1
                while j < len(nums) and nums[j] % 2 != 0:
                    j += 1
                if j > len(nums) - 1:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1

        return nums



solution = Solution()
print(solution.sortArrayByParity([3,1,2,4]))


