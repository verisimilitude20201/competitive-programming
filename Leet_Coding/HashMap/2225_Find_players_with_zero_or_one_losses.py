"""
Complexity:
----------
Time: O(N log N)
Space: O(N)
"""
class Solution1:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_freq = defaultdict(int)
        loser_in_one_match = set()
        winners = set()
        for winner, loser in matches:
            lost_freq[loser] += 1
        
        for winner, loser in matches:
            if winner not in lost_freq:
                winners.add(winner)
            if lost_freq[loser] == 1:
                loser_in_one_match.add(loser) 
        
        return [sorted(winners), sorted(loser_in_one_match)]