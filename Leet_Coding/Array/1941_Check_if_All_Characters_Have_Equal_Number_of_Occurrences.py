"""
Complexity:
---------
Time: O(N)
Space: O(N)
"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(s) == 1:
            return True
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        frequencies = set(count.values())
        
        return len(frequencies) == 1