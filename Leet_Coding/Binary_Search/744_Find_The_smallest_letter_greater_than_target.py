"""
Complexity:
---------
Solution 1
----------
Time: O(N)
Space: O(N) Since we're taking a set 

Solution 1
----------
Time: O(N)
Space: O(1) Since we're taking a set 

Solution 3
---------
Time: O(log N)
Space: O(1)

"""
class Solution1:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters = set(letters)
        for i in range(1, 21):
            letter = chr((ord(target) - ord("a") + i) % 26 + ord("a"))
            if letter in letters:
                return letter

class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        return letters[0]

class Solution3:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]