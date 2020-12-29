"""
Problem: 
-------
Given an array as input, extract the sub-array of K contiguous integers that have the highest sum. Return the highest sum

Approach
--------
Sliding Window - Constant Window Size

Complexity:
----------
Time: O(N)
Space: O(1)

"""
def max_sum_of_sub_array_of_size_k(K, array):
    max_sum = 0
    window_start = 0
    total_sum = 0

    for window_end in range(len(array)):
        total_sum += array[window_end]
        if window_end >= K - 1:
            max_sum = max(max_sum, total_sum)
            total_sum -= array[window_start]
            window_start += 1

    return max_sum


print("Maximum sum of a subarray of size K: " + str(max_sum_of_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
print("Maximum sum of a subarray of size K: " + str(max_sum_of_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
