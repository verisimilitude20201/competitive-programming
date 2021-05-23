"""
Problem:
-------
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
You can assume that the array does not have any duplicates.

Example:
-------
Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.

Approach:
--------
1. Simply find the current index of the least element in the array. 
2. That index is how many times that number has been shifted to the right

Manipulation of pointers low and high is similar to search_in_rotated_array

Complexity:
----------
Time: O(log N)
Space: O(1)

"""

def count_rotations(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[low] == arr[mid] and arr[high] == arr[mid]:
            if arr[low] > arr[low + 1]:  # if element at low+1 is not the smallest
                return low + 1
            low += 1
            if arr[high - 1] > arr[high]:  # if the element at high is not the smallest
                return high
            high -= 1
            
        if arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]:
            return mid

        if arr[low] < arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))
    print(count_rotations([3, 3, 7, 3]))

main()

