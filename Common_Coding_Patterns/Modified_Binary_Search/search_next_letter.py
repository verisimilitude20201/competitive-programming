"""
Problem:
-------
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. 
This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

Example:
-------
Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.

Approach:
--------
1. Since the array is a circular linked list, if key is greater than last element in the array or less than 0th element, return the 0th element.
2. We return the next element that is not equal to the given key. So if that is the last element, we should return the first one.

Tricky Part:
-----------
Understand the significance of circular linked list.

Complexity:
Time: O(log N)
Space: O(1)

"""


def search_next_letter(letters, key):
    n = len(letters)
    if key < letters[0] or key > letters[n - 1]:
        return letters[0]
    low = 0
    high = len(letters) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if key < letters[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return letters[low % n]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
