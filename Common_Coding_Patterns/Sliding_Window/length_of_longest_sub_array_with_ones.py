
"""
Problem
-------
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s

Example:
-------
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6


Approach
-------
Sliding Window containing longest sub-array having all 1s
Sliding window will change if 
Current length of window (window_end - window_start + 1) - max_count_of_repeated_ones > Number of zeroes to be replaced (K)

length_of_longest_sub_array_with_ones2 is an optimized version of length_of_longest_sub_array_with_ones1 wherein we replace the hash table with a simple variable.
 
Complexity
---------
    Time: O(N) N is the length of the array
    Space: O(1) We're just tracking the frequency of 1s in the hash table.
"""
def length_of_longest_sub_array_with_ones1(arr, k):
    window_start, max_count_of_repeated_ones, max_length = 0, 0, 0
    one_freq = {}
    for window_end in range(len(arr)):
        right_int = arr[window_end]
        if right_int == 1:
            if right_int not in one_freq:
                one_freq[right_int] = 0
            one_freq[right_int] += 1
            max_count_of_repeated_ones = max(max_count_of_repeated_ones, one_freq[right_int])
        while window_end - window_start + 1 - max_count_of_repeated_ones > k:
            left_int = arr[window_start]
            if left_int == 1:
                one_freq[left_int] -= 1
                if one_freq[left_int] == 0:
                    del one_freq[left_int]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

def length_of_longest_sub_array_with_ones2(arr, k):
    window_start, max_count_of_repeated_ones, max_length = 0, 0, 0
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_count_of_repeated_ones += 1
        while window_end - window_start + 1 - max_count_of_repeated_ones > k:
            if arr[window_start] == 1:
                max_count_of_repeated_ones -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print(length_of_longest_sub_array_with_ones1([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_sub_array_with_ones1([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()