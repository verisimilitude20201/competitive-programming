"""
Complexity:
----------
Solution 1
-----------
Time: O(N log N)
Space: O(N)

Solution 2
-----------
Time: O(N + K)
Space: O(K)
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




class Solution2: 
    def findWinners(self, matches : List[List[int]]) ->List[List[int]]:
        max_player_num = 0
        for winner, loser in matches:
            max_player_num = max(max_player_num, winner, loser)
        
        loss_count = [-1] * (max_player_num + 1)
        for winner, loser in matches:
            if loss_count[winner] == -1:
                loss_count[winner] = 0
            if loss_count[loser] == -1:
                loss_count[loser] = 1
            else:
                loss_count[loser] += 1
        
        zero_count = []
        one_count = []
        for i, count in enumerate(loss_count):
            if count == 0:
                zero_count.append(i)
            elif count == 1:
                one_count.append(i)
        
        return [zero_count, one_count]


class Solution3: 
    def findWinners(self, matches : List[List[int]]) ->List[List[int]]:
        loss_count = defaultdict(int)
        seen = set()
        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            loss_count[loser] += 1
        
        zero_loss = []
        one_loss = []
        for player in seen:
            count = loss_count.get(player, 0)
            if count == 1:
                one_loss.append(player)
            elif count == 0:
                zero_loss.append(player)
        
        return [sorted(zero_loss), sorted(one_loss)]


class Solution4:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()
        
        for winner, loser in matches:
            if winner not in one_loss and winner not in more_losses:
                zero_loss.add(winner)
            
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser in more_losses:
                continue
            else:
                one_loss.add(loser)