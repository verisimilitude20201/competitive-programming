"""
Explanation:
-----------
Time: O(N)
Space: O(d * S * t) Where d is the number of words in dictionary with a given abbreviation
and S is the average length of word, t is the number of words with the same abbreviation
"""
from typing import List

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.__abbr_map = {}
        self.__abbr_dict(dictionary)

    def __abbr_dict(self, dictionary):
        for word in dictionary:
            abbr = self.__get_word_abbr(word)
            if abbr not in self.__abbr_map:
                self.__abbr_map[abbr] = word

    def isUnique(self, word: str) -> bool:
        abbr = self.__get_word_abbr(word)
        stored_word = None
        if abbr in self.__abbr_map:
            stored_word = self.__get_word_abbr[abbr]

        return stored_word is None or stored_word == word

    def __get_word_abbr(self, word: str) -> str:
        if len(word) == 2:
            return word
        char_count_excluding_first_last = len(word) - 2
        return "".join([word[0], str(char_count_excluding_first_last), word[-1]])




