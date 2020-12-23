"""
Problem: 
-------
Given an array as input, extract the sub-array of K contiguous integers that have the highest sum. Return the highest sum

Approach:
--------
A] Brute-Force -> Find largest sum

5, 2, 4, 6, 3, 1,   K = 3


1. 

0  1  2  3  4  5
5, 2, 4, 6, 3, 1              i = 0, j from 0 to 2, total = 5 + 2 + 4 = 11
_______
i     j  

2. 

0  1  2  3  4  5
5, 2, 4, 6, 3, 1              i = 1, j from 1 to 3, total = 2 + 4 + 6 = 12
   _______
   i     j

3. 

0  1  2  3  4  5
5, 2, 4, 6, 3, 1              i = 2, j from 2 to 4, total = 3 + 4 + 6 = 13
      _______
      i     j

4. 

0  1  2  3  4  5
5, 2, 4, 6, 3, 1              i = 3, j from 3 to 5, total = 3 + 1 + 6 = 10
         _______
         i     j


Complexity
----------
Space: O(1)
Time: O(N * K) where K is the size of the sub-array. 

Disadvantages
-------------
Repeated Calculations at each step along with near quadratic time-complexity

"""


def longest_sum_of_sub_array(array, K):
	sum = 0
	for i in range(len(array)):
		current_sum = 0
		if i + K > len(array):
			break
		for j in range(i, i + K):
			current_sum += array[j]
		sum = max(sum, current_sum)

print(longest_sum_of_sub_array([5, 2, 4, 6, 3, 1], 3))