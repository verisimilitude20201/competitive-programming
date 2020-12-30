"""
Problem
-------
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Approach
--------
Sliding Window with Dynamic Window size and Use of Hashmap to store the frequencies of characters

Input, K = Max number of characters to replace = 2

0   1   2   3   4   5   6               max_letter_count = 0
a   a   b   c   c   b   b               char_frequency = {}
WS
WE



1. 

0   1   2   3   4   5   6               max_letter_count = max(0, char_frequency(a)) = 1
a   a   b   c   c   b   b               char_frequency = {a: 1}
WS
    WE



2. 


0   1   2   3   4   5   6               max_letter_count = max(1, char_frequency(a)) = 2
a   a   b   c   c   b   b               char_frequency = {a: 2}
WS
    WE


3. 

0   1   2   3   4   5   6               max_letter_count = max(2, char_frequency(b)) = 2
a   a   b   c   c   b   b               char_frequency = {a: 2, b: 1}
WS
        WE


4. 


0   1   2   3   4   5   6               max_letter_count = max(2, char_frequency(c)) = 2
a   a   b   c   c   b   b               char_frequency = {a: 2, b: 1, c: 1}
WS
            WE

5. 

0   1   2   3   4   5   6               max_letter_count = max(2, char_frequency(c)) = 2
a   a   b   c   c   b   b               char_frequency = {a: 1, b: 1, c: 2}
    WS
                WE

Complexity:
----------
Time: O(N)
Space: O(c) Where C is the unique number of characters in the string.

"""
def length_of_longest_substring(str1, k):
    char_frequency = {}
    window_start = 0
    max_letter_count = 0
    max_length_of_substring = 0

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        max_letter_count = max(max_letter_count, char_frequency[right_char])

        if window_end - window_start + 1 - max_letter_count > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            window_start += 1

        max_length_of_substring = max(max_length_of_substring, window_end - window_start + 1)

    return max_length_of_substring


print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))