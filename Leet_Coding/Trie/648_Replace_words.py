"""
Complexity:
----------
Solution 1
----------
Time: Summation of O(w^2) from i = 1 to number of words in sentence.
Space: O(N) Number of roots in dictionary

Solution 2:
----------
Time: O(M * N) M is the average length of each root, N is the number of words in the sentence.
Space: O(M)
"""
class Solution1:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word) -> str:
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

class Solution2:
    def __init__(self):
        self._trie = {}

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.construct_trie(dictionary)
        return self.replace_word_with_root(sentence)

    def construct_trie(self, dictionary) -> None:
        for root in dictionary:
            node = self._trie
            for letter in root:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node["$"] = True

    def replace_word_with_root(self, sentence: str) -> str:
        return " ".join(map(self.replace, sentence.split()))

    def replace(self, word: str) -> str:
        node = self._trie
        i = 0
        for char in word:
            if char not in node or "$" in node:
                break
            i += 1
            node = node[char]

        return word[:i] if "$" in node else word