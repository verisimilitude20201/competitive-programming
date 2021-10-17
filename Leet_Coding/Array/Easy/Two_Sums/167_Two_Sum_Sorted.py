"""
Complexity:
----------
twoSums1 --> 2 Pointers
----------------------
Time: O(N)
Space: O(1)

twoSum --> Binary Search
----------------------
Time: O(N log N)
Space: O(log N)
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices_adding_to_target = [-1, -1]
        for i in range(len(numbers)):
            second_num = target - numbers[i]
            second_index = self.search_num(numbers, second_num, i + 1, len(numbers) - 1)
            if second_index != -1:
                indices_adding_to_target = [i + 1, second_index + 1]
                break

        return indices_adding_to_target

    def search_num(self, numbers, target, low, high):
        if low > high:
            return -1

        mid = low + ((high - low) // 2)
        if numbers[mid] == target:
            return mid

        if numbers[mid] < target:
            return self.search_num(numbers, target, mid + 1, high)
        elif numbers[mid] > target:
            return self.search_num(numbers, target, low, mid - 1)

        return -1
    
    def twoSums1(self, numbers: List[int], target: int):
        left = 0
        right = len(numbers) - 1
        while left <= right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]
    
    
    
