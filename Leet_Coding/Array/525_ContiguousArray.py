"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        counts = {}
        for i, num in enumerate(nums):
            count += (-1 if num == 0 else 1)
            if count == 0:
                max_length = i + 1
            elif count in counts:
                max_length = max(max_length, i - counts[count])
            else:
                counts[count] = i
        
        return max_length