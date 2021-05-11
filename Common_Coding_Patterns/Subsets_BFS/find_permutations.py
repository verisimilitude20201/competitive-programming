"""
Problem:
-------
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}


Example:
-------
[1, 3, 5], result = [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]

Approach:
--------

1) []

2) Add 1 

[1]

3) Add 3

[1, 3], [3, 1]

4) Add 5

[1, 3]								[3, 1]
[5, 1, 3], [1, 5 ,3], [1, 3, 5]   [5, 3, 1], [3, 5, 1], [3, 1, 5]

A new number is inserted at all positions of a given 

Complexity:
---------
Time: O(N * N!)
Space: O(N * N!)
"""

from collections import deque


def find_permutations(nums):
    num_length = len(nums)
    permutations = deque()
    permutations.append([])
    result = []
    for num in nums:
        perm_length = len(permutations)
        for _ in range(perm_length):
            old_permutation = permutations.popleft()
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, num)
                if len(new_permutation) == num_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
