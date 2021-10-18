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
non_repeat_substring_brute_force
--------------------------------
Time: O(N^3)
Space: O(Min(M, N)) Where M is the length of the string and N is the length of Set.


non_repeat_substring_two_pointers_hash_map:
------------------------------------------
    Time: O(2N) ~ O(N) N is the number of characters in string
    Space: O(Min(M, N)) Where M is the length of the string and N is the length of Set.


non_repeat_substring_two_pointer_optimized
---------------------
Time: O(N)
Space: O(Min(M, N)) Where M is the length of the string and N is the length of Set.

"""

def non_repeat_substring_brute_force(s: str) -> int:
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if check_repetition(s, i, j):
                res = max(res, j - i + 1)

    return res


def check_repetition(s: str, start: int, end: int) -> bool:
    chars = [0] * 26
    for i in range(start, end + 1):
        ord_c = ord(s[i])
        chars[ord_c] += 1
        if chars[ord_c] > 1:
            return False

    return True


def non_repeat_substring_two_pointers_hash_map(s: str) -> int:
    chars = [0] * 128
    left = right = 0
    res = 0
    while right < len(s):
        r = s[right]
        ord_c = ord(r)
        chars[ord_c] += 1

        while chars[ord_c] > 1:
            l = s[left]
            chars[ord_c] -= 1
            left += 1

        res = max(res, right - left + 1)
        right += 1

    return res


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