"""
Explanation:
-----------
1. If all ones, assume a 64-bit platform to return max_length as 64
2. Count the contiguous sequence of 1s as curr_length
3. If current bit is 0, check if the next bit is also 0. If yes, prev_length and curr_length both become 0 because we cannot start a sequence of 1s like this.

Complexity:
----------
Time: O(b)
Space: O(1) 

"""
def flip_bit(num):
    if ~num == 0:
        return 64
    prev_length = 0
    curr_length = 0
    max_length = 1
    while num > 0:
        if (num & 1) == 1:
            curr_length += 1
        elif (num & 1) == 0:
            prev_length = curr_length if ((num & 2) != 0) else 0
            curr_length = 0
        max_length = max(max_length, prev_length + curr_length + 1)
        num >>= 1

    return max_length


print(flip_bit(1775))

