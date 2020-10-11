"""

Time complexity: O(N), space complexity O(N)

Algorithm

A = Array
target = current sum
map_difference_to_index  = Dictionary that maps difference to index. It will contain a list of indexes whenever the two numbers that sum up to 'target' 

1. Loop array from 1 to N
    1.1 Difference = target - current_element
    1.2 if current_element is in dictionary 'map_difference_to_index'
        1.2.1 Append current loop_counter to it
        1.2.2 Return this list

    1.3 map_difference_to_index[difference] = [loop_counter]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = nums
        map_difference_to_index = {}
        for loop_counter in range(0, len(A)):
            difference = target - A[loop_counter]
            if A[loop_counter] in map_difference_to_index:
                diff_indexes = map_difference_to_index[A[loop_counter]]
                diff_indexes.append(loop_counter)
                return diff_indexes
            map_difference_to_index[difference] = [loop_counter]