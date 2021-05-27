"""
Problem:
-------
Given a string, sort it based on the decreasing frequency of its characters.

Example:
-------
Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

Approach:
--------
1. Compute the frequency of each character
2. Push a tuple of (-frequency, character) on a max_heap.
3. Pop out tuples from max_heap one by one
4. Collect the characters 'frequency' number of times in a list
5. Join the list into a string.

Complexity:
----------
Space: O(N)
Time: O((D * log D) + N )
"""

from heapq import *


def sort_character_by_frequency(string):
    char_frequency = {}
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    max_heap = []
    for character, frequency in char_frequency.items():
        heappush(max_heap, (-frequency, character))

    chars_sorted_by_freq = []
    while max_heap:
        frequency, character = heappop(max_heap)
        for _ in range(-frequency):
            chars_sorted_by_freq.append(character)

    return "".join(chars_sorted_by_freq)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
