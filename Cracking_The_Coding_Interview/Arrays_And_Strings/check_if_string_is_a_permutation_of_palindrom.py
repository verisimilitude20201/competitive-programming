"""
Problem
-------
Check if a given string is a permutation of a palindrom string generated from it.


Complexity
---------

PalindromPermutationChecker1 ===>
    Time --> O(N) To build the character frequency map and compare if it contains utmost one character (0 or 1) that is of odd frequency
    Space --> O(d) Distinct letters in the string. 

"""


class PalindromPermutationChecker1:
    def __init__(self):
        self.__char_frequency = {}

    def is_string_permutation_of_a_palindrom(self, string):
        self._build_char_frequency_map(string)
        return self._is_no_more_than_one_odd_character()

    def _build_char_frequency_map(self, string):
        for character in string:
            if character == " ":
                continue
            character = character.lower()
            if character not in self.__char_frequency:
                self.__char_frequency[character] = 0
            self.__char_frequency[character] += 1

    def _is_no_more_than_one_odd_character(self):
        found_odd = False
        for character in self.__char_frequency:
            if self.__char_frequency[character] % 2 == 1:
                if found_odd:
                    return False
                found_odd = True
        return True


ppc = PalindromPermutationChecker()
print(ppc.is_string_permutation_of_a_palindrom("Tact coa"))