"""
Complexity:
----------
is_permutation_of_a_palindrome1
-------------------------------
Time: O(N)
Space: O(1) Considering the map can store at the max only 26 lower case characters

is_permutation_of_a_palindrome2
-------------------------------
Time: O(N)
Space: O(1) Because we are maintaining the array of characters as a 26-bit number.

is_permutation_of_a_palindrome3
-------------------------------
Time: O(N)
Space: O(1) Because we are maintaining the array of characters as a 26-bit bit-vector
"""
def is_permutation_of_a_palindrome1(string):
    string = string.lower()
    char_code_for_a = ord("a")
    char_code_for_z = ord("z")

    char_frequency = {}
    for char in string:
        if char_code_for_a <= ord(char) <= char_code_for_z:
            char_frequency[char] = char_frequency.get(char, 0) + 1

    found_odd_frequency = False
    for char, char_frequency in char_frequency.items():
        if char_frequency % 2 != 0:
            if found_odd_frequency:
                return False

            found_odd_frequency = True

    return True

def is_permutation_of_a_palindrome2(string):
    string = string.lower()
    char_code_for_a = ord("a")
    char_code_for_z = ord("z")
    bit_vector = 0
    for char in string:
        char_code = ord(char)

        if char_code_for_a <= char_code <= char_code_for_z:
            char_index = char_code - char_code_for_a
            mask = 1 << char_index
            if (bit_vector & mask) == 0:
                bit_vector |= mask
            else:
                bit_vector &= ~mask

    return bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0

print(is_permutation_of_a_palindrome2("Taco Coa"))

def is_palindrom_permutation3(string):
    bit_vector = create_bit_vector(string)
    return bit_vector == 0 or (((bit_vector - 1) & bit_vector) == 0)


def create_bit_vector(string):
    ord_a = ord("a")
    ord_z = ord("z")
    bit_vector = 0
    for char in string:
         if ord_a <= ord(char) <= ord_z:
             index = ord(char) - ord_a
             mask = 1 << index
             if bit_vector & mask == 0:
                 bit_vector |= mask
             else:
                 bit_vector &= ~mask

    return bit_vector


print(is_palindrom_permutation3("abcb"))