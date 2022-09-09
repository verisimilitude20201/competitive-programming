"""
Complexity:
----------
AutocompleteSystem1 (Without Trie)
---------------------------------
Time: O(N log N)
Space: O(N^2)

AutocompleteSystem1 (With Trie)
"""
class AutocompleteSystem1:

    def __init__(self, sentences: List[str], times: List[int]):
        self._history = defaultdict(int)
        self._matches = []
        for i in range(len(sentences)):
            self._history[sentences[i]] = times[i]
        self._search = []

    def input(self, c: str) -> List[str]:
        if c == "#":
            self._matches = []
            self._history["".join(self._search)] += 1
            self._search = []
            return
        
        if not self._search:
            self._matches = [[sentence, times] for sentence, times in self._history.items() if sentence[0] == c]
            self._matches.sort(key=lambda x: (-x[1], x[0]))
            self._matches = [x[0] for x in self._matches]
        else:
            i = len(self._search)
            self._matches = [match for match in self._matches if len(match) > i and match[i] == c]
        
        self._search.append(c)
            
        return self._matches[:3]