"""
Problem:
-------
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Example:
-------
Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

The input is original array [1, 3, 8, 10, 15] rotated with 2 positions

Approach
-------
1. Start with low and high initiated to 0th and last index of the array
2. Compute mid
3. If arr[low] <= arr[mid], the first half of the array is sorted (low to middle), start from this half.
   i. Check if the key lies within the bounds of arr[low] and arr[mid]. If it does, discard the second half totally - high  = mid -1
   ii. If no, discard the first half low = mid + 1
4. If condition 3 is false, then second half of array (middle + 1 to high) is sorted.
   i. Check if the key lies within the bounds of arr[middle + 1] and arr[high]. If it does, discard the first half totally - low  = mid + 1
   ii. If no, discard the second half high = mid - 1

* If there are duplicates, we simply skip one element from front and back of the array 

Complexity:
----------
Time: O(log N)
Space: O(1)
"""

def search_rotated_array(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == key:
            return mid
        if arr[high] == arr[mid] and arr[low] == arr[mid]:
            low += 1
            high -= 1
        if arr[low] <= arr[mid]:
            if arr[low] >= key and key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] > key and key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 15], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_array([3, 7, 3, 3, 3], 7))


main()
