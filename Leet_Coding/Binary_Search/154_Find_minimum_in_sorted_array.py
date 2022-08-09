"""
Complexity:
----------
Time: O(log N). Since this can have duplicate elements, the complexity can go to O(N)
Space: O(1)

"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + ((high - low) // 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        
        return nums[low]