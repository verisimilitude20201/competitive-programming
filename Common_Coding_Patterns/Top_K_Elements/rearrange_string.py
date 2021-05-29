"""
Problem:
-------
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example:
-------
Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.

Approach:
--------
1. Compute the frequency of all chars and push on a max_heap
2. Pop one of the most frequently occuring chars and append to output
3. Before decrementing it's frequency and adding it back to heap, because we do not want same characters next to each other, 
continue with the loop and remove another character.
4. Keep track of the prev character and prev frequency, we would need to add it back to the heap.

Complexity:
----------
Time: O(N log N)
Space: O(N)

"""

from heapq import *


def rearrange_string(string):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, frequency in char_freq.items():
        heappush(max_heap, (-frequency, char))

    prev_char = ""
    prev_freq = 0
    output = []
    while max_heap:
        frequency, char = heappop(max_heap)
        if prev_char != "" and -prev_frequency > 0:
            heappush(max_heap, (prev_frequency, prev_char))
        output.append(char)
        prev_frequency = frequency + 1
        prev_char = char

    return "".join(output)


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))

main()
