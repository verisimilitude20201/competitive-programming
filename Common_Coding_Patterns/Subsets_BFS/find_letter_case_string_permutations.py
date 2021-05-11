"""
Problem:
-------
Given a string, find all of its permutations preserving the character sequence but changing case

Example:
-------
Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

Approach:
--------
Let's swap case character by character

0) "ab7c"


1) 1st character a

     "ab7c",  Ab7c

2) 2nd character b

    
    "ab7c", "aB7c", "Ab7c", "AB7c" 


3) 3rd character c

     "ab7c", "ab7C", "aB7c", "aB7C", "Ab7c", "Ab7C", "AB7c", "AB7C"

Complexity:
----------
Time: O(N * 2^N)
Space: O(2^N)

"""

def find_letter_case_string_permutations(string):
    permutations = []
    permutations.append(string)
    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(len(permutations)):
                new_permutation = list(permutations[i])
                new_permutation[j] = new_permutation[j].swapcase()
                permutations.append("".join(new_permutation))

    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
