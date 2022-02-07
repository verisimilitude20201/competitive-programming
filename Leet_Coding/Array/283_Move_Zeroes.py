"""
Explanation:
-----------
i Tracks the current element
j Tracks non-zero elements from i and swaps if nums[i] = 0 and nums[j] != 0. 
j is always to the right of i and the resulting action moves 0s to the right

Complexity:
----------
moveZeroes1
-----------
Time: O(N)
Space: O(1)

moveZeroes2
-----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j >= len(nums):
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        
        return nums
    
    class Solution:
        def moveZeroes2(self, nums: List[int]) -> None:
            ans = []
            count_zeroes = 0
            for num in nums:
                if num == 0:
                    count_zeroes += 1
                else:
                    ans.append(num)