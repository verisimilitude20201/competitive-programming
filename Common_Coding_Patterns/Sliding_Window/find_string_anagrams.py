"""
Problem
-------
Given a string and a pattern, find all anagrams of the pattern in the given string.

Approach
--------
Sliding window with fixed size window of len(pattern) chacters - Use a Hashmap for frequency

Input

0 1 2 3 
p p q p,       pattern = pq, char_frequency = {}, result_indexes = [], matched = 0
WS
WE


1. Index the pattern in the hash_map


char_frequency = {p: 1, q: 1}


2. p is present in pattern, increment matched


0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 1}, result_indexes = [], matched = 1
WS
  WE


3. p is again present in the pattern and window_end >= len(pattern) - 1. Decrement matched


0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 1, q: 1}, result_indexes = [], matched = 0
  WS
  WE


4. p is again present in the pattern increment matched


0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 1}, result_indexes = [], matched = 1
  WS
  WE


5. q is also present in pattern. Increment matched

0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 0}, result_indexes = [], matched = 2
  WS
    WE

5. matched equals the count of length of the pattern i.e. char_frequency. Add left index i.e window start to result.

0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 0}, result_indexes = [1], matched = 2
  WS
    WE


6. window_end >= len(pattern) - 1. Decrement matched

0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 1}, result_indexes = [1], matched = 1
    WS
      WE

7. Increment matched


0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 1}, result_indexes = [1], matched = 2
    WS
      WE

8. matched equals the count of length of the pattern i.e. char_frequency. Add left index i.e window start to result.

0 1 2 3 
p p q p,       pattern = pq, char_frequency = {p: 0, q: 1}, result_indexes = [1, 2], matched = 2
    WS
      WE


9. Stop since window_end is past the ends of the array

Complexity:
----------
Time: O(M + N)
Space: O(M)

"""

def find_string_anagrams(str1, pattern):
    char_frequency_map = {}
    window_start = 0
    matched = 0
    anagram_start_indices = []
    for character in pattern:
        if character not in char_frequency_map:
            char_frequency_map[character] = 0
        char_frequency_map[character] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency_map:
            char_frequency_map[right_char] -= 1
            if char_frequency_map[right_char] == 0:
                matched += 1

        if matched == len(char_frequency_map):
            anagram_start_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency_map:
                if char_frequency_map[left_char] == 0:
                    matched -= 1  # Before putting the character back, decrement the matched count
                char_frequency_map[left_char] += 1  # Put the character back

    return anagram_start_indices


print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))