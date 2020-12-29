"""
Problem
-------
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

For example:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Approach
--------
1. Sliding Window with Variable Window Size
2. Approach similar to Longest Substring with 2 Distinct characters


Time Complexity
--------------
Time: O(N) N is the size of the fruits array
Space: O(1) - Since at a time there may be utmost 3 fruits in the hash map


"""

def fruits_into_baskets(fruits):
    fruit_frequency = {}
    window_start = 0
    max_number_of_fruits = 0
    for window_end in range(len(fruits)):
        ending_fruit = fruits[window_end]
        if ending_fruit not in fruit_frequency:
            fruit_frequency[ending_fruit] = 0
        fruit_frequency[ending_fruit] += 1

        while len(fruit_frequency) > 2:
            starting_fruit = fruits[window_start]
            fruit_frequency[starting_fruit] -= 1
            if fruit_frequency[starting_fruit] == 0:
                del fruit_frequency[starting_fruit]
            window_start += 1

        max_number_of_fruits = max(max_number_of_fruits, window_end - window_start + 1)

    return max_number_of_fruits


print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))