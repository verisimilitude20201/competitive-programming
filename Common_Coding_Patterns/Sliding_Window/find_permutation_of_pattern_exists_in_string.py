"""
Problem
-------
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations

Example:
-------
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.


Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.


Approach
-------
Sliding window pattern

find_permutation_of_pattern_exists_in_string1 -->
    Assumes that we have unique characters in pattern.
 
Complexity
---------
    Time: O(N) N is the length of the input string
    Space: O(K) Distinct number of characters in the pattern
"""

def find_permutation_of_pattern_exists_in_string1(str1, pattern):
    if pattern == "" or str1 == "":
        return False

    pattern_map = {}
    for char in pattern:
        pattern_map[char] = True
    window_start = 0
    match_count = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern_map:
            match_count += 1
        else:
            match_count -= 1
            if match_count < 0:
                match_count = 0
            window_start += 1
        if match_count == len(pattern):
            return True

    return False


def main():
    print(find_permutation_of_pattern_exists_in_string1("oidbcaf", "abc"))
    print(find_permutation_of_pattern_exists_in_string1("odicf", "dc"))
    print(find_permutation_of_pattern_exists_in_string1("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation_of_pattern_exists_in_string1("aaacb", "abc"))

main()