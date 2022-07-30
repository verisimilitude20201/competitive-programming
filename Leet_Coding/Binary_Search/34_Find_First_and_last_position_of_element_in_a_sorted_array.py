"""
Complexity:
---------
Time: O(log N)
Space: O(1)

"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return [-1, -1]

        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        start_index = self.findIndex(nums, target, True)
        end_index = self.findIndex(nums, target, False)

        return [start_index, end_index]

    def findIndex(self, nums, target, is_first) -> int:
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = begin + ((end - begin) // 2)
            if nums[mid] == target:
                if is_first:
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1

            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1

        return -1