"""
Problem
-------
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array

Example:
-------
Input: [1, 4, 4, 3, 2]
Output: 4

Input: [2, 1, 3, 3, 5, 4]
Output: 3

Approach
--------
Cyclic sort

1. Keep finding the correct index of the number if A[i] != i + 1
2. If we can swap the numbers, then swap them.
3. If we cannot swap the numbers, there's your duplicate

Complexity:
---------
Time: O(N)
Space: O(1)

"""

def find_duplicate(nums):
    i, j, n = 0, 0, len(nums)
    while i < n:
        if nums[i] == i + 1:
            i += 1
        else:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]

    return -1


print(find_duplicate([1, 4, 4, 3, 2]))
print(find_duplicate([2, 1, 3, 3, 5, 4]))
print(find_duplicate([2, 4, 1, 4, 4]))