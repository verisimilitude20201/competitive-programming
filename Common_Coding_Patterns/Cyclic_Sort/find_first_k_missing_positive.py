"""
Problem
-------
Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array

Example:
-------
Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Approach
-------
Cyclic Sort

1. Ignore all elements less than 0, duplicate ones and greater than size of the array
2. Tricky Part: 
    i. If we don't find k missing numbers, we would need additional numbers in the output array. 
    ii. We keep track of extra numbers that don't fit in their indices. In above example, -1 and 5
    iii. We then repeatedly add 1 to the length of the array which becomes a potential candidate number
    iv. We add above candidate number to the output array if and only if len(missing_numbers) < k and this number is not a part of extra numbers

3. Use of a set is to have O(1) time to check if number exists in the set.

Complexity:
----------
Time: O(N + K)
Space: O(K)

"""

import math


def find_first_k_missing_positive(nums, k):
    i, j, n = 0, 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    missing_numbers = set()
    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) >= k:
            break
        if nums[i] != i + 1:
            missing_numbers.add(i + 1)
            extra_numbers.add(nums[i])
    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n
        if candidate_number not in extra_numbers:
            missing_numbers.add(candidate_number)
        i += 1

    return missing_numbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
