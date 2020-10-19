"""
Solution 1 (Using an auxillary string):
----------
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


Solution 2 (Plain Mathematical)
------------------------------
Consider any 3-digit number i.e. 321.

0. int rev = 0
1. digit = 321 % 10 = 1
	rev = 10 * rev + digit = 0 + 1 = 1
	number = 321 / 10 = 32.1 ~ 32

2. digit = 32 % 10 = 2
	rev = 10 * rev + digit = 10 * 1 + 2 = 12
	number = 32 / 10 = 3.2 = 3

3. digit = 3 % 10 ~ 3
	rev = 10 * rev + digit = 10 * 12 + 3 = 123
	number = 3 / 10 = 0.3 ~ 0

Complexity
-----------
Space: O(1)
Time: log   (N)
          10

"""
class Solution:
    def reverse1(self, x: int) -> int:
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
    
    def reverse2(number: int) -> int:
        sign_multiplier = -1 if number < 0 else 1
        reversed_number = 0
        largest_32_bit_number = pow(2, 31)
        number = abs(number)
        while number != 0:
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            if reversed_number > largest_32_bit_number:
                return 0
            number = int(number / 10)

        return reversed_number * sign_multiplier