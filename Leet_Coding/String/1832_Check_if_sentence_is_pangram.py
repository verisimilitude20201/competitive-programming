"""
Complexity:
----------
checkIfPangram1
--------------
Time: O(N)
Space: O(1)

checkIfPangram2
--------------
Time: O(N)
Space: O(1)


checkIfPangram3
--------------
Time: O(N)
Space: O(1)
"""
class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in range(26):
            c = chr(i + ord("a"))
            if sentence.find(c) == -1:
                return False
        
        return True
    

class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set(sentence)
        
        return len(letters) == 26

class Solution3:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False] * 26
        for char in sentence:
            seen[ord(char) - ord("a")] = True
        
        for status in seen:
            if not status:
                return False
        
        return True