"""
Problem
--------

We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Example:
-------

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1

Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.


Approach
--------
Fast-slow pointers


Complexity:
----------
Time: O(N^2) - The list is iterated through twice - once by the outer for loop and then by the inner index calculation loop
Space: O(1)

"""

def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        fast, slow = i, i
        is_forward = arr[i] > 0

        while True:
            slow = find_next_index(is_forward, arr, slow)
            fast = find_next_index(is_forward, arr, fast)
            if fast != -1:
                fast = find_next_index(is_forward, arr, fast)
            if fast == -1 or slow == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True

    return False


def find_next_index(is_forward, arr, current_index):
    direction = arr[current_index] > 0
    if direction != is_forward:
        return -1

    next_index = (current_index + arr[current_index]) % len(arr)
    if current_index == next_index:
        return -1

    return next_index


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
main()