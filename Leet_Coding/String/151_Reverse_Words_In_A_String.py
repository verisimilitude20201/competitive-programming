"""
Complexity:
----------
Time: O(N)
Space: O(N)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words_without_spaces = self.trim_spaces(s)
        left = 0
        right = len(words_without_spaces) - 1
        while left < right:
            words_without_spaces[left], words_without_spaces[right] = words_without_spaces[right], words_without_spaces[
                left]
            left += 1
            right -= 1

        return " ".join(words_without_spaces)

    def trim_spaces(self, s: str) -> List[str]:
        words_without_spaces = []
        words = s.split(" ")
        for word in words:
            if word != "":
                words_without_spaces.append(word)

        return words_without_spaces