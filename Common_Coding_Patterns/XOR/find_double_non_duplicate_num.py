"""
Problem:
-------
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. 
Find the two numbers that appear only once.

Example:
-------
[2, 1, 3, 2], should output 1 and 3

Approach:
--------
1      0001  
2      0010
3      0011
4      0100
5      0101


0) [2, 1, 3, 2], should output 1 and 3


1)

x1 = 0000
x1 = 0000 XOR 0010(2) = 0010
x2 = 0010 XOR 0001(1) = 0011
x2 = 0011 XOR 0011(3) = 0000
x4 = 0000 XOR 0010 = 0010

num1 XOR num2 = 0010 (i.e. 1 XOR 3 = 2)


2) Find any bit set in num1 XOR num2

   right_most_bit_set = 0001, num1 XOR num2 = 0010

   i) 
      Is the 1st bit from LHS set? 0001 & 0010 = 0 ~ True
      Left shift right_most_bit by 1 = 0010

   ii) Is the second bit from LHS set? 0010 & 0010 = 1 False

   right_most_bit_set = 0010

3) Partition elements according to when the bit 3 is set or not
   num1 = 0000
   num2 = 0000

   i) num = 2 (0010), bit 3 is set so
      num1 = 0010 XOR 0000 = 0010
      num2 = 0000

   ii) num = 1 (0001), bit 3 is reset so
       num1 = 0010
       num2 = 0000 XOR 0001 = 0001

   iii) num = 3 (0011) bit 3 is set so
        num1 = 0010 XOR 0011 = 0001
        num2 = 0001

    iv) num = 2 (0010) bit 3 is set so
        num1 = 0001 XOR 0010 = 0011
        num2 = 0001

    [3, 1]

Complexity:
----------
Time: O(N)
Space: O(1)

"""

def find_double_non_duplicate_num(arr):
    num1 = 0
    num2 = 0
    num1_xor_num2 = 0
    for num in arr:
        num1_xor_num2 ^= num

    right_most_set_bit = 1
    while num1_xor_num2 & right_most_set_bit == 0:
        right_most_set_bit = right_most_set_bit << 1

    for num in arr:
        if num & right_most_set_bit == 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_double_non_duplicate_num([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_double_non_duplicate_num([2, 1, 3, 2])))


main()
