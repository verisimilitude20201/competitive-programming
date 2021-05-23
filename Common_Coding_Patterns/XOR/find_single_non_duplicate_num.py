"""
Problem:
-------
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example:
-------
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Approach:
--------
Start with XORing all numbers with each other. The one that's left out at the end is the missing number, the duplicates cancel each other out.

Complexity:
---------
Time: O(1)
Space: O(1)
"""

def find_single_non_duplicate_num(arr):
    num = 0
    for i in range(len(arr)):
        num ^= arr[i]

    return num
def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_non_duplicate_num(arr))

main()