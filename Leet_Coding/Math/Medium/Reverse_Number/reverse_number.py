"""
Complexity:
----------
Time: O(log x)
           10
Space: O(1)
"""
class Solution:
    def reverse(self, x: int) -> int:
        max_positive_int = pow(2, 31) 
        max_negative_int = -(max_positive_int-1)
        last_digit_of_max_positive = max_positive_int % 10
        last_digit_of_max_negative = -(max_negative_int % 10)
        max_positive_int /= 10
        max_negative_int /= 10

        reversed_int = 0
        x1 = abs(x)
        while x1 > 0:
            last_digit = x1 % 10
            x1 //= 10
            if reversed_int > max_positive_int or (reversed_int == max_positive_int and last_digit > last_digit_of_max_positive):
                return 0
            
            if reversed_int < max_negative_int or (reversed_int == max_negative_int and last_digit < last_digit_of_max_negative):
                return 0
            
            reversed_int = reversed_int * 10 + last_digit
            

        return -reversed_int if x < 0 else reversed_int