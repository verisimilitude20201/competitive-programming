"""
Explanation:
-----------
First two solutions are pretty straight-forward. 

The 3rd one uses bit-vectors.
1. It maps each char to a unique index from 0 to 25.
2. It maintains a 26-bit vector corresponding to the index position of that char.
3. The OR includes all bit-positions included till now.
4. The AND checks a given bit position. If it's already set, that character has occurred.


Complexity:
----------

does_string_have_unique_chars1:
------------------------------
Time: O(N)
Space: O(N)

does_string_have_unique_chars2:
------------------------------
Time: O(N^2)
Space: O(N)

does_string_have_unique_chars3:
------------------------------
Time: O(N)
Space: O(1)

"""
def does_string_have_unique_chars1(string):
    string = string.lower()
    char_frequency = {}
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    for char, frequency in char_frequency.items():
        if frequency > 1:
             return False

    return True


def does_string_have_unique_chars2(string):
    string = string.lower()
    idx1 = 0
    idx2 = 1
    character_array = list(string)
    character_array = sorted(character_array)
    while idx1 < len(character_array) and idx2 < len(character_array):
        if character_array[idx1] == character_array[idx2]:
            return False
        idx1 += 1
        idx2 += 1

    return True


def does_string_have_unique_chars3(string):
    checker = 0
    string = string.lower()
    for char in string:
        char_code = ord(char) - ord("a")
        if checker & (1 << char_code) > 0:
            return False
        checker |= 1 << char_code

    return True

print(does_string_have_unique_chars1("Abhijit"))
print(does_string_have_unique_chars1("Amey"))

print(does_string_have_unique_chars2("Abhijit"))
print(does_string_have_unique_chars2("Amey"))

print(does_string_have_unique_chars3("Abhijit"))
print(does_string_have_unique_chars3("Amey"))