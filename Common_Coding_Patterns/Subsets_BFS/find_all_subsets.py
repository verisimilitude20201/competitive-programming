"""
Problem:
-------
Given a set with distinct elements, find all of its distinct subsets.

Example:
--------
0)  Given set -> [1,5, 3]


Output = [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]

Approach
--------
1)                       []      

2)                     []       [1] ---> Copy [] and add 1

3)               []    [1]   [5] [1, 5]  ---> Copy [], [1] & add [5]         

4)         []    [1]   [5] [1, 5] [3] [1, 3], [5, 3] [1, 5, 3]       -> Copy [] [1]   [5] [1, 5] and add 3

This is a binary tree kind of structure where the nodes at each level is 2 ^ node level.

Complexity
---------
Time: O(N * 2^N). The inner loop takes double the time to append the current number to all existing sub-lists within the list. The outer loop takes N time.
Space: O(2^N)

"""

def find_all_subsets(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_all_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_all_subsets([1, 5, 3])))


main()
