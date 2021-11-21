"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""

class Solution:
    def removeVowels(self, s: str):
        if len(s) == 0:
            return ""
        vowels = "aeiou"
        chars_without_vowels = [c for c in s if c not in vowels]
        return "".join(chars_without_vowels)