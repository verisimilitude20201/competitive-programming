"""
Explanation
-----------
number of 1s is odd -> Odd parity return 1
number of 1s is even -> even parity return 0


0)  Compute parity of 5

00000101, result = 0

00000001

1) 00000101 & 00000001 = 1
   result = result ^ 1 = 0 ^ 1 = 1

   00000101 << 1 ~ 00000010


2) 00000010 & 00000001 = 0
   result = result ^ 1 = 0 ^ 1 = 1
   00000010 << 1 ~ 00000001

3) 00000001 & 00000001 = 1
result = 1 ^ 1 = 0
00000001 << 1 = 00000000

Parity: 0
---------

Complexity
----------
Time: O(N) N is the word size.
Space: O(1)

"""
def parity(num):
    parity1 = 0
    while num:
        parity1 ^= num & 1
        num >>= 1

    return parity1


print(parity(10))