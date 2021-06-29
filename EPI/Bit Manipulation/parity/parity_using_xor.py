"""
Complexity:
----------
Time: O(log N)
Space: O(1)
"""

def parity_using_xor(num):
    right_shift_by = 32
    while right_shift_by >= 1:
        num ^= num >> int(right_shift_by)
        right_shift_by /= 2

    return num & 1


print(parity_using_xor(5))
    