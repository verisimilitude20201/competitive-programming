"""
Problem
-------
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example:
-------
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.


Approach
-------
Two Pointers


Keep index i fix for each iteration, and set left = i + 1 and right = len(array) - 1. Find all combinations such that

     current_sum = arr[left] + arr[right] + arr[i]
     current_sum <= target_sum
        And keep track of the max_sum that is less than target_sum viz.
            max_sum = max(current_sum, max_sum)

The comparison conditions are similar to that for 2-Sum problem to increment the pointers.


Complexity
---------
    Time: O(N^2 + N log N) 
            N log N for sorting the array. 
            N^2 because we are stepping through the array twice once with i and the second with the traversal of left and right pointers.
            
    Space: O(M)
"""

import math


class TriplesWithSumClosestToTarget:
    def __init__(self, arr, target_sum):
        self._arr = arr
        self._target_sum = target_sum

    def get_sum_of_triplet(self):
        if len(self._arr) == 0:
            return -1

        self._arr.sort()
        right = len(self._arr) - 1
        min_sum = -math.inf
        for i in range(len(self._arr)):
            if i > 0 and self._arr[i - 1] == self._arr[i]:
                continue
            left = i + 1
            while left < right:
                current_sum = self._arr[i] + self._arr[left] + self._arr[right]
                if current_sum <= self._target_sum:
                    min_sum = max(min_sum, current_sum)
                    left += 1
                    while left < right and self._arr[left] == self._arr[left - 1]:
                        left += 1
                    while left < right != len(self._arr) - 1 and self._arr[right] == self._arr[right + 1]:
                        right -= 1
                else:
                    right -= 1
        if min_sum == math.inf:
            return -1

        return min_sum


def main():
    triplets_with_sum_closest_to_target1 = TriplesWithSumClosestToTarget([-2, 0, 1, 2], 2)
    print(triplets_with_sum_closest_to_target1.get_sum_of_triplet())

    triplets_with_sum_closest_to_target2 = TriplesWithSumClosestToTarget([-3, -1, 1, 2], 1)
    print(triplets_with_sum_closest_to_target2.get_sum_of_triplet())

    triplets_with_sum_closest_to_target3 = TriplesWithSumClosestToTarget([1, 0, 1, 1], 100)
    print(triplets_with_sum_closest_to_target3.get_sum_of_triplet())

main()
