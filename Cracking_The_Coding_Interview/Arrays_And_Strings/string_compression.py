"""
Problem:
-------
Design an algorithm that takes input a string and returns its compressed version.
For example: For the string "aabcccccaaa", it should print "a2b1c5a2"

Complexity:
----------
Time O(N): N is the number of characters in string
Space O(c + n): Where c is the number of character occurences in string and n is the number of digits. 
"""

def compress_string(string):
    if len(string) == 0:
        return ""
    letter_count = 1
    i = 0
    j = 1
    compressed = []
    while j < len(string):
        if string[i] != string[j] or j == len(string) - 1:
            compressed.append(string[i])
            compressed.append(str(letter_count))
            letter_count = 1
        else:
            letter_count += 1

        i += 1
        j += 1

    return compressed


print("".join(compress_string("aabcccccaaa")))