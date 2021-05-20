"""
Problem
--------
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. 
The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example:
-------
Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Approach:
--------
1. If a key is found at mid, we need to move forward to find it's end index and back-ward to find it's start index.
2. If the start index is not found, we don't compute the end index and straightway return [-1, -1]

Complexity:
----------
Time: O(log N)
Space: O(1)
"""

def find_range(arr, key):
    key_range = [-1, -1]
    key_start_index = find_key_by_binary_search(arr, key, False)
    if key_start_index == -1:
        return [-1, -1]
    key_end_index = find_key_by_binary_search(arr, key, True)
    return [key_start_index, key_end_index]


def find_key_by_binary_search(arr, key, is_search_forward):
    low = 0
    high = len(arr) - 1
    key_index = -1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            key_index = mid
            if is_search_forward:
                low = mid + 1
            else:
                high = mid - 1

    return key_index


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
