"""
Explanation:

1. Check if the bits at position i and j are different.
2. If yes, we need to flip them. 
3. Compute the bit_mask as the OR of 
   a. Number such that its ith bit is set
   b. Number such that its jth bit is set
4. Compute the XOR

Complexity:
----------
Time: O(1)
Space: O(1)

"""


def swap_bits(num, i, j):
    if ((num >> i) & 1) != ((num >> j) & 1):
        bit_mask = (1 << i) | (1 << j)
        num ^= bit_mask

    return num


print(swap_bits(73, 1, 6))