"""
Problem
-------
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example:
-------
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".


Approach
-------
Sliding Window containing K distinct characters.

Complexity
---------
    Time: O(N) N is the number of chars in string
    Space: O(K) K is the number of distinct chars in string.
"""

def longest_substring_with_k_distinct(str1, K):
    char_frequency = {}
    window_start = 0
    max_length = 1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        while len(char_frequency) > K:
            left_char = str1[window_start]
            if left_char in char_frequency:
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))

main()
