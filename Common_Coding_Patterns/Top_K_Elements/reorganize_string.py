"""
Problem:
-------
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

Example:
-------
Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more  
Explanation: All same characters are 3 distance apart.

Approach:
--------
1. Similar to rearrage_string. However, we need to keep K previous characters in a queue and append the first one after K.
2. For example: if there are two repeated gs, and we have already appended one, add it to queue and pop the next character from the max_heap
3. Continue popping and appending from the max heap till the len(queue) equals k.

Complexity:
----------
Time: O(N log N)
Space: O(N + K), because we are storing K previous characters on the queue.
"""
from heapq import *
from collections import deque


def reorganize_string(string, k):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1

    max_heap = []
    for char, frequency in char_freq.items():
        heappush(max_heap, (-frequency, char))

    prev_chars = {}
    output = []
    queue = deque()
    while max_heap:
        frequency, char = heappop(max_heap)
        output.append(char)
        queue.append([char, frequency+1])
        if len(queue) == k:
            prev_char, prev_freq = queue.popleft()
            if -prev_freq > 0:
                heappush(max_heap, (prev_freq, prev_char))

    return "".join(output)


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Rearranged string:  " + reorganize_string("Programming", 3))


main()
