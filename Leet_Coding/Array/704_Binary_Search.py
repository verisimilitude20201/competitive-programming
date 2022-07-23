"""
Complexity:
----------
Time: O(log N)
Space: O(log N)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search_recursive(nums, target, 0, len(nums) - 1)
    
    def binary_search_recursive(self, nums: List[int], target: int, low: int, high: int) -> int:
        if low > high:
            return -1
        
        mid = low + ((high - low) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search_recursive(nums, target, mid + 1, high)
        else:
            return self.binary_search_recursive(nums, target, low, mid - 1)