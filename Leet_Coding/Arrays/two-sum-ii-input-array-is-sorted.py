"""
This is similar to two-sums.py. The only difference is we are incrementing loop counter by 1.
Since either index1 or index2 should not be zero.

Time complexity O(N), Space complexity: O(1)

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = nums
        map_difference_to_index = {}
        for loop_counter in range(0, len(A)):
            difference = target - A[loop_counter]
            if A[loop_counter] in map_difference_to_index:
                diff_indexes = map_difference_to_index[A[loop_counter]]
                diff_indexes.append(loop_counter + 1)
                return diff_indexes
            map_difference_to_index[difference] = [loop_counter + 1]