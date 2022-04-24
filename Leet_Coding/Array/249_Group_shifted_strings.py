"""
Complexity:
----------
Time: O(N * K)
Space: O(N * K)
"""
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strings:
            hash_value = self._get_hash(string)
            result[hash_value].append(string)
        
        return result.values()
    
    def _get_hash(self, string: str) -> str:
        shift = string[0]
        return "#".join(self._hash_code(letter, shift) for letter in string)
    
    def _hash_code(char: str, shift: str) -> int:
        return (ord(char) - ord(shift) % 26) + ord("a")