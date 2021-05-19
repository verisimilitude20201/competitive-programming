"""
Problem:
-------
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example:
-------
Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.

Approach:
--------
Use binary search. Whenever we find a mid whose value is >= that of the key, track it and find it's max. Floor function would also be similar

Complexity:
----------
Time: O(log N)
Space: O(1)

"""

def search_ceiling_of_a_number(arr, key):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1
    ceil_of_key = -1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] >= key:
            ceil_of_key = max(ceil_of_key, arr[mid])
        if key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return ceil_of_key


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()