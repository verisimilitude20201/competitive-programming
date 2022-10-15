"""
Complexity:
----------
Time: O(N)
Space: O(N) where D is the number of distinct characters in the string
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        seen = defaultdict(int)
        right = 0
        left = 0
        max_length = 0
        for right in range(len(s)):
            right_char = s[right]
            seen[right_char] += 1
            while len(seen) > 2:
                left_char = s[left]
                seen[left_char] -= 1
                if seen[left_char] == 0:
                    del seen[left_char]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length