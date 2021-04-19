"""
Problem:
-------
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some numbers appearing twice, find all these duplicate numbers without using any extra space

Example:
-------
Input: [3, 4, 4, 5, 5]
Output: [4, 5]


Approach
-------

1. find_all_duplicates1:    
    a. Keep track of all numbers that have'nt been placed at the correct index.
    b. Increment the main loop counter for duplicates case or if the element is placed at the correct index.

2. find_all_duplicates2
    a. Swap to place numbers at correct index in the first loop
    b. In the second loop find all those numbers that are not placed in correct index. Those are duplicates.

Complexity:
----------
Time: O(N)
Space: O(d) where d is the number of duplicates in array

"""


def find_all_duplicates1(nums):
    i, j, n = 0, 0, len(nums)
    duplicates = []
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                duplicates.append(nums[i])
                i += 1
        else:
            i += 1

    return duplicates

def find_all_duplicates2(nums):
    i, j, n = 0, 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    i = 0
    duplicates = []
    while i < n:
        if nums[i] != i + 1:
            duplicates.append(nums[i])
        i += 1

    return duplicates

print(find_all_duplicates1([3, 4, 4, 5, 5]))
print(find_all_duplicates1([5, 4, 7, 2, 3, 5, 3]))


print(find_all_duplicates2([3, 4, 4, 5, 5]))
print(find_all_duplicates2([5, 4, 7, 2, 3, 5, 3]))