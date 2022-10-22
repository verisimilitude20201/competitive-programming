"""
Complexity:
----------

Time: 
-----
 O(N) + O(MAX(K, L)) ~= O(N). The reason this is MAX(K, L) and not MIN(K, L)
K = [1, 5], L = [1, 2, 3, 4]


Space: O(N)
"""
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self._positions = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self._positions[word].append(i)
            
        

    def shortest(self, word1: str, word2: str) -> int:
        d_w1 = self._positions[word1]
        d_w2 = self._positions[word2]
        shortest = math.inf
        i = 0
        j = 0
        while i < len(d_w1) and j < len(d_w2):
            shortest = min(shortest, abs(d_w1[i] - d_w2[j]))
            if d_w1[i] < d_w2[j]:
                i += 1
            else:
                j += 1
        
        return shortest