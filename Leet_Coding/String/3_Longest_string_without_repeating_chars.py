"""
Complexity:
-----------
Solution1
--------
Time: O(N^3)
Space: O(K) K is the number of unique characters in the set.

Solution2
---------
Time: O(N)
Space: O(128/MIN(M,N))
"""
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_unique(s, i, j):
                    max_length = max(max_length, j - i + 1)

        return max_length

    def is_unique(self, s: str, i: int, j: int) -> bool:
        unique_chars = set()
        while i <= j:
            if s[i] in unique_chars:
                return False
            unique_chars.add(s[i])
            i += 1

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = {}
        left = right = 0
        max_length = 0
        for right in range(len(s)):
            right_char = s[right]
            char_count[right_char] = char_count.get(right_char, 0) + 1
            while char_count[right_char] > 1:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length