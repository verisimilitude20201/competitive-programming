"""
Solution 1: moveZeroes1
------------------------
Time: O(N)
Space: O(1)

We use two pointers. 
1. For each non-zero element, we start assiging at index 0 of the array. We note the last index where the last non-zero number gets filled in.
2. We pre-fill the array of the array with 0s for len(array) - last_non_zero_found_at


Solution 2: moveZeroes2
-----------------------
Time: O(N)
Space: O(1)

For arrays with lots of zeroes, we move N elements. For example: [0,1,0,0,0]. Here if we just keep the non-zero element's position fixed to the left, we can achieve the same in
less than N operations, in this case just 1. Worst case complexity remains O(N) 

Note that since we're modifying array in-place, the space complexity is constant time. We are not allocating any auxillary memory.

"""
class SolutionZeroesRight:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for loop_counter in range(0, len(nums)):
            if nums[loop_counter] != 0:
                nums[last_non_zero_found_at] = nums[loop_counter]
                last_non_zero_found_at += 1

        while last_non_zero_found_at < len(nums):
            nums[last_non_zero_found_at] = 0
            last_non_zero_found_at += 1
    
    def moveZeroes2(nums) :
    last_non_zero_found_at = 0
    for loop_counter in range(0, len(nums)):
        if nums[loop_counter] != 0:
            nums[last_non_zero_found_at], nums[loop_counter] = nums[loop_counter], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

  

