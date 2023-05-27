"""
Complexity:
-----------

Solution 2:
----------
Time: O(M + N)
Space: O(1)
"""

class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"
        balloon_freq = Counter(balloon)
        text_freq = Counter(text)
        max_number_of_balloons = len(text)
        for c in balloon_freq:
            if c not in text_freq:
                return 0
            potential = text_freq[c] // balloon_freq[c]
            max_number_of_balloons = min(max_number_of_balloons, potential)
        
        return max_number_of_balloons


class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        pattern = "balloon"
        
        pattern_counter = [0] * 26 
        text_counter = [0] * 26
        for c in pattern:
            pattern_counter[ord(c) - ord("a")] += 1
        for c in text:
            text_counter[ord(c) - ord("a")] += 1
        ans = math.inf
        for i in range(26):
            if pattern_counter[i] > 0:
                ans = min(ans, text_counter[i] // pattern_counter[i])
        if ans == math.inf:
            return 0
        return ans