"""
Problem
-------
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example:
-------
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.


Approach
-------
Two Pointers

a + b + c = 0 means
a + b = -c

Keep index i fix for each iteration, and set left = i + 1 and right = len(array) - 1. Find all combinations such that

    -arr[i] = arr[left] + arr[right]

The comparison conditions are similar to that for 2-Sum problem to increment the pointers.


Complexity
---------
    Time: O(N^2 + N log N) 
            N log N for sorting the array. 
            N^2 because we are stepping through the array twice once with i and the second with the traversal of left and right pointers.
            
    Space: O(M)
"""

def get_triplets_summing_to_zero(arr):
    if len(arr) == 0:
        return []
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_triplets_with_zero_sum(-arr[i], i + 1, triplets, arr)
    return triplets


def search_triplets_with_zero_sum(target_sum, left, triplets, arr):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1



def main():
    print(get_triplets_summing_to_zero([-3, 0, 1, 2, -1, 1, -2]))
    print(get_triplets_summing_to_zero([-5, 2, -1, -2, 3]))

main()
