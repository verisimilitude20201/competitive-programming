"""
Complexity:
---------
Time: O(N)
Space: O(1) Assuming we store lowercase 26 english alphabets
"""
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen_chars = set()
        for char in s:
            if char in seen_chars:
                return char
            seen_chars.add(char)