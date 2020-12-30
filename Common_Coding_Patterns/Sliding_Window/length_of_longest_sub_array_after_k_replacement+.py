"""
Problem
-------
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

For example:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Approach:
--------
Sliding Window with Variable Window Size + Use a HashMap to store frequency of input elements (Similar to length_of_longest_sub_array_after_k_replacement.py)

Complexity:
----------
Time: O(N)
Space: O(1) Because only 0 and 1s will be stored in the number_frequency dict

"""
def length_of_longest_sub_array_after_k_replacement(array, k):
    number_frequency = {}
    max_count_of_ones = 0
    max_length = 0
    window_start = 0
    for window_end in range(len(array)):
        right_number = array[window_end]
        if right_number not in number_frequency:
            number_frequency[right_number] = 0
        number_frequency[right_number] += 1
        max_count_of_ones = max(max_count_of_ones, number_frequency[right_number])

        if window_end - window_start + 1 - max_count_of_ones > k:
            left_number = array[window_start]
            number_frequency[left_number] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print(length_of_longest_sub_array_after_k_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_sub_array_after_k_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
