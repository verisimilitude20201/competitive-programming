"""
Explanation:
------------

is_all_chars_unique1
--------------------
    1. Assumes a 128-ASCII charset.
    2. Initialize a list of 128 characters with the alphabet's integer code.
    3. Return False if the index is already occupied. Return true at the end of the iteration

is_all_chars_unique2:
---------------------
Uses bit-vector

Complexity:
-----------
is_all_chars_unique1
-------------------
Time: O(N)
Space: O(128)/O(1)/O(N)

is_all_chars_unique2
--------------------
Time: O(N)
Space: O(N)

Note:
----
1. If we don't want to use additional data structures we can
    a. Scan characets in two-nested loops comparing each character with every other character.
    b. Sort the string and compare if consecutive characters are not the same.


"""
class Solution:
    def is_all_chars_unique1(self, s: str) -> bool:
        alphabets = [None] * 128
        for i in range(len(s)):
            index = ord(s[i])
            if alphabets[index] is not None:
                return False
            alphabets[index] = s[i]
        return True
    
    def is_all_chars_unique2(self, s: str) -> bool:
        checker = 0
        for char in s:
            index = ord(char) - ord("a")
            if (checker & (1 << index)) > 0:
                return False
            checker |= (1 << index)
        return True