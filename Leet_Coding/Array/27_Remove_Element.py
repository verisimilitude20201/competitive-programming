"""
Complexity:
---------
Time: O(N)
Space: O(1)

"""
class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i
    
    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            while nums[j] == val:
                nums[j] = None
                j -= 1
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j] = None
                j -= 1
            i += 1

        return j + 1