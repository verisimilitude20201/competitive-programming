"""
Concept
-------
1. Stores the frequency of occurence of a character in a hash table.
2. Iterates through string again. Checks in hash table if the character's frequency of occurrence is 1. Returns the index if so.

Complexity:
----------

Time: O(N) We are iterating through string twice.
Space: O(1) We are allocating a hash table for finding unique occurences of characters. 


"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_char_frequency = {}
        for character in s:
            if character in map_char_frequency:
                map_char_frequency[character] += 1
            else:
                map_char_frequency[character] = 1

        for index, character in enumerate(s):
            if map_char_frequency[character] == 1:
                return index

        return -1