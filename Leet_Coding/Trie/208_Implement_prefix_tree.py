"""
Complexity:

Trie1: HashMap Internals
------------------------
Time: O(N) -> N: Length of the longest word
Space: O(M * N * K) Where M is the number of words, N avg length of the words and K is the number of alphabets 
"""
class TrieNode1:
    def __init__(self):
        self._links = dict()
        self._is_end = False

    def get_links(self, char: str) -> dict:
        if char not in self._links:
            return None
        return self._links[char]

    def set_links(self, char):
        self._links[char] = TrieNode()

    def get_is_end(self) -> bool:
        return self._is_end

    def set_is_end(self, is_end: bool):
        self._is_end = is_end


class Trie1:
    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        current = self._root
        for char in word:
            if not current.get_links(char):
                current.set_links(char)
            current = current.get_links(char)
        current.set_is_end(True)

    def search(self, word: str) -> bool:
        current = self._root
        for char in word:
            if not current.get_links(char):
                return False
            current = current.get_links(char)
        return current.get_is_end()

    def startsWith(self, prefix: str) -> bool:
        current = self._root
        for char in prefix:
            if not current.get_links(char):
                return False
            current = current.get_links(char)

        return True