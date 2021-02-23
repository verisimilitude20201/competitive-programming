"""
Problem
-------
Given a string, find the length of the longest substring, which has no repeating characters

Example:
-------
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".


Approach
-------
Sliding Window containing longest substring with distinct characters.

Complexity
---------
    Time: O(N) N is the number of characters in string
    Space: O(K) K is the number of distinct characters in string because they'll be stored in the hash table.
"""

def non_repeat_substring1(str1):
    char_freq = {}
    window_start = 0
    max_length = -1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while char_freq[right_char] > 1:
            left_char = str1[window_start]
            if left_char in char_freq:
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def non_repeat_substring2(str1):
    char_position = {}
    window_start = 0
    max_length = -1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_position:
            window_start = max(window_start, char_position[right_char] + 1)
        char_position[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


def main():
    print(non_repeat_substring1("aabccbb"))
    print(non_repeat_substring1("abbbb"))
    print(non_repeat_substring1("abccde"))

    print(non_repeat_substring2("aabccbb"))
    print(non_repeat_substring2("abbbb"))
    print(non_repeat_substring2("abccde"))


main()