class Solution:
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