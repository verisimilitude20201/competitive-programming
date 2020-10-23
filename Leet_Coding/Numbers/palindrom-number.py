"""
Concept
-------
1. For negative numbers, simply return false
2. For positive numbers, apply the mathematical version of the reverse number problem to reverse the number.
3. Check for overflow. If overflow, set the reversed number to 0.
4. Compare original number and reverse number and return True if they are equal and false if otherwise

Complexity
---------

O(1) Space
O(log n): Time
    10 
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_number = x
        if original_number < x:
            return False
        largest_32_bit_number = pow(2, 31)
        reversed_number = 0
        while x != 0:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + last_digit
            if reversed_number > largest_32_bit_number:
                reversed_number = 0
                break
            x = int(x / 10)
        if original_number == reversed_number:
            return True
        return False