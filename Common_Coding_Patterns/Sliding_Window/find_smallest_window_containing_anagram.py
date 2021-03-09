"""
Problem
-------
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example:
-------
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.

Approach
-------
Sliding window pattern where the sliding window contains the chars of the anagram plus some additional characters


Complexity
---------
    Time: O(N + M) N is the length of the input string and M is length of the pattern
    Space: O(M) Distinct number of letters in the pattern, O(N) since each index of the string can start an anagram 

Common Mistakes
---------------
1. Not adding a key back to the HashTable.
===> S = xyacabc, P = abc.
    In this case there are multiple occurences of key a in S. The last occurence is what matches the pattern. We would need to add 
    it back

2. Here we check if the match count is equal to the length of the pattern. This is because our output string will contain additional characters other than
chars in the anagram

3. We increment matched_count if pattern_char_freq[right_char] >= 0. Again, this is because our output string will contain additional characters other than
chars in the anagram.

4. Once the matched_count equals the length of the pattern, we would need to continue reducing the window and finding the minimun window containing all
anagram chars and any additional characters.

"""


import math


def find_smallest_window_containing_anagram(string, pattern):
    pattern_char_freq = {}
    window_start, matched, substring_start = 0, 0, 0
    min_length = math.inf
    for char in pattern:
        if char not in pattern_char_freq:
            pattern_char_freq[char] = 0
        pattern_char_freq[char] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in pattern_char_freq:
            pattern_char_freq[right_char] -= 1
            if pattern_char_freq[right_char] >= 0:
                matched += 1
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substring_start = window_start
            left_char = string[window_start]

            if left_char in pattern_char_freq:
                if pattern_char_freq[left_char] == 0:
                    matched -= 1
                pattern_char_freq[left_char] += 1

            window_start += 1

    if min_length == math.inf:
        return ""

    return string[substring_start: substring_start + min_length]


def main():
    print(find_smallest_window_containing_anagram("aabdec", "abc"))
    print(find_smallest_window_containing_anagram("abdbca", "abc"))
    print(find_smallest_window_containing_anagram("adcad", "abc"))


main()
