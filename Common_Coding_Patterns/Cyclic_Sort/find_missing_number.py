"""
Problem
-------
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example:
-------
Input: [4, 0, 3, 1]
Output: 2

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

Approach
--------
Cyclic sort. Element at index i is equal to i itself. 

Complexity:
----------
Time: O(N)
Space: O(1)

"""

def find_missing_number(nums):
    i, j, n = 0, 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[j] != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i != nums[i]:
            return i

    return -1


def main():
  print(find_missing_number([4, 0, 3, 1]))


main()