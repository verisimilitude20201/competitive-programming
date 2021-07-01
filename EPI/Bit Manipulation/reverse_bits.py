"""
Complexity:
---------
Time: O(N)
Space: O(1)
"""
def reverse_bits(num):
    bit_count = get_bit_count(num)
    return reverse(num, bit_count, 0)


def get_bit_count(num):
    bit_count = 0
    while num:
        num >>= 1
        bit_count += 1

    return bit_count


def reverse(num, i, j):
    while j <= i:
        if ((num >> j) & 1) != ((num >> i) & 1):
            bit_mask = 1 << i | 1 << j
            num ^= bit_mask
        j += 1
        i -= 1

    return num


print(reverse_bits(11))