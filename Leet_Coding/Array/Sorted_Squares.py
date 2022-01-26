"""
Complexity:
----------
Time: O(N)
Space: O(N)

Tip:
---
Instead of comparing squares, we can just compare the absolute values of the left and right pointed elements.

"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums_length = len(nums)    
        squares = [None] * nums_length
        left = 0
        right = nums_length - 1
        square_ptr = nums_length - 1
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square <= right_square:
                squares[square_ptr] = right_square
                right -= 1
            else:
                squares[square_ptr] = left_square
                left += 1
            square_ptr -= 1
        return squares