"""
Concept:
---------
Consider any 3-digit number i.e. 321.

1. 321 % 10 is 1
2. 321 / 10 is 32.1 and if we truncate it, it becomes 32.
3. 

Explanation
----------------
1. Uses an auxillary string to hold reversed digits
2. We always consider positive numbers. If a number is negative, we track it as a flag and multiply the last result by -1 
3. For checking overflow, we check if the result > pow(2, 31). We consider positive numbers so always we check the positive overflow.

Complexity
-----------
Space: O(1)
Time: log   (N)
          10

"""
class Solution:
    def reverse(self, x: int) -> int:
        reversed_number_string = ""
        largest_integer_32_bit = pow(2, 31)
        is_negative = False
        if x == 0:
            return 0
        if x < 0:
            x = abs(x)
            is_negative = True
        while x != 0:
            reversed_number_string += str(x % 10)
            x = int(x / 10)
        reversed_number = int(reversed_number_string)
        if reversed_number > largest_integer_32_bit:
            return 0
        if is_negative:
            return reversed_number * -1
        return reversed_number