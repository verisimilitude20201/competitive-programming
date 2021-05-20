"""
Problem
------
Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. 
Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. 
ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

Example:
-------
Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.

Approach
--------
Finding the bounds is most crucial here for binary search to apply since we don't know the bounds of the array.

Start within initially low = 0 and high = 1 and then double them

low = high + 1
high = (high - old_low + 1) * 2

Complexity:
---------
Time: O(log N + log N). The first log N would be to compute the bounds because we're doubling them. The second log N would be to search in the 
found bounds.
Space: O(1)

"""
import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    low, high = get_proper_bounds(reader, key)
    while low <= high:
        mid = low + ((high - low) // 2)
        if reader.get(mid) == math.inf:
            return -1
        if reader.get(mid) == key:
            return mid
        elif reader.get(mid) > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def get_proper_bounds(reader, key):
    low = 0
    high = 1
    while reader.get(high) < key:
        new_low = high + 1
        high = (high - low + 1) * 2
        low = new_low
    return [low, high]


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))


main()
