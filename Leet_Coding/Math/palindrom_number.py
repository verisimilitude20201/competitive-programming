"""
Complexity:
----------
Time: O(log   N)
           10
Space: O(1)

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        num = x
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x //= 10

        return (x == reversed) or (x == (reversed // 10))