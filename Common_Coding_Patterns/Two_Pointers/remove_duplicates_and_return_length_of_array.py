"""
Problem
-------
Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example:
-------
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].


Approach
-------
Two Pointers

1. remove_duplicates_and_return_length_of_array1: We continue unique_counter till consecutive elements are not equal. The final comparisons are N and so the
number of unique elements would be N + 1

2. remove_duplicates_and_return_length_of_array2: We keep track of the last_non_duplicate_index where the last non_duplicate number was placed. The second 
pointer controls the loop and replaces the current non_duplicate_index with the current loop index if the numbers are not equal


Complexity
---------
    Time: O(N) 
    Space: O(1)

def remove_duplicates_and_return_length_of_array1(arr):
    unique_element_counter = 0
    if len(arr) == 0:
        return 0
    first_pointer = 0
    second_pointer = 1
    while second_pointer < len(arr):
        if arr[first_pointer] != arr[second_pointer]:
            unique_element_counter += 1
        first_pointer += 1
        second_pointer += 1

    return unique_element_counter + 1


def remove_duplicates_and_return_length_of_array2(arr):
    if len(arr) == 0:
        return 0

    last_non_duplicate_index = 1
    i = 1
    while i < len(arr):
        if arr[last_non_duplicate_index - 1] != arr[i]:
            arr[last_non_duplicate_index] = arr[i]
            last_non_duplicate_index += 1
        i += 1

    return last_non_duplicate_index


def main():
    print(remove_duplicates_and_return_length_of_array1([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates_and_return_length_of_array1([2, 2, 2, 11]))

    print(remove_duplicates_and_return_length_of_array2([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates_and_return_length_of_array2([2, 2, 2, 11]))


main()
