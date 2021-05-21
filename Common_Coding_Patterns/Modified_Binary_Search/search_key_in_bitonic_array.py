"""
Problem:
-------
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1]

Example:
-------
Input: [1, 3, 8, 4, 3], key=4
Output: 3

Approach:
--------
1. Find the max_index i.e index of the maximum element first in the Bitonic array.
2. Apply individual binary search on the two array segments i.e (0, max_index) & (max_index + 1, len(arr) - 1)


Complexity:
----------
Time: O(3 log N) ~ O(log N)
Time: O(1)

"""

def search_bitonic_array(arr, key):
    max_index = find_max_index(arr)
    key_index = find_key_by_binary_search(arr, 0, max_index, key)
    if key_index == -1:
        key_index = find_key_by_binary_search(arr, max_index, len(arr) - 1, key)

    return key_index


def find_max_index(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return low


def find_key_by_binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
