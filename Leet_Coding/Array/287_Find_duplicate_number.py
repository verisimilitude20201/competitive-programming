"""
Complexity:
----------
Solution 1 -- Sorting
--------------------
Time: O(N log N)
Space: O(log N) / O(N) Python uses Timsort

Solution 2 -- Set
--------------------
Time: O(N)
Space: O(N) / O(N) Python uses Timsort

Solution 3 - Negative Mark
--------------------
Time: O(N)
Space: O(1) 

Solution 4 - Binary Search
--------------------
Time: O(N)
Space: O(1) 

"""
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                duplicate = abs(num)
            nums[index] *= -1

        for i in range(len(nums)):
            num = abs(nums[i])
            nums[i] = num

        return duplicate

class Solution4:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        duplicate = -1
        while low <= high:
            current = (low + high) // 2
            count = 0
            count = sum(num <= current for num in nums)
            if count > current:
                duplicate = current
                high = current - 1
            else:
                low = current + 1
        
        return duplicate