"""
Explanation:
------------
WordDictionary1
---------------
Not efficient for more practical use-cases.
    - Does not scale for large data sets
    - Enumerate a dataset of strings in lexicographical order 
    - Find keys with a common prefix.

Complexity:
----------
Time: O(M * N) Where M is the key length. As hash table increases, there are a lot of collisions fur
ther increasing this O(M^2 * N)
Space: O(M) assuming none of the words has a common prefix.

"""
class WordDictionary1:

    def __init__(self):
        self.dictionary = defaultdict(set)
        

    def addWord(self, word: str) -> None:
        self.dictionary[len(word)].add(word)
        

    def search(self, word: str) -> bool:
        length = len(word)
        dict_words = self.dictionary[length]
        for dict_word in dict_words:
            i = 0
            while i < length and (dict_word[i] == word[i] or word[i] == "."):
                i += 1
            if i == length:
                return True
        
        return False