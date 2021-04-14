"""
Problem
-------
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Example:
-------
Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]

Approach:
---------
Cyclic Sort. 

1. If number is not at the correct index, swap it with the number at the correct index. 
2. Repeat this till the number at current index is the correct one.
3. Then only increment the current index.

0)  0  1  2  3  4  5
   [2, 6, 4, 3, 1, 5],         start = 2


1)  Swap 2 with 6 (index 1 and 0)

    0  1  2  3  4  5
   [6, 2, 4, 3, 1, 5],         start = 6


1)  Swap 6 with 5 (index 0 and 5)

    0  1  2  3  4  5
   [5, 2, 4, 3, 1, 6],         start = 5


2) Swap 5 with 1 (index 0 and 4)

    0  1  2  3  4  5
   [1, 2, 4, 3, 5, 6],         start = 1


    0  1  2  3  4  5
   [1, 2, 4, 3, 5, 6],         start = 2


    0  1  2  3  4  5
   [1, 2, 4, 3, 5, 6],         start = 4


3) Swap 4 with 3 (Index 2 with 3)

    0  1  2  3  4  5
   [1, 2, 3, 4, 5, 6],         start = 5


    0  1  2  3  4  5
   [1, 2, 3, 4, 5, 6],         start = 5

Complexity:
----------
Time: More than N iterations but the swaps in each iteration is N - 1. Therefore, asymptotic complexity is O(N)
Space: O(1)

"""

def cyclic_sort(nums):
    i, j = 0, 0
    while i < len(nums):
        j = nums[i] - 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
