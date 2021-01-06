"""
Problem
-------
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

For example: 

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Approach
--------
Sliding Window with Dynamic Window Size and Use of HashMap

Complexity
----------
Time: O(N + M)
Space: O(M)


"""

def smallest_substring_containing_anagram(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    char_frequency = {}
    min_length = len(str1) + 1

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # Decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1

        while matched == len(pattern):  # Have we found an anagram?
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1  # Before putting the character back, decrement the matched count
                char_frequency[left_char] += 1  # Put the character back

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


print(smallest_substring_containing_anagram("aabdec", "abc"))
print(smallest_substring_containing_anagram("abdbca", "abc"))
print(smallest_substring_containing_anagram("adcad", "abc"))
