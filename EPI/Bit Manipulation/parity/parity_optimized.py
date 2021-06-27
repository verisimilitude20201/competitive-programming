"""
Explanation:
-----------
number of 1s is odd -> Odd parity return 1
number of 1s is even -> even parity return 0

x & X - 1 = x with it's lower most set bit reset to 0

For example: 
5 ~ 00000101
5 - 1 = 00000100
5 & 5 - 1 = 00000101 & 00000100 = 00000100

1. Keep on computing x = x & (x - 1) till x is not 0
2. Keep on computing parity as parity ^ 1 with parity initialized to 0 initially.

"""
def parity(num):
    parity1 = 0
    while num:
        parity1 ^= 1
        num = num & (num - 1)

    return parity1


print(parity(10))