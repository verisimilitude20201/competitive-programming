"""
Complexity:
----------
canConstruct1
------------
Time: O(N + M)
Space: O(N)

canConstruct2
------------
Time: O(N * M)
Space: O(M)

canConstruct3
------------
Time: O(M)
Space: O(k)/O(1) Since HashMap can contain 26 characters at max.


"""
import collections
class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        if magazine == "" or ransomNote == "":
            return False
        char_count = {}
        for char in ransomNote:
            char_count[char] = char_count.get(char, 0) + 1

        for char in magazine:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]
        return len(char_count) == 0
    
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        if magazine == "" or ransomNote == "":
            return False
        char_count = {}
        for char in ransomNote:
            if char not in magazine:
                return False
            location = magazine.index(char)
            magazine = magazine[:location] + magazine[location + 1:]
        return True
    
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        if magazine == "" or ransomNote == "" or len(ransomNote) > len(magazine):
            return False
        ransom_note_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)
        for char, r_count in ransom_note_count.items():
            if char not in magazine_count:
                return False
            m_count = magazine_count[char]
            if r_count > m_count:
                return False

        return True