"""
Problem
-------
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example:
-------
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".


Approach
-------
Sliding window pattern where the sliding window equals the number of letters in the pattern


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

2. Clearly ask if the pattern can contain duplicate characters or not.
    a. If the pattern can contain duplicate characters, below condition would never be True
        if match_count == len(pattern_freq):
            
    b. We would have to check in case pattern can contain duplicates
        if match_count == len(pattern_char_freq)

3. No need to decrement the matched_count once the condition if matched == len(pattern_char_freq) is satisfied. 

"""

def find_string_anagrams(string, pattern):
  window_start, matched = 0, 0
  pattern_char_freq = {}
  anagram_start_indexes = []
  for char in pattern:
    if char not in pattern_char_freq:
      pattern_char_freq[char] = 0
    pattern_char_freq[char] += 1

  for window_end in range(len(string)):
    right_char = string[window_end]
    if right_char in pattern_char_freq:
      pattern_char_freq[right_char] -= 1
      if pattern_char_freq[right_char] == 0:
        matched += 1
    if matched == len(pattern_char_freq):
      anagram_start_indexes.append(window_start)

    if window_end >= len(pattern) - 1:
      left_char = string[window_start]
      if left_char in pattern_char_freq:
        if pattern_char_freq[left_char] == 0:
          matched -= 1
        pattern_char_freq[left_char] += 1
      window_start += 1
  return anagram_start_indexes


def main():
  print('Permutation exist: ' + str(find_string_anagrams("ppqp", "pq")))
  print('Permutation exist: ' + str(find_string_anagrams("abbcabc", "abc")))



main()