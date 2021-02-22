"""
Problem
-------
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

Example:
-------
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


Approach
-------
Sliding Window containing 2 distinct fruits.

Complexity
---------
    Time: O(N) N is the number of fruits in list
    Space: O(K) K is the number of distinct fruits in list (they'll be placed in a hash table).
"""

def fruits_into_baskets(fruits):
    fruit_freq = {}
    window_start = 0
    max_number_of_fruits = 0
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        while len(fruit_freq) > 2:
            left_fruit = fruits[window_start]
            if left_fruit in fruit_freq:
                fruit_freq[left_fruit] -= 1
                if fruit_freq[left_fruit] == 0:
                    del fruit_freq[left_fruit]
            window_start += 1

        max_number_of_fruits = max(max_number_of_fruits, window_end - window_start + 1)

    return max_number_of_fruits


def main():
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))


main()