"""
Problem
-------
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example:
-------
Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Complexity:
----------
Time: O(N)
Space: O(d) where d is the number of duplicate numbers in the array. 

"""

def find_missing_numbers(nums):
    missingNumbers = []
    i, j, n = 0, 0, len(nums)
    while i < n:
      j = nums[i] - 1
      if i != j and nums[i] != nums[j]:
          nums[i], nums[j] = nums[j], nums[i]
      else:
          i += 1

    for i in range(n):
       if i != nums[i] - 1:
           missingNumbers.append(i + 1)

    return missingNumbers


def main():
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))


main()