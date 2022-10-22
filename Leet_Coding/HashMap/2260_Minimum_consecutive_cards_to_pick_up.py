from collections import defaultdict
import math


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_positions = defaultdict(list)
        for i, card in enumerate(cards):
            card_positions[card].append(i)
        
        ans = math.inf
        for card in card_positions:
            if len(card_positions[card]) > 1:
                positions = card_positions[card]
                for i in range(len(positions) - 1):
                    ans = min(ans, positions[i + 1] - positions[i] + 1)
        
        if ans == math.inf:
            return -1
        return ans