"""
Complexity:
----------

Solution1
---------
Time: O(N log N)
Space: O(1)


Solution 2
---------
Time: O(N)
Space: O(N)

Solution 3
----------
Time: O(N)
Space: O(1)

"""
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        elif nums[-1] != len(nums):
            return len(nums)
            
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if expected_num != nums[i]:
                return expected_num

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = (len(nums) * (len(nums) + 1)) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum