"""
Problem
-------
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number 
going missing. Find both these numbers.

Example:
-------
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Approach:
--------
1. Sort the numbers cyclically. 
2. Since only one number is missing and one number is duplicated, that number is the one not at the correct index and m
    a. Missing number:  incorrect index + 1
    b. Duplicated number: current number at incorrect index.

Complexity:
---------
Time: O(N)
Space: O(1)
"""

def find_corrupt_numbers(nums):
    i, j, n = 0, 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    corrupt_numbers = [-1, -1]
    i = 0
    while i < n:
        if nums[i] != i + 1:
            corrupt_numbers[0] = nums[i]
            corrupt_numbers[1] = i + 1
        i += 1

    return corrupt_numbers


print(find_corrupt_numbers([3, 1, 2, 5, 2]))
print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))

