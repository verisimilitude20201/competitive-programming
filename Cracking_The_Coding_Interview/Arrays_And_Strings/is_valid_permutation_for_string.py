"""
Problem
-------
Check whether a string is a valid permutation of the other

Complexity:
----------

is_valid_string_permutation1 --> 
    Time - O(N)
    Space - O(c) Where c is the unique number of characters in the input string

is_valid_string_permutation2 -->
    Time - O(N log N)
    Space - O(N) An N character array gets created and joined in-memory. Further more after sorting, two new strings are created.

"""

def is_valid_string_permutation1(string, permutation_string):
    if len(string) != len(permutation_string):
        return False

    char_frequency = {}
    for character in string:
        if character not in char_frequency:
            char_frequency[character] = 0
        char_frequency[character] += 1

    for char in permutation_string:
        if char in char_frequency:
            char_frequency[char] -= 1
            if char_frequency[char] == 0:
                del char_frequency[char]

    return len(char_frequency) == 0


def is_valid_string_permutation2(string, permutation_string):
    if len(string) != len(permutation_string):
        return False

    def sort_string(s):
        return "".join(sorted(s))

    sorted_string = sort_string(string)
    permutation_string = sort_string(permutation_string)

    return sorted_string == permutation_string



print(is_valid_string_permutation2("AABB", "BACA"))
