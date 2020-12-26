"""
Problem: 
-------
Given an array as input, extract the sub-array of K contiguous integers that have the highest sum. Return the highest sum

Complexity:
----------
Time: O(N)
Space: O(1)

"""
def compute_maximum_sum_of_subarray_of_size_k(array, K):
    max_sum = 0
    window_start = 0
    current_sum = 0
    for window_end in range(len(array)):
        current_sum += array[window_end]
        if window_end >= K - 1:
            max_sum = max(max_sum, current_sum)
            current_sum -= array[window_start]
            window_start += 1

    return max_sum


print(compute_maximum_sum_of_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3))
