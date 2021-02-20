"""
Problem
-------
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum 
is greater than or equal to ‘S’. Return 0 if no such subarray exists.


Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: Smallest sub-array with Sum >= 7 is of length 2 viz. [5, 2]

Approach
-------
Variable length Window.
    Increment window size till curent total < K
    Decrement window size by 1 when current total >= K

Complexity
---------
    Time: O(N)
    Space: O(1)

"""
import math


def smallest_sub_array_with_a_given_sum(S, arr):
    min_length = math.inf
    window_start = 0
    total = 0
    for window_end in range(len(arr)):
        total += arr[window_end]
        while total >= S:
            min_length = min(min_length, window_end - window_start + 1)
            total -= arr[window_start]
            window_start += 1

    if min_length == math.inf:
        return 0
    return min_length


def main():
  print("Smallest subarray length: " + str(smallest_sub_array_with_a_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_sub_array_with_a_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_sub_array_with_a_given_sum(8, [3, 4, 1, 1, 6])))


main()
