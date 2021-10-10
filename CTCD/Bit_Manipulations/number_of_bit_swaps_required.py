def number_of_bit_swaps_required(a, b):
    x = a ^ b
    bit_count = 0
    while x != 0:
        bit_count += (x & 1)
        x >>= 1

    return bit_count


print(number_of_bit_swaps_required(29, 15))

