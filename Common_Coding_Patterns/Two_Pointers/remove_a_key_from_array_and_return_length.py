"""
Problem
-------
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array

Example:
-------
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9]


Approach
-------
Two Pointers

1. Similar to remove_duplicates_and_return_length_of_array2


Complexity
---------
    Time: O(N) 
    Space: O(1)
"""
def remove_a_key_from_array_and_return_length(arr, key):
    if len(arr) == 0:
        return 0

    last_non_key_index = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[last_non_key_index] = arr[i]
            last_non_key_index += 1

    return last_non_key_index


def main():
    print(remove_a_key_from_array_and_return_length([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_a_key_from_array_and_return_length([2, 11, 2, 2, 1], 2))

main()
