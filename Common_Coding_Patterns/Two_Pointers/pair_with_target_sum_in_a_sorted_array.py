"""
Problem
-------
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example:
-------
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6


Approach
-------
Two Pointers

Assumption & Caveats
---------
1. Here we are assuming that the array is already sorted. 
2. Also, there is only one pair of integers which sum up to the target sum. 
    2.1 If this is not the case, after every pair that we find, decrement the end_pointer and increment the start_pointer

Complexity
---------
    Time: O(N) Where M = length of the string, N = number of words, L = Length of each word
    Space: O(2) ~ O(1) 

"""
def pair_with_target_sum_in_a_sorted_array(target_sum, array):
    if len(array) == 0:
        return []

    target_element_pair = []
    start_pointer = 0
    end_pointer = len(array) - 1

    while start_pointer < end_pointer:
        current_sum = array[start_pointer] + array[end_pointer]
        if current_sum > target_sum:
            end_pointer -= 1
        elif current_sum < target_sum:
            start_pointer += 1
        else:
            target_element_pair.append(start_pointer)
            target_element_pair.append(end_pointer)

            return target_element_pair



def main():
    print(pair_with_target_sum_in_a_sorted_array(6, [1, 2, 3, 4, 6]))
    print(pair_with_target_sum_in_a_sorted_array(11, [2, 5, 9, 11]))

main()
