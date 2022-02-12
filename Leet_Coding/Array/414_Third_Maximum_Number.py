"""
Explanation:
-----------
1. thirdMax1: Convert the elements into a set to eliminate duplicates and take max 3 times. 
Remove the two top max numbers from set.

2. thirdMax2: Use a set to keep track of the maximum elements already been seen. Try computing the 
maximum 3 times. 

Complexity:
----------
thirdMax1
---------
Time: O(N)
Space: O(N)

thirdMax2
---------
Time: O(N)
Space: O(N)

thirdMax3
--------
Time: O(N)
Space: O(1)

"""
class Solution:
    def thirdMax1(self, nums: List[int]) -> int:
        nums = set(nums)
        max_num = max(nums)
        if len(nums) <= 2:
            return max_num
        nums.remove(max_num)
        second_max = max(nums)
        nums.remove(second_max)
        return max(nums)
    
    def thirdMax2(self, nums: List[int]) -> int:
        seen_maximums = set()
        for _ in range(3):
            maximum = self.getUnseenMaximum(nums, seen_maximums)
            if maximum is None:
                return max(seen_maximums)
            seen_maximums.add(maximum)

        return min(seen_maximums)

    def getUnseenMaximum(self, nums: List[int], seen_maximums: set[int]) -> int:
        maximum = None
        for num in nums:
            if num in seen_maximums:
                continue
            if maximum is None or num > maximum:
                maximum = num
        return maximum

    def thirdMax3(self, nums: List[int]) -> int:
        seen_maximums = set()
        for num in nums:
            seen_maximums.add(num)
            if len(seen_maximums) > 3:
                seen_maximums.remove(min(seen_maximums))
        if len(seen_maximums) < 3:
            return max(seen_maximums)
        return min(seen_maximums)