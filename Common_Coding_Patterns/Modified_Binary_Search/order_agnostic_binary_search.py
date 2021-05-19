"""
Problem:
-------
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates

Example:
-------
Input: [4, 6, 10], key = 10
Output: 2

Input: [10, 6, 4], key = 10
Output: 0

Approach:
--------
Definitely this is a case of binary search. But the array can be sorted in ascending or descending so this gives rise to 4 cases of modifying the low and high pointers

Case 1: Ascending Find 2

2 < 3

mid = high - 1

[1, 2, 3, 4, 5]
low    mid   high



Case 2: Ascending Find 5

3 > 5

low = mid + 1



Case 3: Descending 

[5, 4, 3 ,2, 1]
low    mid  high   
Find 4

4 > 3
mid = high - 1


Case 4: Descending
[5, 4, 3 ,2, 1]
low    mid  high 

Find 2

2 < 3
low = mid + 1



Complexity:
----------
Time: O(log N)
Space: O(1)
"""


def order_agnostic_binary_search(arr, key):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1
    is_ascending = arr[low] < arr[high]
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == key:
            return mid
        if is_ascending:
            if key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if key < arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def main():
  print(order_agnostic_binary_search([4, 6, 10], 10))

main()