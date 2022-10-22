"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_frequency = defaultdict(int)
        for num in nums:
            num_frequency[num] += 1
        
        max_unique_number = -1
        for num in num_frequency:
            if num_frequency[num] == 1:
                max_unique_number = max(max_unique_number, num)
        
        return max_unique_number