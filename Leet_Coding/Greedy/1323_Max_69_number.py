"""
Complexity:
----------
Time: O(N)
Space: O(1)
"""
class Solution:
    def maximum69Number(self, num: int) -> int:
        index_first_six = -1
        num_copy = num
        current_digit = 0
        while num_copy:
            if num_copy % 10 == 6:
                index_first_six = current_digit
            num_copy //= 10
            current_digit += 1

        if index_first_six == -1:
            return num

        return num + (3 * pow(10, index_first_six))