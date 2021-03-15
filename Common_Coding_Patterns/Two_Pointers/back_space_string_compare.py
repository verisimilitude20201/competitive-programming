"""
Problem
-------
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Example:
-------

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.


0) 
       0123         0123
 str1="xy#z", str2="xzz#", index1=3, index2=3


1)     0123         0123
      "xy#z",      "xzz#", index1=3, index2=3, backspace_count = 0
          i1           i2   


      0123         0123
      "xy#z",      "xzz#", index1=3, index2=2, backspace_count = 1
          i1          i2 


       0 1 2 3         0 1 2 3
      "x y # z",      "x z z #", index1=3, index2=1, backspace_count = 0
          i1             i2


 2) 

       0 1 2 3         0 1 2 3
      "x y # z",      "x z z #", index1=2, index2=1, backspace_count = 0
          i1             i2


       0 1 2 3         0 1 2 3
      "x y # z",      "x z z #", index1=1, index2=1, backspace_count = 1
         i1              i2

       0 1 2 3         0 1 2 3
      "x y # z",      "x z z #", index1=0, index2=1, backspace_count = 0
       i1                i2

       0 1 2 3          0 1 2 3
      "x y # z",      "x z z #", index1=0, index2=1, backspace_count = 0
       i1              i2


  Return True

Approach
-------
1. Two pointers with the pointers calculating the index of the non-hash character while iterating the string from last index. viz. i1 and i2
2. Will also need two more indexes that keep track of the current position in the strings. i.e. index1 and index2
3*. After each iteration in the main while loop, we should repoint index1 and index2 to last values of i1 and i2, since they have ignored all backspaced chars. 


Complexity
---------
    Time: O(M + N) Where M and N are the lengths of the two strings
    Space: O(1)

"""


def back_space_string_compare(string1, string2):
    index1 = len(string1) - 1
    index2 = len(string2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_index_of_non_hash_char(string1, index1)
        i2 = get_index_of_non_hash_char(string2, index2)
        if string1[i1] != string2[i2]:
            return False
        if i1 < 0 or i2 < 0:
            return False
        if i1 == 0 and i2 == 0:
            return True
        index1 = i1
        index2 = i2
        index1 -= 1
        index2 -= 1

    return True


def get_index_of_non_hash_char(string, index):
    backspace_count = 0
    while index >= 0:
        if string[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1

    return index


def main():
    print(back_space_string_compare("xy#z", "xzz#"))
    print(back_space_string_compare("xy#z", "xyz#"))
    print(back_space_string_compare("xp#", "xyz##"))
    print(back_space_string_compare("xywrrmp", "xywrrmu#p"))


main()
