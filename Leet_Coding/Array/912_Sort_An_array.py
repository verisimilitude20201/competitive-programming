"""
Complexity:
----------
Time: O(N + K)
Space: O(N)
"""
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        min_val = min(nums)
        counts = {}
        for num in nums:
          counts[num] = counts.get(num, 0) + 1

        index = 0
        for num in range(min_val, max_val + 1, 1):
          while counts.get(num, 0) > 0:
            nums[index] = num
            index += 1
            counts[num] -= 1

        return nums