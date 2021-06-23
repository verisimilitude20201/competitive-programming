"""
Explanation:
-----------

0) 

x: 2 (0010)
num_bits = 0


1) 

x & 1 = 0010 & 0001 = 0
num_bits = 0
x >> 1 ~ x = 0001

2)

x & 1 = 0001 & 0001 = 1
num_bits = 1



-------------------------------------

0)

x: 12 (1100)
num_bits = 0

1) x & 1 = 1100 & 0001 = 0
   num_bits = 0
   x >> 1 ~ x = 0110

2) x & 1 = 0110 & 0001 = 0
   num_bits = 0
   x >> 1 ~ x = 0011 

3) x & 1 = 0011 & 0001 = 1
   num_bits = 1
   x >> 1 ~ x = 0001

4) x & 1 = 0001 & 0001 = 1
   num_bits = 2
   x >> 1 ~ x = 0000

Complexity:
----------
Time: O(N) Where N is the total number of bits representing the number
Space: O(1)
"""
def count_number_of_one_bits(num):
    num_bits = 0
    while num:
        num_bits += (num & 1)
        num = num >> 1

    return num_bits


print(count_number_of_one_bits(4))
print(count_number_of_one_bits(5))
print(count_number_of_one_bits(20))