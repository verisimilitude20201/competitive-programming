"""
Problem
-------
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example:
-------
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".


Approach
-------
Sliding Window containing longest substring having same letters

For the above example, Sliding window will change if 

0 1 2 3 4 5 6
a a b c c b b
WS      WE

Current length of window (window_end - window_start + 1) - max_count_of_repeated_letters > Number of characters to be replaced (K)
 
Complexity
---------
    Time: O(N) N is the number of characters in string
    Space: O(K) K is the number of distinct characters in string because they'll be stored in the hash table.
"""

def length_of_longest_substring_after_k_letter_replacement(str1, k):
    char_freq = {}
    max_count_of_repeated_letter = 0
    window_start = 0
    max_length = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        max_count_of_repeated_letter = max(max_count_of_repeated_letter, char_freq[right_char])
        while window_end - window_start + 1 - max_count_of_repeated_letter > k:
            left_char = str1[window_start]
            if left_char in char_freq:
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print(length_of_longest_substring_after_k_letter_replacement("aabccbb", 2))
    print(length_of_longest_substring_after_k_letter_replacement("abbcb", 1))
    print(length_of_longest_substring_after_k_letter_replacement("abccde", 1))



main()