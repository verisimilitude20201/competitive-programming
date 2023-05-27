"""
Complexity:
----------
Time: O(4^N * N)
Space: O(N)
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        combinations = []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, chars):
            if len(chars) == len(digits):
                combinations.append("".join(chars))
                return
            
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                chars.append(letter)
                backtrack(index + 1, chars)
                chars.pop()
        backtrack(0, [])
        
        return combinations