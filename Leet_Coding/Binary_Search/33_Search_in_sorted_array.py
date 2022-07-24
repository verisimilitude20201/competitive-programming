"""
Explanation:
-----------
1. Check whether the left part is sorted i.e. check if middle element is greater than 0th element
2. If the left part is not sorted, then the right part must be sorted

Complexity:
----------
Time: O(log N)
Space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1