"""
Problem:
--------
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’

Example:
-------
Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

Approach:
--------
Modified binary search. Every time check difference between the key and the middle element.

If difference < arr[mid], look in first half else look in second half of list.

Complexity:
----------
Time: O(log N)
Space: O(1)
"""


import math


def search_min_diff_element(arr, key):
    min_difference = math.inf
    low = 0
    high = len(arr) - 1
    min_difference_element = -1
    while low <= high:
        mid = low + (high - low // 2)
        current_difference = abs(arr[mid] - key)
        if current_difference < min_difference:
            min_difference = current_difference
            min_difference_element = arr[mid]
        if current_difference <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return min_difference_element


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
