"""
Problem:
-------
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Example:
-------
Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Input: [10, 9, 8]
Output: 10

Input: [1, 3, 8, 12]
Output: 12

Approach:
---------
find_maximum_in_bitonic_arr1
----------------------------
1. Try to compare the middle element with the middle + 1 element. 
    - If middle element < middle + 1, the required number may be after middle. Move low to middle + 1
    - If middle element > middle + 1, the required number will be before middle. Move high to middle.

2. Stop process when high becomes low.

find_maximum_in_bitonic_arr2
---------------------------
Simple iteration that stops when we find an element that is greater than its sucessor. That is the peak (maximum)

Complexity:
----------
Time: O(log N)
Space: O(1)

Time: O(N)
Space: O(1)

"""

import math


def find_maximum_in_bitonic_arr1(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


def find_maximum_in_bitonic_arr2(arr):
    i = 0
    while i < len(arr) and arr[i] < arr[i+1]:
        i += 1
    return arr[i]


def main():
    print(find_maximum_in_bitonic_arr1([1, 3, 8, 12, 4, 2]))
    print(find_maximum_in_bitonic_arr1([3, 8, 3, 1]))
    print(find_maximum_in_bitonic_arr1([1, 3, 8, 12]))
    print(find_maximum_in_bitonic_arr1([10, 9, 8]))

    print(find_maximum_in_bitonic_arr2([1, 3, 8, 12, 4, 2]))


main()
