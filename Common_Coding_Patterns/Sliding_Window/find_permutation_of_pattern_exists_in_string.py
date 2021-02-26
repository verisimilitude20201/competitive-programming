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
Sliding window pattern where the sliding window equals the number of letters in the pattern

find_permutation_of_pattern_exists_in_string1 -->
    Assumes that we have unique characters in pattern.

find_permutation_of_pattern_exists_in_string2 -->
    Assumes that pattern can contain duplicate letters
 
Complexity
---------
    Time: O(N) N is the length of the input string
    Space: O(K) Distinct number of characters in the pattern

Common Mistakes
---------------
1. Not adding a key back to the HashTable.
===> S = xyacabc, P = abc.
    In this case there are multiple occurences of key a in S. The last occurence is what matches the pattern. We would need to add 
    it back

2. Clearly ask if the pattern can contain duplicate characters or not.
    a. If the pattern can contain duplicate characters, below condition would never be True
        if match_count == len(pattern_freq):
            
    b. We would have to check in case pattern can contain duplicates
        if match_count == len(pattern_char_freq)

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

def find_permutation_of_pattern_exists_in_string2(str1, pattern):
    if pattern == "" or str1 == "":
        return False
    window_start, match_count = 0, 0
    pattern_freq = {}
    for char in pattern:
        if char not in pattern_freq:
            pattern_freq[char] = 0
        pattern_freq[char] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern_freq:
            pattern_freq[right_char] -= 1
            if pattern_freq[right_char] == 0:
                match_count += 1
        if match_count == len(pattern_freq):
            return True
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in pattern_freq:
                if pattern_freq[left_char] == 0:
                    match_count -= 1
                pattern_freq[left_char] += 1

    return False


def main():
    print(find_permutation_of_pattern_exists_in_string2("abcdaebaa", "aba"))
    print(find_permutation_of_pattern_exists_in_string2("oidbbbcaf", "abc"))
    print(find_permutation_of_pattern_exists_in_string2("odicf", "dc"))
    print(find_permutation_of_pattern_exists_in_string2("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation_of_pattern_exists_in_string2("aaacb", "abc"))

main()


def main():
    print(find_permutation_of_pattern_exists_in_string1("oidbcaf", "abc"))
    print(find_permutation_of_pattern_exists_in_string1("odicf", "dc"))
    print(find_permutation_of_pattern_exists_in_string1("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation_of_pattern_exists_in_string1("aaacb", "abc"))

main()