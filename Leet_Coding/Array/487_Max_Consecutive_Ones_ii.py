
"""
Explanation:
-----------
Two Pointers

 0  1  2  3  4  5  6
[1, 0, 0, 1, 1, 0, 1], zero_count = 1,  longest_seq = 4
 L
    R 

Complexity:
----------
findMaxConsecutiveOnes1
-----------------------
Time: O(N^2)
Space: O(1)

findMaxConsecutiveOnes2
----------------------
Time: O(N)
Space: O(1)
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        longest_sequence = 0
        for left in range(len(nums)):
            zero_count = 0
            for right in range(left, len(nums)):
                if nums[right] == 0:
                    zero_count += 1
                if zero_count > 1:
                    break
                if zero_count <= 1:
                    longest_sequence = max(longest_sequence, right - left + 1)

        return longest_sequence
    
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        left, right = 0, 0
        zero_count = 0
        longest_seq = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            longest_seq = max(longest_seq, right - left + 1)     
            right += 1
        return longest_seq


solution = Solution()
# print(solution.findMaxConsecutiveOnes([1,0,1,1,0]))
print(solution.findMaxConsecutiveOnes([1,1,0,1]))
# print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))

