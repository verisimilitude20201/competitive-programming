"""
Problem
-------
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example:
-------
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Approach
--------
Instead of appending current number to all subsets, add it only to those subsets that have been previously added in the previous step. For example

0)  Given set -> [1,3, 3]


Output = [[], [1], [3], [1, 3], [1, 3, 3]]


1) [[]], start_index = 0, end_index = 0  
    
  Add 1

  [[], [1]]


2) Add 3 start_index = 0, end_index = 1 

   [[], [1], [3], [1, 3]]


3) Add 3. Now nums[i] == nums[i - 1]
       
        start_index = 1, end_index = 3


    [[], [1], [3], [1, 3], [1, 3], [3, 3], [1, 3, 3]]

Complexity:
----------
Time: O(N * 2^N)
Space: O(2 ^ N)
"""

def find_subsets_for_duplicates(nums):
    subsets = [[]]
    start_index, end_index = 0, 0
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            start_index = end_index + 1
        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets_for_duplicates([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets_for_duplicates([1, 5, 5, 3])))


main()
