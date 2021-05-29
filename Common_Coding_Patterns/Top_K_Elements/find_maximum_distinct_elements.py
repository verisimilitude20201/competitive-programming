"""
Problem:
-------
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers


Example:
-------
Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have 
to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be left with three 
distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

Approach:
--------
0) [7, 3, 5, 8, 5, 3, 3] K=2
Output = 3

1) num_freq_map = {7: 1, 3: 3, 5: 2, 8: 1}

2) num, freq in num_freq_map:

   i) num = 7, freq = 7, distinct_element_count = 1, min_heap = []
   ii) num = 3, freq = 3, distinct_element_count = 1, min_heap = [(3, 3)]
   iii) num = 5, freq = 2, distinct_element_count = 1, min_heap = [(2, 5), (3, 3)]
   iv) num = 8, freq = 1, distinct_element_count = 2, min_heap = [(2, 5), (3, 3)]

3)  K > 0 and min_heap
   i) freq = 2, num = 5, min_heap = [(3, 3)], K = 2 - 2 = 0, distinct_elements_count = 3

Complexity:
----------
Time: O(N log N + K log N) N log N because we initially insert all numbers in HashMap and min_heap. K log N because we take out K elements from the 
min_heap.
Space: O(N)

"""
