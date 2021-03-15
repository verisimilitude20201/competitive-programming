"""
Problem
-------
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.



Example:
-------
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted


0. [1, 3, 2, 0, -1, 7, 10]
    L                   R


1. [1, 3, 2, 0, -1, 7, 10]
     L                R

2. [1, 3, 2, 0, -1, 7, 10]
       L         R

   sub_array_min = -1
   sub_array_max = 3


3. [1, 3, 2, 0, -1, 7, 10]
    L            R

Approach
--------
Two pointers - starting at the first and last element

1. Find the misplaced (that are not sorted) indexes in the string
2. Find the maximum and minimum element in this window.
3. Extend the window such that
    a. If there is an element before the current left pointer thats greater than the minimum element, include it
    b. If there is an element after the right pointer that's less than the maximum element in the window, increment the right pointer.

Complexity:
----------
Time: O(N)
Space: O(1)


"""
import math

def shortest_window_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < len(arr) - 1 and arr[left] < arr[left + 1]:
        left += 1
    if left == right:
        return 0

    while right >= 0 and arr[right] > arr[right - 1]:
        right -= 1
    subarray_min = math.inf
    subarray_max = -math.inf
    for i in range(left, right + 1):
        subarray_min = min(subarray_min, arr[left])
        subarray_max = max(subarray_max, arr[left])

    while left >= 0 and arr[left - 1] > subarray_min:
        left -= 1

    while right < len(arr) - 1 and arr[right + 1] < subarray_max:
        right += 1

    return right - left + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))

main()
