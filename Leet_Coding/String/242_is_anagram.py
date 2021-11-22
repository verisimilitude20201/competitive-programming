"""
Complexity:
----------
isAnagram1
    Time: O(N)
    Space: O(N)

isAnagram2
    Time: O(N)
    Space: O(1)

Follow-Up:
--------
"""
import collections

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_map_count = collections.Counter(t)
        for char in s:
            if char in t_map_count:
                t_map_count[char] -= 1
                if t_map_count[char] == 0:
                    del t_map_count[char]
        
        return len(t_map_count) == 0
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_alpha_count = [0] * 26
        for i in range(len(s)):
            t_alpha_count[ord(s[i]) - ord("a")] += 1
            t_alpha_count[ord(t[i]) - ord("a")] -= 1
        
        for count in t_alpha_count:
            if count > 0:
                return False
        
        
        return True
        