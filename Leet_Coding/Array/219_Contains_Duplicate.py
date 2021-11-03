"""
Similar Problems: ["https://leetcode.com/problems/contains-duplicate-ii/", "https://leetcode.com/problems/contains-duplicate-iii/"]

Complexity:
----------
containsDuplicate1:
    Time: O(N)
    Space: O(N)

containsDuplicate2:
    Time: O(N log N)
    Space: O(1)
"""
class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in set:
                return True
            s.add(num)

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return True
            return False

        return False