"""
Problem
-------
Write a function that will check if a string has unique characters

Approach for bit-vector (is_unique_chars3)
-----------------------------------------
00000000 00000000 00000000 00000000 Checker, string=abacd


1. 

0 1 2 3 4
a b a c d
_

i. Current character = a
character index = 0

ii. So, left shift  (1 << 0) by 0 bits.

1 << 0 ==> 00000000 00000000 00000000 00000001

iii. IS checker & 1 << 0 > 0 ==> FALSE

00000000 00000000 00000000 00000000 Checker

AND

00000000 00000000 00000000 00000001 1 << 0


iv. checker = checker || 1 << 0

00000000 00000000 00000000 00000000 Checker

OR

00000000 00000000 00000000 00000001 1 << 0

00000000 00000000 00000000 00000001 Checker (Position of a remembered)


2. 

0 1 2 3 4
a b a c d
  _

i. Current character = b
character index = 1

ii. So, left shift  (1 << 1) by 1 bits.

1 << 1 ==> 00000000 00000000 00000000 00000010

iii. IS checker & 1 << 1 > 0 ==> FALSE

00000000 00000000 00000000 00000001 Checker

AND

00000000 00000000 00000000 00000010 1 << 1


iv. checker = checker || 1 << 1

00000000 00000000 00000000 00000001 Checker

OR

00000000 00000000 00000000 00000010 1 << 1

00000000 00000000 00000000 00000011 Checker (Position of a and b remembered)



3. 

0 1 2 3 4
a b a c d
    _

i. Current character = a
character index = 0

ii. So, left shift  (1 << 0) by 0 bits.

1 << 0 ==> 00000000 00000000 00000000 00000010

iii. IS checker & 1 << 0 == 0 ==> TRUE

00000000 00000000 00000000 00000011 Checker

AND

00000000 00000000 00000000 00000001 1 << 0

So the string has a duplicate character

Complexity:
----------
is_unique_chars1: 
    Time: O(N + u) -> N is the characters in the string and u is the number of unique characters
    Space: O(u) --> Required for HashMap to store u number of unique chars


is_unique_chars2:
    Time: O(N) 
    Space: O(u)

is_unique_chars3:
    Time: O(N) 
    Space: O(1) ---> Bit vector takes constant space, native integer representation of platform.

"""


def is_unique_chars1(string1):
    char_frequency = {}
    for i in range(len(string1)):
        char = string1[i]
        if char not in char_frequency:
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1

    for char in char_frequency:
        if char_frequency[char] > 1:
            return False

    return True


def is_unique_chars2(string):
    if len(string) > 128:
        return False

    char_unique = {}

    for char in string:
        if char in char_unique and char_unique[char]:
            return False
        char_unique[char] = True

    return True


def is_unique_chars3(string):
    checker = 0
    for char in string:
        char_index = ord(char.lower()) - ord("a")
        bit_index_for_char = 1 << char_index
        if checker & bit_index_for_char > 0:
            return False
        checker = checker | bit_index_for_char

    return True


print(is_unique_chars1("Abhijt"))
print(is_unique_chars2("Abhijt"))
print(is_unique_chars3("Abhijt"))